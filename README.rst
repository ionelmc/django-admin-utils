===========================
    django-admin-utils
===========================

Utility code and patterns. Tested against Python 2.7, 2.6 and Django 1.3, 1.4, 1.5, 1.6 (trunk).

.. image:: https://secure.travis-ci.org/ionelmc/django-admin-utils.png
    :alt: Build Status
    :target: http://travis-ci.org/ionelmc/django-admin-utils

.. image:: https://coveralls.io/repos/ionelmc/django-admin-utils/badge.png?branch=master
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/django-admin-utils

.. image:: https://badge.fury.io/py/django-admin-utils.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/django-admin-utils

.. image:: https://d2weczhvl823v0.cloudfront.net/ionelmc/django-admin-utils/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

Terse admin.py
==============

::

    from django.contrib import admin
    from admin_utils import register, inline

    from .models import MyModel, OtherModel

    @register(MyModel)
    class MyModelAdmin(admin.ModelAdmin):
        inlines = inline(OtherModel),

If you want custom admin sites::

    customsite = admin.AdminSite()

    @register(MyModel, site=customsite)
    class MyModelAdmin(admin.ModelAdmin):
        inlines = inline(OherModel),


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

To use different admin site::

    make_admin_class("Test1", patterns("test_app.views",
        url(r'^$', 'root', name='test_app_test1_changelist'),
        url(r'^level1/$', 'level1', name='level-1'),
        url(r'^level1/level2/$', 'level2', name='level-2'),
    ), "test_app", site=customsite)

Admin mixins
============

admin_utils.mixins.FoldableListFilterAdminMixin
-----------------------------------------------

Adds nice filter toggling with cookie support. Largely based on `django-foldable-list-filter
<https://bitbucket.org/Stanislas/django-foldable-list-filter>`_ but without the transition effect and no pictures.

Example::

    from admin_utils.mixins import FoldableListFilterAdminMixin

    class MyModelAdmin(FoldableListFilterAdminMixin, admin.ModelAdmin):
        pass

Looks like this:

    .. image:: docs/FoldableListFilterAdminMixin.png
       :alt: Screenshort of FoldableListFilterAdminMixin

admin_utils.mixins.FullWidthAdminMixin
--------------------------------------

Make the changelist expand instead of having the width of the windows and having that nasty inner scrollbar. You never gonna notice that if
your table is long !

Example::

    from admin_utils.mixins import FoldableListFilterAdminMixin

    class MyModelAdmin(FoldableListFilterAdminMixin, admin.ModelAdmin):
        pass

You probably didn't even notice you had this problem:

.. image:: docs/FullWidthAdminMixin.png
   :alt: Screenshort of FullWidthAdminMixin



