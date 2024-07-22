import unittest
from exam1 import listies


class listiesTest(unittest.TestCase):

    def test_drop_last(self):
        test_cases = [
            ([1, 2, 3], [1,2]),
            ([1], []),
            (["foo", "bar"], ["foo"]),
        ]

        for tt_in, expected in test_cases:
            with self.subTest(f"{tt_in} -> {expected}"):
                self.assertEqual(expected, listies.drop_last(tt_in))

    def test_drop_first_two(self):
        test_cases = [
            ([1, 2, 3], [3]),
            ([1, 5], []),
            (["foo", "bar", "baz"], ["baz"]),
        ]

        for tt_in, expected in test_cases:
            with self.subTest(f"{tt_in} -> {expected}"):
                self.assertEqual(expected, listies.drop_first_two(tt_in))

    def test_drop_last_two(self):
        test_cases = [
            ([1, 2, 3], [1]),
            ([1, 5], []),
            (["foo", "bar", "baz"], ["foo"]),
        ]

        for tt_in, expected in test_cases:
            with self.subTest(f"{tt_in} -> {expected}"):
                self.assertEqual(expected, listies.drop_first_two(tt_in))


    def test_drop_mangle(self):
        test_cases = [
            ([1, 2, 3, 4], [3]),
            ([0, 1, 1], []),
            (["foo", "bar", "wow", "baz"], ["wow"]),
        ]

        for tt_in, expected in test_cases:
            with self.subTest(f"{tt_in} -> {expected}"):
                self.assertEqual(expected, listies.drop_mangle(tt_in))

    def test_add_item_front(self):
        test_cases = [
            ([1, 2, 3, 4], 3, [3, 1, 2, 3, 4]),
            ([0, 1, 1], 2, [2, 0, 1, 1]),
            (["foo", "bar", "wow", "baz"], "wow", ["wow", "foo", "bar", "wow", "baz"] ),
        ]

        for tt_in, aaa, expected in test_cases:
            with self.subTest(f"{tt_in} {aaa} -> {expected}"):
                self.assertEqual(expected, listies.add_item_front(tt_in, aaa))

    def test_add_item_end(self):
        test_cases = [
            ([1, 2, 3, 4], 3, [1, 2, 3, 4, 3]),
            ([0, 1, 1], 2, [0, 1, 1, 2]),
            (["foo", "bar", "wow", "baz"], "wow", ["foo", "bar", "wow", "baz", "wow"] ),
        ]

        for tt_in, aaa, expected in test_cases:
            with self.subTest(f"{tt_in} {aaa} -> {expected}"):
                self.assertEqual(expected, listies.add_item_end(tt_in, aaa))
