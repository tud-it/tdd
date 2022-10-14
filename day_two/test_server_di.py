"""testing"""
# pylint: disable=disallowed-name
from unittest import TestCase
from unittest.mock import Mock, call

from server_di import use_foo_factory


class TestUseFoo(TestCase):
    """nö"""

    def test_converts(self) -> None:
        """ldsjf!!!?"""

        def mock_foo(bar: str) -> float:
            return 42

        use_foo = use_foo_factory(mock_foo)
        self.assertEqual([42, 42], use_foo(["", ""]))

    def test_converts_corrects_bar(self) -> None:
        """dhfskhsda7856757,.-,.#+,.-ß,.-"""

        def mock_foo(value: str) -> float:
            return float(value)

        use_foo = use_foo_factory(mock_foo)
        self.assertEqual([4, 2], use_foo([4, 2]))
