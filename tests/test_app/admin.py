from django.urls import path
from test_app import views

from admin_utils import make_admin_class

make_admin_class("test_app", "Test1", [
    path('', views.root, name='test_app_test1_changelist'),
    path('level1/', views.level1, name='level-1'),
    path('level1/level2/', views.level2, name='level-2'),
])

make_admin_class("test_app", "Test2", [
    path('', views.root, name='test_app_test2_changelist'),
])
