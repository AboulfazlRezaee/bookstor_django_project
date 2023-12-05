from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.

class SignupPageTests(TestCase):
    username = 'testuser',
    email = 'testuser@gmail.com',
    def test_signup_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    # def test_signup_page_content(self):
    #     response = self.client.get(reverse('signup'))
    #     self.assertContains(response, 'Sign Up')
    #     self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_page_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)