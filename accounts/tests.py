from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
# tests everything works properly 
class CustomUserTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.normal_user = get_user_model().objects.create_user(
            username="user", email="user@email.com", password="testing321",
        )
        cls.admin_user = get_user_model().objects.create_superuser(
            username="admin", email="admin@email.com", password="testing321",
        )
    
    def test_create_user(self):
        self.assertEqual(self.normal_user.username, "user")
        self.assertEqual(self.normal_user.email, "user@email.com")
        self.assertTrue(self.normal_user.is_active)
        self.assertFalse(self.normal_user.is_staff)
        self.assertFalse(self.normal_user.is_superuser)

    def test_create_superuser(self):
        self.assertEqual(self.admin_user.username, "admin")
        self.assertEqual(self.admin_user.email, "admin@email.com")
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_superuser)

class SignupPageTests(TestCase):
    username = "newuser"
    email = "newuser@email.com"
    phone = "01234567890"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "I should not be here")
    
    def test_signup_form(self):
        newuser = get_user_model().objects.create_user(self.username, self.email, self.phone)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
    