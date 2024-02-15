# test_with_unittest.py
from unittest import TestCase
from button import *


class TryTesting(TestCase):
    def test_button(self):
        result = button()
        self.assertTrue(result)
