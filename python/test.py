"""Contains unit tests."""

from unittest import TestCase

from utils import BEST_NUMBER, give_me_the_best_number


class TestGiveMeTheBestNumber(TestCase):
    """Tests give_me_the_best_number."""

    def test_best_number(self) -> None:
        """Returns the best number."""

        self.assertEqual(BEST_NUMBER, give_me_the_best_number())
