from django.test import TestCase, Client
from django.urls import reverse


class BasicTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_login_page_loads(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_redirect_admin(self):
        response = self.client.get(reverse("redirect-admin"))
        self.assertEqual(response.status_code, 302)

    def test_home_page_redirects(self):
  
        response = self.client.get(reverse("home-page"))
        self.assertIn(response.status_code, [200, 302])

    def test_test_page_loads(self):
        response = self.client.get(reverse("test-page"))
        self.assertIn(response.status_code, [200, 302])  # safe for both
