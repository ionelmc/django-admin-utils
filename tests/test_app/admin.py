try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url
from admin_utils import make_admin_class

make_admin_class("Test1", patterns("test_app.views",
    url(r'^$', 'root', name='test_app_test1_changelist'),
    url(r'^level1/$', 'level1', name='level-1'),
    url(r'^level1/level2/$', 'level2', name='level-2'),
), "test_app")

make_admin_class("Test2", patterns("test_app.views",
    url(r'^$', 'root', name='test_app_test2_changelist'),
), "test_app")
