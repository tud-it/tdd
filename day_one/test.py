"""utils test"""
from unittest import TestCase

from utils import (
    BEST_NUMBER,
    COUNT_WAS_NEGATIVE_ERROR,
    calculate,
    fibonacci,
    give_me_the_best_number,
)


class TestGiveMeTheBestNumber(TestCase):
    """test give_me_the_best_number"""

    def test_best_number(self) -> None:
        """return best number"""

        self.assertEqual(BEST_NUMBER, give_me_the_best_number())


class TestFibonacci(TestCase):
    """test fibonacci"""

    def test_first_is_one(self):
        """returns first"""

        self.assertEqual((1,), fibonacci(1))

    def test_first_two_are_one(self) -> None:
        """returns one"""

        self.assertEqual((1, 1), fibonacci(2))

    def test_first_three(self) -> None:
        """return (1, 1, 2)"""

        self.assertEqual((1, 1, 2), fibonacci(3))

    def test_first_four(self) -> None:
        """return (1, 1, 2)"""

        self.assertEqual((1, 1, 2, 3), fibonacci(4))

    def test_first_ten(self) -> None:
        """testing first 10 fibo's"""

        self.assertEqual((1, 1, 2, 3, 5, 8, 13, 21, 34, 55), fibonacci(10))

    def test_raises_with_negative_count(self) -> None:
        """raises ArgumentError, when negative number"""

        with self.assertRaises(ValueError) as ctx:
            _ = fibonacci(-1)

        self.assertEqual(COUNT_WAS_NEGATIVE_ERROR, str(ctx.exception))


class TestCalculate(TestCase):
    """test calculate"""

    def test_return_number(self) -> None:
        """return expression number"""

        self.assertEqual(42, calculate("42"))
        self.assertEqual(2, calculate("2"))

    def test_sum_two_numbers_no_spaces(self) -> None:
        """sum two one digit numbers, no spaces"""

        self.assertEqual(8, calculate("2+6"))

    def test_divisor_two_numbers_no_spaces(self) -> None:
        """sum two one digit numbers, no spaces"""

        self.assertEqual(4, calculate("6-2"))

    def test_multiplikator_two_numbers_no_spaces(self) -> None:
        """product two one digit numbers, no spaces"""

        self.assertEqual(12, calculate("6*2"))

    def test_divident_two_numbers_no_spaces(self) -> None:
        """divident two one digit numbers, no spaces"""

        self.assertEqual(3, calculate("6/2"))

    def test_sum_two_multiple_numbers_no_spaces(self) -> None:
        """sum two multi-digit numbers, with spaces"""

        self.assertEqual(73, calculate("12+61"))

    def test_divisor_two_multiple_numbers_no_spaces(self) -> None:
        """divisor two multi-digit numbers, with spaces"""

        self.assertEqual(49, calculate("61-12"))

    def test_multiplikator_two_multiple_numbers_no_spaces(self) -> None:
        """multiplikator two multi-digit numbers, with spaces"""

        self.assertEqual(732, calculate("12*61"))

    def test_divident_two_multiple_numbers_no_spaces(self) -> None:
        """divident two multi-digit numbers, with spaces"""

        self.assertEqual(6, calculate("60/10"))

    def test_more_then_two_sum(self) -> None:
        """more then two sum"""

        self.assertEqual(300, calculate("120+80+100"))

    def test_more_then_two_divisor(self) -> None:
        """more then two sum"""

        self.assertEqual(95, calculate("120-10-8-7"))

    def test_more_then_two_product(self) -> None:
        """more then two sum"""

        self.assertEqual(168, calculate("12*7*2*1"))

    def test_more_then_two_divident(self) -> None:
        """more then two sum"""

        self.assertEqual(0.3148148148148148, calculate("170/45/6/2"))

    def test_dot_before_dash(self) -> None:
        """calculate dot before dash"""

        self.assertEqual(8, calculate("4 + 2 * 2"))
        self.assertEqual(5, calculate("4 + 2 / 2"))

    def test_double_minus(self) -> None:
        """testing if there is a double minus"""

        self.assertEqual(25, calculate("25--5+5"))

    def test_plus_minus(self) -> None:
        """testing for number +- number"""

        self.assertEqual(40, calculate("30+-12-2"))
