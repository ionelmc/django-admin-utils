===========================
    django-admin-utils
===========================

Utility code and patterns. Tested against Python 2.7, 2.6 and Django 1.3, 1.4, 1.5, 1.6 (trunk).

Terse admin.py
==============

::
    
    from django.contrib import admin
    from admin_utils import register, inline
    
    from .models import MyModel, OtherModel
    
    @register(MyModel)
    class MyModelAdmin(admin.ModelAdmin):
        inlines = inline(OtherModel),

Mock admin (mount your views in admin using model wrappers)
===========================================================

Have you ever wanted a page in the admin that appears in the app list but you don't have any 
models ? Now you can have that without patching up the admin Site or the templates. Just put this 
in your admin.py::
    
    from django.conf.urls import patterns, url
    from admin_utils import make_admin_class

    make_admin_class("Test1", patterns("test_app.views",
        url(r'^$', 'root', name='test_app_test1_changelist'),
        url(r'^level1/$', 'level1', name='level-1'),
        url(r'^level1/level2/$', 'level2', name='level-2'),
    ), "test_app")
