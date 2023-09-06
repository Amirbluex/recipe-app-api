"""
Calc TestSamples
"""
from django.test import SimpleTestCase

from app import calc

class ClacTest(SimpleTestCase):
    """ Test the clac module. """
    def test_add_number(self):
        """ Test adding numbers togeather. """
        res = calc.add(5, 6)

        self.assertEqual(res, 11)