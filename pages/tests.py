from django.test import TestCase
from django.urls import reverse


class TestPagesApp(TestCase):
    def test_home_page(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_with_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_show_home_page_in_website(self):
        response = self.client.get('/home/')
        self.assertContains(response, 'Home page')

    def test_show_home_page_in_website_with_name(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home page')

    def test_used_home_html_in_page(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
