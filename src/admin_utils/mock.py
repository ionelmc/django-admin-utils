from functools import update_wrapper
from django.contrib import admin

def make_admin_class(name, urls, app_label, dont_register=False):
    label = app_label

    class _meta:
        abstract = False
        app_label = label
        module_name = name.lower()
        verbose_name_plural = name
        verbose_name = name
        model_name = name.lower()
        object_name = name
        swapped = False
    model_class = type(name, (object,), {'_meta': _meta})

    class admin_class(admin.ModelAdmin):
        has_add_permission = lambda *args: False
        has_change_permission = lambda *args: True
        has_delete_permission = lambda *args: False

        def get_urls(self):
            def wrap(view):
                def wrapper(*args, **kwargs):
                    return self.admin_site.admin_view(view)(*args, **kwargs)
                return update_wrapper(wrapper, view)
            from django.core.urlresolvers import RegexURLPattern
            return [ # they are already prefixed
                RegexURLPattern(
                    str(url.regex.pattern),
                    wrap(url.callback),
                    url.default_args,
                    url.name
                ) if isinstance(url, RegexURLPattern)
                  else url
                for url in urls
            ]

        @classmethod
        def register(cls):
            admin.site.register((model_class,), cls)
    if not dont_register:
        admin_class.register()
    return admin_class
