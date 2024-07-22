import unittest
from exam1 import dictionaries


class DictionariesTest(unittest.TestCase):

    def test_delete_keys_from_dict(self):
        test_cases = [
            (['a', 'c'], {'a': 1, 'b': 2, 'c': 3, 'd': 4}, {'b': 2, 'd': 4}),
            (["name", "salary"], {"name": "Kelly", "age":25, "salary": 8000, "city": "New york" },
            {'age': 25, 'city': 'New york'}),
            ([0, 2], {0: 2, 1: 1, 2: 1}, {1: 1}),
            (["foo", "bar", "baz"], {'bar': 'foo', 'baz': 'wow', 'foo': 'wow', 'wow': 'bar'}, 
            {'wow': 'bar'}),
        ]

        for kkk, vvv, expected in test_cases:
            with self.subTest(f"{vvv} {kkk} -> {expected}"):
                self.assertEqual(expected, dictionaries.delete_keys_from_dict(vvv, kkk))

    def test_check_dict_for_key(self):
        test_cases = [
            ({'a': 1, 'b': 2, 'c': 3, 'd': 4}, 3, True),
            ({'a': 1, 'b': 2, 'c': 3, 'd': 4}, 5, False),
            ({"name": "Kelly", "age":25, "salary": 8000, "city": "New York" }, 8000, True),
            ({"name": "Kelly", "age":25, "salary": 8000, "city": "New York" }, "Megan", False),
            ({'bar': 'foo', 'baz': 'wow', 'foo': 'wow', 'wow': 'bar'}, "foo", True),
            ({'bar': 'foo', 'foo': 'wow', 'wow': 'bar'}, "baz", False),
        ]

        for ddd, kkk, expected in test_cases:
            with self.subTest(f"{ddd} {kkk} -> {expected}"):
                self.assertEqual(expected, dictionaries.check_dict_for_key(ddd, kkk))

    def test_get_key_of_min_value(self):
        test_cases = [
            ({'Physics': 82, 'Math': 65, 'History': 75}, 'Math'),
            ({'Oranges': 12, 'Apples': 7, 'Bananas': 4}, 'Bananas'),
            ({'Foo': 2, 'Bar': 6, 'Baz': 7}, 'Foo'),
        ]

        for ddd, expected in test_cases:
            with self.subTest(f"{ddd} -> {expected}"):
                self.assertEqual(expected, dictionaries.get_key_of_min_value(ddd))

    def test_get_key_of_max_value(self):
        test_cases = [
            ({'Physics': 82, 'Math': 65, 'History': 75}, "Physics"),
            ({'Oranges': 12, 'Apples': 7, 'Bananas': 4}, "Oranges"),
            ({'Foo': 2, 'Bar': 6, 'Baz': 7}, 'Baz'),
        ]

        for ddd, expected in test_cases:
            with self.subTest(f"{ddd} -> {expected}"):
                self.assertEqual(expected, dictionaries.get_key_of_max_value(ddd))

    def test_letterfreq(self):
        test_cases = [
            ('apple', {'a' : 1, 'p': 2, 'l' : 1, 'e': 1}),
            ('mississippi', {'m' : 1, 'p': 2, 's' : 4, 'i': 4}),
        ]

        for ddd, expected in test_cases:
            with self.subTest(f"{ddd} -> {expected}"):
                self.assertEqual(expected, dictionaries.letterfreq(ddd))