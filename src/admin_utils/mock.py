from functools import update_wrapper

from django.contrib import admin
from django.urls import path
from django.urls.resolvers import URLPattern


class InvalidAdmin(RuntimeError):
    pass


def fake_model_factory(**kwargs):
    type_name = f'Fake{kwargs["model_name"]}Model'

    class _meta:
        abstract = kwargs.pop('abstract')
        app_label = kwargs.pop('app_label')
        app_config = kwargs.pop('app_config')
        module_name = kwargs.pop('module_name')
        verbose_name_plural = kwargs.pop('verbose_name_plural')
        verbose_name = kwargs.pop('verbose_name')
        model_name = kwargs.pop('model_name')
        object_name = kwargs.pop('object_name')
        swapped = kwargs.pop('swapped')
        is_composite_pk = False
        label = f'{app_label}.{model_name}'

    if kwargs:
        raise InvalidAdmin(f'Unexpected arguments: {kwargs}')
    return type(type_name, (object,), {'_meta': _meta})


def register_view(app_label, model_name, **kwargs):
    def register_admin_decorator(view_func):
        urls = [
            path('', view_func, name=f'{app_label}_{model_name.lower()}_changelist'),
        ]
        return make_admin_class(app_label, model_name, urls, **kwargs)

    return register_admin_decorator


def make_admin_class(
    app_label,
    model_name,
    urls,
    register=True,
    site=admin.site,
    **kwargs,
):
    required_name = f'{app_label}_{model_name.lower()}_changelist'
    for url in urls:
        if getattr(url, 'name', None) == required_name:
            break
    else:
        raise InvalidAdmin(f'You must have an url with the name {required_name!r} otherwise the admin will fail to reverse it.')
    if 'app_label' in kwargs:
        raise InvalidAdmin(f'Got multiple values for app_label ({app_label}/{kwargs["app_label"]})')
    if 'model_name' in kwargs:
        raise InvalidAdmin(f'Got multiple values for model_name ({model_name}/{kwargs["model_name"]})')
    for url in urls:
        if not isinstance(url, URLPattern):
            raise InvalidAdmin(f'Unexpected url {url}')

    kwargs['model_name'] = model_name.lower()
    kwargs['app_label'] = app_label
    kwargs.setdefault('abstract', False)
    kwargs.setdefault('app_config', None)
    kwargs.setdefault('module_name', model_name.lower())
    kwargs.setdefault('verbose_name_plural', model_name)
    kwargs.setdefault('verbose_name', model_name)
    kwargs.setdefault('object_name', model_name)
    kwargs.setdefault('swapped', False)

    FakeModel = fake_model_factory(**kwargs)

    class FakeModelAdminClass(admin.ModelAdmin):
        fake_model = FakeModel

        def has_view_permission(*args, **kwargs):
            return True

        def has_add_permission(*args, **kwargs):
            return False

        def has_change_permission(*args, **kwargs):
            return False

        def has_delete_permission(*args, **kwargs):
            return False

        def get_urls(self):
            def wrap(view):
                def wrapper(*args, **kwargs):
                    return self.admin_site.admin_view(view)(*args, **kwargs)

                wrapper.model_admin = self
                return update_wrapper(wrapper, view)

            return [
                URLPattern(
                    pattern=url.pattern,
                    callback=wrap(url.callback),
                    default_args=url.default_args,
                    name=url.name,
                )
                for url in urls
            ]

        @classmethod
        def register(cls):
            site.register((FakeModel,), cls)

    if register:
        FakeModelAdminClass.register()
    return FakeModelAdminClass
