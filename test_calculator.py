import contextlib
import io
import unittest
from unittest.mock import patch

import calc
import tools
from p2_digits import count_digits
from digit_sum_rec import digit_sum_rec
from main import main


class FunctionTests(unittest.TestCase):
    def test_arithmetic(self):
        cases = [(calc.add, (2, 3), 5), (calc.add, (-2, 2), 0),
                 (calc.sub, (3, 5), -2), (calc.mul, (-3, 4), -12),
                 (calc.mul, (0, 9), 0), (calc.div, (7, 2), 3.5),
                 (calc.div, (5, 0), None), (calc.div, (0, 5), 0.0)]
        for fn, args, expected in cases:
            with self.subTest(function=fn.__name__, args=args):
                self.assertEqual(fn(*args), expected)

    def test_power(self):
        for args, expected in [((5,), 25), ((2, 10), 1024), ((-2, 3), -8),
                               ((2, -2), 0.25), ((2, 0), 1),
                               ((0, -1), None), ((-4, 0.5), None)]:
            with self.subTest(args=args):
                self.assertEqual(calc.power(*args), expected)

    def test_percent(self):
        for args, expected in [((200, 15), 30), ((80, 0), 0),
                               ((80, 100), 80), ((200, 12.5), 25)]:
            with self.subTest(args=args):
                self.assertEqual(calc.percent(*args), expected)

    def test_tools(self):
        for n, expected in [(0, True), (-4, True), (7, False)]:
            with self.subTest(n=n):
                self.assertEqual(tools.is_even(n), expected)
        self.assertEqual(tools.max3(-5, -2, -9), -2)
        self.assertEqual(tools.max3(8, 8, 3), 8)

    def test_digits(self):
        for n, expected in [(50525, 5), (7, 1), (1000, 4), (0, 1)]:
            with self.subTest(n=n):
                self.assertEqual(count_digits(n), expected)
        with self.assertRaises(ValueError):
            count_digits(-1)

    def test_recursive_sum(self):
        for n, expected in [(50525, 17), (0, 0), (7, 7), (1000, 1), (-305, 8)]:
            with self.subTest(n=n):
                self.assertEqual(digit_sum_rec(n), expected)

    def test_menu(self):
        cases = [
            (["1", "2", "3", "0"], "Результат: 5.0"),
            (["2", "3", "5", "0"], "Результат: -2.0"),
            (["3", "-3", "4", "0"], "Результат: -12.0"),
            (["4", "7", "2", "0"], "Результат: 3.5"),
            (["4", "7", "0", "0"], "Дію не визначено"),
            (["5", "2", "10", "0"], "Результат: 1024.0"),
            (["6", "200", "15", "0"], "Результат: 30.0"),
            (["7", "4", "0"], "Парне"),
            (["8", "-5", "-2", "-9", "0"], "Результат: -2.0"),
            (["9", "0"], "Невідома дія"),
            (["1", "abc", "0"], "Помилка: введіть число"),
            (["7", "2.5", "0"], "Помилка: введіть ціле число"),
        ]
        for entries, expected in cases:
            with self.subTest(entries=entries):
                output = io.StringIO()
                with patch("builtins.input", side_effect=entries) as mocked:
                    with contextlib.redirect_stdout(output):
                        main()
                self.assertIn(expected, output.getvalue())
                self.assertIn("Роботу завершено", output.getvalue())
                self.assertEqual(mocked.call_count, len(entries))


if __name__ == "__main__":
    unittest.main(verbosity=2)
