from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestAccountsApp(TestCase):
    def test_render_signup_page(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_render_signup_page_with_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        user = get_user_model().objects.create_user(
            'myusername',
            'myemail@gmail.com'
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, user.username)
        self.assertEqual(get_user_model().objects.all()[0].email, user.email)
