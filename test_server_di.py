"""...."""
from unittest import TestCase

from server import Person
from server_di import (
    change_age_factory,
    change_name_factory,
    simulate_database_factory,
    use_foo_factory,
)


class TestUseFoo(TestCase):
    """test use_foo"""

    def test_converts(self) -> None:
        """..."""

        def mock_foo(bar: str) -> float:
            return 42

        use_foo = use_foo_factory(mock_foo)
        self.assertEqual([42, 42], use_foo(["", ""]))

    def test_with_content_in_bars(self) -> None:
        """test with content in bars"""

        def mock_foo(value: str) -> float:
            return float(value)

        use_foo = use_foo_factory(mock_foo)
        self.assertEqual([41, 42], use_foo(["41", "42"]))


class TestSimulateDatabase(TestCase):
    """..."""

    def test_get_only_person(self) -> None:
        """..."""

        def get_lines() -> list[str]:
            return ["Marry, 25\n"]

        get_persons = simulate_database_factory(get_lines)
        self.assertListEqual([Person(name="Marry", age=25)], get_persons())

    def test_get_some_persons(self) -> None:
        """..."""

        def get_lines() -> list[str]:
            return ["Marry, 25\n", "Harry, 43\n", "Sebastian, 77\n"]

        get_persons = simulate_database_factory(get_lines)
        self.assertListEqual(
            [
                Person(name="Marry", age=25),
                Person(name="Harry", age=43),
                Person(name="Sebastian", age=77),
            ],
            get_persons(),
        )


class TestChangeNameFactory(TestCase):

    """test change_name_factory"""

    def test_change_name(self) -> None:

        """..."""

        written_lines: list[str] = []

        def get_lines() -> list[str]:

            return ["Marry, 33\n"]

        def write_lines(lines: list[str]) -> None:

            nonlocal written_lines

            written_lines = lines

        change_name = change_name_factory(get_lines, write_lines)

        change_name("Marry", "Sue")

        self.assertListEqual(["Sue, 33\n"], written_lines)

    def test_change_second_name(self) -> None:

        """..."""

        written_lines: list[str] = []

        def get_lines() -> list[str]:

            return ["Harry, 33\n"]

        def write_lines(lines: list[str]) -> None:

            nonlocal written_lines

            written_lines = lines

        change_name = change_name_factory(get_lines, write_lines)

        change_name("Harry", "Potter")

        self.assertListEqual(["Potter, 33\n"], written_lines)

    def test_change_one_of_two_names(self) -> None:

        """..."""

        written_lines: list[str] = []

        def get_lines() -> list[str]:

            return ["Harry, 23\n", "Marry, 33\n"]

        def write_lines(lines: list[str]) -> None:

            nonlocal written_lines

            written_lines = lines

        change_name = change_name_factory(get_lines, write_lines)

        change_name("Harry", "Potter")

        self.assertListEqual(["Potter, 23\n", "Marry, 33\n"], written_lines)


class TestChangeAgeFactory(TestCase):

    """test change_age_factory"""

    def test_change_age(self) -> None:

        """..."""

        written_lines: list[str] = []

        def get_lines() -> list[str]:

            return ["Marry, 33\n"]

        def write_lines(lines: list[str]) -> None:

            nonlocal written_lines

            written_lines = lines

        change_age = change_age_factory(get_lines, write_lines)

        change_age("Marry", 95)

        self.assertListEqual(["Marry, 95\n"], written_lines)

    def test_change_other_age(self) -> None:

        """..."""

        written_lines: list[str] = []

        def get_lines() -> list[str]:

            return ["Edward, 24\n"]

        def write_lines(lines: list[str]) -> None:

            nonlocal written_lines

            written_lines = lines

        change_age = change_age_factory(get_lines, write_lines)

        change_age("Edward", 42)

        self.assertListEqual(["Edward, 42\n"], written_lines)

    def test_change_one_of_two_ages(self) -> None:

        """..."""

        written_lines: list[str] = []

        def get_lines() -> list[str]:

            return ["Edward, 24\n", "Fridolin, 69\n"]

        def write_lines(lines: list[str]) -> None:

            nonlocal written_lines

            written_lines = lines

        change_age = change_age_factory(get_lines, write_lines)

        change_age("Edward", 42)

        self.assertListEqual(["Edward, 42\n", "Fridolin, 69\n"], written_lines)
