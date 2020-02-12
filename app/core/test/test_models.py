from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_email(self):
        email = "abc.com"
        password = "pass123"
        print(get_user_model())
        user = get_user_model().obj.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalize_email(self):
        email = 'test@abc.com'
        user = get_user_model().obj.create_user(email, 'pass123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().obj.create_user(None, 'pass123')

    def test_create_new_superuser(self):
        user = get_user_model().obj.create_superuser(
            'admin',
            'admin123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)