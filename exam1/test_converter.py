import unittest
from exam1 import converter


class ConverterTest(unittest.TestCase):

    def test_meters_to_feet(self):
        test_cases = [
            (1, 3.28),
            (5, 16.40),
            (10, 32.81),
            (100, 328.08),
            (0.91, 2.99),
        ]

        for meter_in, expected in test_cases:
            with self.subTest(f"{meter_in} -> {expected}"):
                self.assertEqual(expected, converter.meters_to_feet(meter_in))

    def test_feet_to_meters(self):
        test_cases = [
            (1, .30),
            (33, 10.06),
            (125, 38.10)
        ]

        for feet_in, expected in test_cases:
            with self.subTest(f"{feet_in} -> {expected}"):
                self.assertEqual(expected, converter.feet_to_meters(feet_in))

    def test_kilometer_to_miles(self):
        test_cases = [
            (1, 0.62),
            (5, 3.11),
            (10, 6.21),
            (42, 26.1)
        ]

        for kilometer_in, expected in test_cases:
            with self.subTest(f"{kilometer_in} -> {expected}"):
                self.assertEqual(expected, converter.kilometer_to_miles(kilometer_in))

    def test_miles_to_kilometers(self):
        test_cases = [
            (1, 1.61),
            (3, 4.83),
            (26.2, 42.16),
            (55, 88.51),
        ]

        for mile_in, expected in test_cases:
            with self.subTest(f"{mile_in} -> {expected}"):
                self.assertEqual(expected, converter.miles_to_kilometers(mile_in))
