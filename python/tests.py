"""Contains unit tests."""

from argparse import ArgumentError
from email import message
from unittest import TestCase

import utils


class TestGiveMeTheBestNumber(TestCase):
    """Tests give_me_the_best_number."""

    def test_best_number(self) -> None:
        """Tests the best number."""

        self.assertEqual(utils.BEST_NUMBER, utils.give_me_the_best_number())


class TestFibonacci(TestCase):
    """Tests Fibonacci sequence returned by utils.fibonacci."""

    def test_first_is_one(self) -> None:
        """Tests first number."""

        self.assertEqual((1,), utils.fibonacci(1))

    def test_first_two_are_one(self) -> None:
        """Tests first two numbers."""

        self.assertEqual((1, 1), utils.fibonacci(2))

    def test_first_three(self) -> None:
        """Tests first three numbers."""

        self.assertEqual((1, 1, 2), utils.fibonacci(3))

    def test_first_ten(self) -> None:
        """Tests first ten numbers."""

        self.assertEqual(
            (1, 1, 2, 3, 5, 8, 13, 21, 34, 55), utils.fibonacci(10)
        )

    def test_raises_with_negative_count(self) -> None:
        """Raises ArgumentError when count is negative."""

        with self.assertRaises(ValueError) as ve:
            _ = utils.fibonacci(-1)

        self.assertEqual(utils.NEED_NON_NEG_NUM, str(ve.exception))
