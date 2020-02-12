from typing import Dict

from django.test import TestCase
from django.contrib.auth import get_user_model

from django.urls import reverse

from rest_framework.test import APIClient

from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')


def create_user(**param):
    return get_user_model().obj.create_user(**param)


class PublicUserApiTest(TestCase):
    """test the user api public"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """test create user"""
        payload = {
            'email': 'admin@gmail.com',
            'password': 'admin123',
            'name': 'Test name'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().obj.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exist(self):
        payload = {'email': 'admin@gmail.com', 'password': 'admin123'}
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        payload = {'email': 'admin@gmail.com', 'password': 'admin123'}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exist = get_user_model().obj.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exist)

    def test_create_token_for_user(self):
        payload = {'email': 'admin@gmail.com', 'password': 'admin123'}
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        create_user(email='admin@gmail.com', password='admin123')
        payload = {'email': 'admin@gmail.com', 'password': 'wrong'}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        payload = {'email': 'admin@gmail.com', 'password': 'admin123'}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_filed(self):
        res = self.client.post(TOKEN_URL, {'email': 'one', 'password': ''})
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
