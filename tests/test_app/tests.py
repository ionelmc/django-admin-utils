import pytest
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from admin_utils.mock import InvalidAdmin
from test_app import views

from .admin import make_admin_class
from .admin import path


class MockAdminTestCase(TestCase):
    def setUp(self):
        self.user = User(
            username='test',
            email='test@example.com',
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )
        self.user.set_password('test')
        self.user.save()
        self.client.login(username='test', password='test')  # noqa:S106

    def test_admin_not_broken(self):
        response = self.client.get('/admin/')
        self.assertContains(response, '/admin/password_change/')
        self.assertNotContains(response, "You don't have permission to edit anything")

    def test_admin_auth_not_broken(self):
        response = self.client.get('/admin/auth/')
        assert response.status_code == 200, response

    def test_admin_auth_user_not_broken(self):
        url = reverse('admin:auth_user_changelist')
        assert url == '/admin/auth/user/'
        response = self.client.get(url)
        assert response.status_code == 200, response

    def test_admin_shows_in_applist(self):
        url = reverse('admin:app_list', kwargs={'app_label': 'test_app'})
        assert url == '/admin/test_app/'
        response = self.client.get(url)
        assert response.status_code == 200, response
        assert b'>Test1<' in response.content, response
        assert b'href="/admin/test_app/test1/"' in response.content, response
        assert b'>Test2<' in response.content, response
        assert b'href="/admin/test_app/test2/"' in response.content, response

    def test_admin_shows_in_index(self):
        url = reverse('admin:index')
        assert url == '/admin/'
        response = self.client.get(url)
        assert response.status_code == 200, response
        assert b'>Test1<' in response.content, response
        assert b'href="/admin/test_app/test1/"' in response.content, response
        assert b'>Test2<' in response.content, response
        assert b'href="/admin/test_app/test2/"' in response.content, response

    def test_admin_1_root(self):
        url = reverse('admin:test_app_test1_changelist')
        assert url == '/admin/test_app/test1/'
        self.assertRedirects(self.client.get(url.rstrip('/')), url, 301)
        response = self.client.get(url)
        assert response.status_code == 200, response
        assert response.content == b'root', response

    def test_admin_1_level1(self):
        url = reverse('admin:level-1')
        assert url == '/admin/test_app/test1/level1/'
        self.assertRedirects(self.client.get(url.rstrip('/')), url, 301)
        response = self.client.get(url)
        assert response.status_code == 200, response
        assert response.content == b'level1', response

    def test_admin_1_level1_level2(self):
        url = reverse('admin:level-2')
        assert url == '/admin/test_app/test1/level1/level2/'
        self.assertRedirects(self.client.get(url.rstrip('/')), url, 301)
        response = self.client.get(url)
        assert response.status_code == 200, response
        assert response.content == b'level2', response

    def test_admin_2_root(self):
        url = reverse('admin:test_app_test2_changelist')
        assert url == '/admin/test_app/test2/'
        self.assertRedirects(self.client.get(url.rstrip('/')), url, 301)
        response = self.client.get(url)
        assert response.status_code == 200, response
        assert response.content == b'root', response

    def test_runtime_error(self):
        with pytest.raises(InvalidAdmin):
            make_admin_class(
                'test_app',
                'Test',
                [
                    path('', views.root, name='whatever'),
                ],
            )

    def test_page(self):
        url = reverse('admin:test_app_page_changelist')
        assert url == '/admin/test_app/page/'
        self.assertRedirects(self.client.get(url.rstrip('/')), url, 301)
        response = self.client.get(url)
        assert response.status_code == 200, response
        assert response.content.startswith(b'<!DOCTYPE')
