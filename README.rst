===========================
    django-admin-utils
===========================

Utility code and patterns.

Terse admin.py
==============

::
    
    from django.contrib import admin
    from admin_utils import register, inline
    
    from .models import MyModel, OtherModel
    
    @register(MyModel)
    class MyModelAdmin(admin.ModelAdmin):
        inlines = inline(OtherModel),
