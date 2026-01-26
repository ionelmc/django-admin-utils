
Changelog
=========

2.2.0 (2026-01-26)
------------------

* Added Django 6.0 in test grid. Dropped Django 5.0 or older.
* Added a missing 'label' attribute to fake models. Should allow you to use `pghistory.admin` as long as you have an adequate `get_model` in your `AppConfig`.

2.1.0 (2025-03-22)
------------------

* Added support for Django 5.2.
* Increased minimum versions to Django 4.2 and Python 3.9.

2.0.4 (2021-07-19)
------------------

* Fixed mock admin regression and add test.

2.0.3 (2021-07-19)
------------------

* Made the mock admin behave as without editable permissions (implemented the missing ``has_view_permission`` method).

2.0.2 (2021-07-18)
------------------

* Exposed the fake hidden model as a ``fake_model`` attribute.

2.0.1 (2021-07-18)
------------------

* Added missing import for ``admin_utils.register_view``.

2.0.0 (2021-07-18)
------------------

* Dropped support for Python 2.7 and Django 1.11.
* Added the ``register_view`` decorator.
* Update examples/readme.
* Various bugfixes.

1.0.0 (2021-07-14)
------------------

* Fixed a bunch of regressions with Django 3.2.

0.3.0 (2014-02-02)
------------------

* Forgot to add any details.
