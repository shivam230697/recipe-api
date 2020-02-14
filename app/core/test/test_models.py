from django.test import TestCase
from django.contrib.auth import get_user_model
from app.core import models


def sample_user(email="admin@gmail.com", password="admin123"):
    return get_user_model().obj.create_user(email, password)


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

    def test_tag_str(self):
        """
        dd
        :return:
        """

        tag = models.Tag.objects.create(
            user=sample_user(),
            name="vegan"
        )
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """

        :return:
        """
        ingredients = models.Ingredient.objects.create(
            user = sample_user(),
            name= 'cucumber'
        )
        self.assertEqual(str(ingredients), ingredients.name)

    def Test_the_recipe_string_representation(self):
        recipe = models.REcipe.obkects.create(
            user=sample_user(),
            title= 'steak and mushroom souce',
            price='5.00'

        )
        self.assertEqual(str(recipe), recipe.title)