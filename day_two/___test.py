"""Testing server.py"""
import os
from unittest import TestCase, skip
from unittest.mock import mock_open, patch

from server import (
    Person,
    _can_split,
    _to_person,
    add_person,
    db_persons_change_name,
    get_person,
    simulate_db_persons,
    use_foo,
)


class TestServerFunctions(TestCase):

    """testing something"""

    def test_getting_the_person(self) -> None:
        """gets a person"""

        expected = [
            Person(name="P1", age=1),
            Person(name="P2", age=2),
        ]

        with patch("server.simulate_db_persons") as mock:
            mock.return_value = expected

            got = get_person()

            self.assertListEqual(
                expected,
                got,
            )


class TestSimulateDBPersons(TestCase):
    """Something"""

    def test_file_exists(self) -> None:
        """test that production file exists"""

        self.assertTrue(os.path.isfile("database"))

    def test_read_persons_db(self) -> None:
        """i dont want to write a docstring now"""

        persons = simulate_db_persons()
        persons_str: list[str] = []
        for person in persons:
            persons_str.append(f"{person.name}, {person.age}\n")
        with open("database", encoding="utf-8") as file:
            self.assertListEqual(list(file), persons_str)

    def test_add_person(self) -> None:
        """SSS"""

        temp = Person(name="Peter", age=18)

        self.assertEqual(len(simulate_db_persons()) + 1, len(add_person(temp)))

    @skip
    def test_person_name_changed(self) -> None:
        """test if name has changed"""
        mock_data = "Harry, 42\n"

        with patch("builtins.open", mock_open(read_data=mock_data)) as mock:
            db_persons_change_name("Harry", "Potter")
            mock_file = mock()
            mock_file.writelines.assert_called_once_with(["Potter, 42\n"])

    # @skip
    def test_something(self) -> None:
        mock_data = ["Harry, 42\n"]

        with open("_mock_persons_db", "w", encoding="utf-8") as file:
            file.writelines(mock_data)

        with patch("server.DB_PATH", "_mock_persons_db"):
            db_persons_change_name("Harry", "Potter")

        with open("_mock_persons_db", encoding="utf-8") as file:
            self.assertEqual(["Potter, 42\n"], file.readlines())


class TestUseFoo(TestCase):
    """test use_foo"""

    def test_converts_to_float(self) -> None:
        """..."""

        with patch("server.foo") as mock:
            mock.return_value = 42
            result = use_foo(["", "", "", "", ""])
            self.assertListEqual([42, 42, 42, 42, 42], result)

    def test_converts_to_float_2(self) -> None:
        """..."""

        def mock_foo(bar: str) -> float:
            return 42

        with patch("server.foo", mock_foo):
            result = use_foo(["", "", "", "", ""])
            self.assertListEqual([42, 42, 42, 42, 42], result)
