========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |travis| |requires|
        | |coveralls| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |travis| image:: https://api.travis-ci.com/ionelmc/django-admin-utils.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/ionelmc/django-admin-utils

.. |requires| image:: https://requires.io/github/ionelmc/django-admin-utils/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ionelmc/django-admin-utils/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/ionelmc/django-admin-utils/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/django-admin-utils

.. |codecov| image:: https://codecov.io/gh/ionelmc/django-admin-utils/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ionelmc/django-admin-utils

.. |version| image:: https://img.shields.io/pypi/v/django-admin-utils.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/django-admin-utils

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-admin-utils.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/django-admin-utils

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/django-admin-utils.svg
    :alt: Supported versions
    :target: https://pypi.org/project/django-admin-utils

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/django-admin-utils.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/django-admin-utils

.. |commits-since| image:: https://img.shields.io/github/commits-since/ionelmc/django-admin-utils/v2.0.4.svg
    :alt: Commits since latest release
    :target: https://github.com/ionelmc/django-admin-utils/compare/v2.0.4...master



.. end-badges

Utility code and patterns.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install django-admin-utils

You can also install the in-development version with::

    pip install https://github.com/ionelmc/django-admin-utils/archive/master.zip

Documentation
=============

Terse admin.py
--------------

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
-----------------------------------------------------------

Have you ever wanted a page in the admin that appears in the app list but you don't have any
models ? Now you can have that without patching up the admin Site or the templates. Just put this
in your admin.py::

    from django.urls import path
    from admin_utils import make_admin_class

    make_admin_class(
        app_label="test_app",
        model_name="Test1",
        urls=[
            path('', views.root, name='test_app_test1_changelist'),
            path('level1/', views.level1, name='level-1'),
            path('level1/level2/', views.level2, name='level-2'),
        ],
    )

To use different admin site::

    make_admin_class(
        site=customsite,
        app_label="test_app",
        model_name="Test1",
        urls=[
            path('', views.root, name='test_app_test1_changelist'),
            path('level1/', views.level1, name='level-1'),
            path('level1/level2/', views.level2, name='level-2'),
        ],
    )

Alternatively you can mount a single view with a decorator::

    from admin_utils import register_view

    @register_view(
        site=customsite,
        app_label="test_app",
        model_name="Test1",
    )
    def root(request):
        ...


Admin mixins
------------

admin_utils.mixins.FoldableListFilterAdminMixin
```````````````````````````````````````````````

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
``````````````````````````````````````

Make the changelist expand instead of having the width of the windows and having that nasty inner scrollbar. You never gonna notice that if
your table is long !

Example::

    from admin_utils.mixins import FoldableListFilterAdminMixin

    class MyModelAdmin(FoldableListFilterAdminMixin, admin.ModelAdmin):
        pass

You probably didn't even notice you had this problem:

.. image:: https://raw.githubusercontent.com/ionelmc/django-admin-utils/master/docs/FullWidthAdminMixin.png
   :alt: Screenshort of FullWidthAdminMixin
