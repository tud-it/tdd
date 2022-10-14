"""testing"""
# pylint: disable=disallowed-name
# pylint: disable=unused-argument
from unittest import TestCase
from urllib.parse import non_hierarchical

from server_di import change_name_factory, simulate_db_person_factory, use_foo_factory
from server import Person


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
        self.assertEqual([4, 2], use_foo(["4", "2"]))

class TestSimulateDBPersonFactory(TestCase):
    """42"""

    def test_get_only_person(self) -> None:
        """42"""

        def get_lines() -> list[str]:
            return ["Marry, 19\n"]

        get_persons = simulate_db_person_factory(get_lines)
        self.assertEqual(
            [Person(name="Marry", age="19")],
            get_persons()
        )

    def test_ignore_error_lines(self) -> None:
        """42"""

        def get_lines() -> list[str]:
            return [
                "Marry, 25\n",
                "Harry, 55\n",
                "Sebastian, 177, 56\n"
            ]

        get_persons = simulate_db_person_factory(get_lines)
        self.assertEqual(
            [
                Person(name="Marry", age="25"),
                Person(name="Harry", age="55"),
                Person(name="Sebastian", age="77"),
            ],
            get_persons()
        )


class TestChangeNameFactory(TestCase):
    """..."""

    def test_change_name(self) -> None:
        """..."""


        written_lines: list[str] = []
        def get_lines() -> list[str]:
            return ["Marry, 33"]

        def write_lines(line: list[str]) -> None:
            nonlocal write_lines
            write_lines = lines

        change_name = change_name_factory(get_lines, write_lines)
        change_name("Marry", "Sue")

        self.assertListEqual(["Sue, 33\n"], written_lines)
