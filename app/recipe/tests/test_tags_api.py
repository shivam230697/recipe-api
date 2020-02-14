from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


from app.core import models
from app.core.models import Tag
from app.recipe import TagSerializer

TAGS_URLS = reverse('recipe:tag-list')


class PublicTagsApiTests(TestCase):
    """

    """

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        res = self.client.get(TAGS_URLS)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagsApiTests(TestCase):
    """

    """

    def setUp(self):
        self.user = get_user_model().obj.create_user(
            'admin@gmail.com',
            'admin123'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        Tag.objects.create(user=self.user, name='Vegan')
        Tag.objects.create(user=self.user, name='Desert')
        res = self.client.get(TAGS_URLS)
        tags = Tag.objects.all().order_by('-name')
        serializer = TagSerializer(tags, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_tags_limited_to_user(self):
        """

        :return:
        """
        user2 =  get_user_model().objects.create_user(
            'admin@gail.com',
            'admin123'
        )
        tag = Tag.objects.create(user=self.user, name ='comfort food')
        res = self.client.get(TAGS_URLS)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual((len(res.data)), 1)
        self.assertEqual(res.data[0]['name'], tag.name)

    def _test_create_tag_successful(self):
        payload = {'name':'Test tga'}
        self.client.post(TAGS_URLS, payload)
        exists = Tag.objects.filter(
            user=self.user,
            name = payload['name']
        ).exists()
        self.assertTrue(exists)

    def test_create_tags_invalid(self):
        """

        :return:
        """
        payload = {'name': ''}
        res = self.client.post(TAGS_URLS, payload)

        self.assertSetEqual(res.status_code, status.HTTP_400_BAD_REQUEST)