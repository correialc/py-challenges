import unittest
from challenges.two_pointers.roman_decimal import roman_decimal_decode


class TestRomanDecimal(unittest.TestCase):

    def test_roman_decimal_decode(self):
        self.assertEqual(roman_decimal_decode('I'), 1)
        self.assertEqual(roman_decimal_decode('II'), 2)
        self.assertEqual(roman_decimal_decode('III'), 3)
        self.assertEqual(roman_decimal_decode('IV'), 4)
        self.assertEqual(roman_decimal_decode('V'), 5)
        self.assertEqual(roman_decimal_decode('VI'), 6)
        self.assertEqual(roman_decimal_decode('VII'), 7)
        self.assertEqual(roman_decimal_decode('VIII'), 8)
        self.assertEqual(roman_decimal_decode('IX'), 9)
        self.assertEqual(roman_decimal_decode('X'), 10)
        self.assertEqual(roman_decimal_decode('XXI'), 21)
        self.assertEqual(roman_decimal_decode('M'), 1000)
        self.assertEqual(roman_decimal_decode('MCMXC'), 1990)
        self.assertEqual(roman_decimal_decode('MMVIII'), 2008)
        self.assertEqual(roman_decimal_decode('MDCLXVI'), 1666)
