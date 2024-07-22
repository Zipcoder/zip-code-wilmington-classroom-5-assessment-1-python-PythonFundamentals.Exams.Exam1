
import unittest
from exam1 import cases


class CasesTest(unittest.TestCase):

    def test_camel_to_snake(self):
        test_cases = [
            ('python', 'python'),
            ('zipCode', 'zip_code'),
            ('desaBurton', 'desa_burton'),
            ('dataEngineeringWithPython', 'data_engineering_with_python'),
        ]

        for word, expected in test_cases:
            with self.subTest(f"{word} -> {expected}"):
                self.assertEqual(expected, cases.camel2snake(word))


    def test_snake_to_camel(self):
        test_cases = [
            ('zz', 'zz'),
            ('python', 'python'),
            ('zip_code', 'zipCode'),
            ('wilmington_delaware', 'wilmingtonDelaware'),
            ('holy_smokes', 'holySmokes'),
            ('this_is_silly', 'thisIsSilly'),
        ]

        for word, expected in test_cases:
            with self.subTest(f"{word} -> {expected}"):
                self.assertEqual(expected, cases.snake2camel(word))

