from django.test.client import Client
from django.test import TestCase
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse

class MockAdminTestCase(TestCase):
    def setUp(self):
        self.user = User(
            username='test', email='test@example.com', is_active=True,
            is_staff=True, is_superuser=True,
        )
        self.user.set_password('test')
        self.user.save()
        self.client.login(username='test', password='test')

    def test_admin_not_broken(self):
        response = self.client.get('/admin/')
        self.assertContains(response, '/admin/password_change/')
        self.assertNotContains(response, "You don't have permission to edit anything")

    def test_admin_auth_not_broken(self):
        response = self.client.get('/admin/auth/')
        self.assertEqual(response.status_code, 200, response)

    def test_admin_auth_user_not_broken(self):
        url = reverse('admin:auth_user_changelist')
        self.assertEqual(url, '/admin/auth/user/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, response)

    def test_admin_1_root(self):
        url = reverse('admin:test_app_test1_changelist')
        self.assertEqual(url, '/admin/test_app/test1/')
        self.assertRedirects(self.client.get(url.rstrip('/')), url, 301)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, response)
        self.assertEqual(response.content, b"root", response)

    def test_admin_1_level1(self):
        url = reverse('admin:level-1')
        self.assertEqual(url, '/admin/test_app/test1/level1/')
        self.assertRedirects(self.client.get(url.rstrip('/')), url, 301)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, response)
        self.assertEqual(response.content, b"level1", response)

    def test_admin_1_level1_level2(self):
        url = reverse('admin:level-2')
        self.assertEqual(url, '/admin/test_app/test1/level1/level2/')
        self.assertRedirects(self.client.get(url.rstrip('/')), url, 301)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, response)
        self.assertEqual(response.content, b"level2", response)

    def test_admin_2_root(self):
        url = reverse('admin:test_app_test2_changelist')
        self.assertEqual(url, '/admin/test_app/test2/')
        self.assertRedirects(self.client.get(url.rstrip('/')), url, 301)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, response)
        self.assertEqual(response.content, b"root", response)

    def test_runtime_error(self):
        from .admin import make_admin_class, patterns, url
        from admin_utils.mock import InvalidAdmin
        self.assertRaises(
            InvalidAdmin,
            make_admin_class, "Test", patterns("test_app.views",
                url(r'^$', 'root', name='whatever'),
            ), "test_app"
        )
