"""test server_di"""


from unittest import TestCase
from unittest.mock import Mock, call

from server import Person
from server_di import (
    change_name_factory,
    simulate_db_person_factory,
    use_foo_factory,
)


class TestSimulateDBPersonFactory(TestCase):
    """test simulate_db_person_factory"""

    def test_get_only_person(self) -> None:
        """..."""

        def get_lines() -> list[str]:
            return ["Marry, 25\n"]

        get_persons = simulate_db_person_factory(get_lines)
        self.assertListEqual(
            [Person(name="Marry", age=25)],
            get_persons(),
        )

    def test_ignore_too_few_item_lines_persons(self) -> None:
        """..."""

        def get_lines() -> list[str]:
            return [
                "Marry, 25\n",
                "Harry\n",
                "Sebastian, 77\n",
            ]

        get_persons = simulate_db_person_factory(get_lines)
        self.assertListEqual(
            [
                Person(name="Marry", age=25),
                Person(name="Sebastian", age=77),
            ],
            get_persons(),
        )

    def test_ignore_additional_line_items_persons(self) -> None:
        """..."""

        def get_lines() -> list[str]:
            return [
                "Marry, 25\n",
                "Harry, 55\n",
                "Sebastian, 77, 66\n",
            ]

        get_persons = simulate_db_person_factory(get_lines)
        self.assertListEqual(
            [
                Person(name="Marry", age=25),
                Person(name="Harry", age=55),
                Person(name="Sebastian", age=77),
            ],
            get_persons(),
        )

    def test_ignore_invalid_age(self) -> None:
        """..."""

        def get_lines() -> list[str]:
            return [
                "Marry, zz\n",
                "Harry, 55\n",
                "Sebastian, 77, 66\n",
            ]

        get_persons = simulate_db_person_factory(get_lines)
        self.assertListEqual(
            [
                Person(name="Harry", age=55),
                Person(name="Sebastian", age=77),
            ],
            get_persons(),
        )

    def test_get_some_persons(self) -> None:
        """..."""

        def get_lines() -> list[str]:
            return [
                "Marry, 25\n",
                "Harry, 105\n",
                "Sebastian, 77\n",
            ]

        get_persons = simulate_db_person_factory(get_lines)
        self.assertListEqual(
            [
                Person(name="Marry", age=25),
                Person(name="Harry", age=105),
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

    def test_change_name_with_mock(self) -> None:
        """..."""

        def get_lines() -> list[str]:
            return ["Marry, 33\n"]

        write_lines = Mock()

        change_name = change_name_factory(get_lines, write_lines)
        change_name("Marry", "Sue")

        write_lines.assert_called_once_with(["Sue, 33\n"])


class TestUseFoo(TestCase):
    """test use_foo"""

    def test_converts(self) -> None:
        """..."""

        def mock_foo(_: str) -> float:
            return 42

        use_foo = use_foo_factory(mock_foo)
        self.assertEqual([42, 42], use_foo(["", ""]))

    def test_use_correct_item_bar(self) -> None:
        """..."""

        def mock_foo(value: str) -> float:
            return float(value)

        use_foo = use_foo_factory(mock_foo)
        self.assertEqual([4, 2], use_foo(["4", "2"]))

    def test_use_correct_item_via_list(self) -> None:
        """..."""
        calls: list[str] = []

        def mock_foo(value: str) -> float:
            calls.append(value)
            return 42

        use_foo = use_foo_factory(mock_foo)
        _ = use_foo(["4", "2"])
        self.assertEqual(["4", "2"], calls)

    def test_use_correct_item_via_mock(self) -> None:
        """..."""

        mock_foo = Mock(return_value=42)

        use_foo = use_foo_factory(mock_foo)
        _ = use_foo(["4", "2"])
        mock_foo.assert_has_calls([call("4"), call("2")])
