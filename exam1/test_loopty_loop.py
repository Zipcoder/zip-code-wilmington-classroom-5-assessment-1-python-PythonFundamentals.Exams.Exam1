import unittest
from exam1 import loopty_loop


class LooptyLoopTest(unittest.TestCase):
    def test_generate_list(self):
        test_cases = [
            ((1, 5, 1), [1, 2, 3, 4]),
            ((15, 22, 2), [15, 17, 19, 21]),
        ]
        for data_in, data_out  in test_cases:
            with self.subTest(f"{data_in} -> {data_out}"):
                self.assertEqual(data_out, loopty_loop.generate_list(*data_in))

    def test_generate_list_with_strategy(self):
        test_cases = [
            ((1, 5, 1, lambda x: x**2), [1, 4, 9, 16]),
            ((5, 10, 1, lambda x: x+5), [10, 11, 12, 13, 14]),
            ((100, 0, -25, lambda x: x/5), [20, 15, 10, 5]),
            ((100, 50, -10, lambda x: x-10), [90, 80, 70, 60, 50]),
        ]
        for data_in, data_out in test_cases:
            with self.subTest(f"{data_in} -> {data_out}"):
                self.assertEqual(data_out, loopty_loop.generate_list_with_strategy(*data_in))

