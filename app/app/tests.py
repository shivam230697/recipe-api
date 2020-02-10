from django.test import TestCase
from .calc import add, sub


class CalcTests(TestCase):

    def test_add_numbers(self):
        """tetst that number are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """sdhvfh"""
        self.assertEqual(sub(5, 11), 6)
