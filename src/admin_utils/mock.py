from functools import update_wrapper

from django.contrib import admin

try:
    from django.core.urlresolvers import RegexURLPattern
except ImportError:
    from django.urls.resolvers import RegexPattern as RegexURLPattern


class InvalidAdmin(RuntimeError):
    pass


def make_admin_class(name, urls, app_label, dont_register=False,
                     site=admin.site):
    label = app_label

    required_name = "%s_%s_changelist" % (app_label, name.lower())
    for url in urls:
        if getattr(url, 'name', None) == required_name:
            break
    else:
        raise InvalidAdmin(
            "You must have an url with the name %r otherwise the admin "
            "will fail to reverse it." % required_name
        )

    class _meta:
        abstract = False
        app_label = label
        app_config = None
        module_name = name.lower()
        verbose_name_plural = name
        verbose_name = name
        model_name = name.lower()
        object_name = name
        swapped = False
    model_class = type(name, (object,), {'_meta': _meta})

    class admin_class(admin.ModelAdmin):
        def has_add_permission(*args):
            return False

        def has_change_permission(*args):
            return True

        def has_delete_permission(*args):
            return False

        def get_urls(self):
            def wrap(view):
                def wrapper(*args, **kwargs):
                    return self.admin_site.admin_view(view)(*args, **kwargs)
                return update_wrapper(wrapper, view)

            return [  # they are already prefixed
                RegexURLPattern(
                    str(url.regex.pattern),
                    wrap(url.callback),
                    url.default_args,
                    url.name
                )
                if isinstance(url, RegexURLPattern)
                else url
                for url in urls
            ]

        @classmethod
        def register(cls):
            site.register((model_class,), cls)
    if not dont_register:
        admin_class.register()
    return admin_class
