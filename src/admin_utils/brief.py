from django.contrib import admin

def register(model):
    def decorator(klass, site=admin.site):
        site.register(model, klass)
        return klass
    return decorator

def inline(model, klass=admin.TabularInline, **options):
    return type(
        "%sInlineAdmin" % model.__name__,
        (klass,),
        dict(model=model, **options)
    )
