===========================
    django-admin-utils
===========================

| |docs| |travis| |appveyor| |coveralls| |landscape| |scrutinizer|
| |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/django-admin-utils/badge/?style=flat
    :target: https://readthedocs.org/projects/django-admin-utils
    :alt: Documentation Status

.. |travis| image:: http://img.shields.io/travis/ionelmc/django-admin-utils/master.png?style=flat
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/django-admin-utils

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ionelmc/django-admin-utils?branch=master
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/django-admin-utils

.. |coveralls| image:: http://img.shields.io/coveralls/ionelmc/django-admin-utils/master.png?style=flat
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/django-admin-utils

.. |landscape| image:: https://landscape.io/github/ionelmc/django-admin-utils/master/landscape.svg?style=flat
    :target: https://landscape.io/github/ionelmc/django-admin-utils/master
    :alt: Code Quality Status

.. |version| image:: http://img.shields.io/pypi/v/django-admin-utils.png?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/django-admin-utils

.. |downloads| image:: http://img.shields.io/pypi/dm/django-admin-utils.png?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/django-admin-utils

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-admin-utils.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/django-admin-utils

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/django-admin-utils.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/django-admin-utils

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/django-admin-utils.svg?style=flat
    :alt: Supported imlementations
    :target: https://pypi.python.org/pypi/django-admin-utils

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/ionelmc/django-admin-utils/master.png?style=flat
    :alt: Scrtinizer Status
    :target: https://scrutinizer-ci.com/g/ionelmc/django-admin-utils/

Utility code and patterns. 

Requirements
============

:OS: Any
:Runtime: Python 2.6, 2.7, 3.2, 3.3 or PyPy
:Packages: Django>=1.4 (including 1.7); Django>=1.1 probably works but it's not tested, those releases should not be used (they are insecure).

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

    .. image:: https://raw.githubusercontent.com/ionelmc/django-admin-utils/master/docs/FoldableListFilterAdminMixin.png
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

.. image:: https://raw.githubusercontent.com/ionelmc/django-admin-utils/master/docs/FullWidthAdminMixin.png
   :alt: Screenshort of FullWidthAdminMixin



