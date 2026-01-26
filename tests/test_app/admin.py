from types import SimpleNamespace

from django.contrib import admin
from django.shortcuts import render
from django.urls import path

from admin_utils import make_admin_class
from admin_utils import register_view
from test_app import views

make_admin_class(
    'test_app',
    'Test1',
    [
        path('', views.root, name='test_app_test1_changelist'),
        path('level1/', views.level1, name='level-1'),
        path('level1/level2/', views.level2, name='level-2'),
    ],
)

make_admin_class(
    'test_app',
    'Test2',
    [
        path('', views.root, name='test_app_test2_changelist'),
    ],
)


@register_view(
    'test_app',
    'Page',
    verbose_name='Page',
    verbose_name_plural='Page',
)
def page(request):
    return render(
        request,
        'admin/change_list.html',
        {
            **admin.site.each_context(request),
            'action_form': None,
            'cl': SimpleNamespace(
                can_show_all=False,
                formset=None,
                full_result_count=0,
                get_ordering_field_columns=list,
                has_filters=False,
                list_display=[],
                multi_page=False,
                opts=page.fake_model._meta,
                result_count=0,
                result_list=[],
                show_all=False,
                date_hierarchy=None,
                search_fields=[],
            ),
            'has_add_permission': False,
            'opts': page.fake_model._meta,
            'title': '123',
            'subtitle': '234',
            'verbose_name': '123',
            'verbose_name_plural': '123',
        },
    )
