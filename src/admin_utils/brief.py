from django.contrib import admin


def register(model, site=admin.site):
    def decorator(klass):
        site.register(model, klass)
        return klass

    return decorator


def inline(model, klass=admin.TabularInline, **options):
    return type(f'{model.__name__}InlineAdmin', (klass,), dict(model=model, **options))
