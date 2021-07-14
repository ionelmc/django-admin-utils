try:
    from django.urls import re_path as url
except ImportError:
    from django.conf.urls import url

from test_app import views

from admin_utils import make_admin_class

make_admin_class("Test1", [
    url(r'^$', views.root, name='test_app_test1_changelist'),
    url(r'^level1/$', views.level1, name='level-1'),
    url(r'^level1/level2/$', views.level2, name='level-2'),
], "test_app")

make_admin_class("Test2", [
    url(r'^$', views.root, name='test_app_test2_changelist'),
], "test_app")
