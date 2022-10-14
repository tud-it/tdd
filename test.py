"""test API"""


import os
from unittest import TestCase, skip
from unittest.mock import call, mock_open, patch

from server import (Person, db_persons_change_name, get_persons,
                    simulate_db_persons, use_foo)


class TestGetPersons(TestCase):
    """test get_persons"""

    def test_get_all_persons(self) -> None:
        """get all persons"""

        expected = [
            Person(name="P1", age=1),
            Person(name="P2", age=2),
        ]
        with patch("server.simulate_db_persons") as mock:
            mock.return_value = expected

            got = get_persons()
            self.assertListEqual(expected, got)


class TestSimulateDBPersons(TestCase):
    """test simulate_db_persons"""

    def tearDown(self) -> None:
        if os.path.isfile("_mock_db"):
            os.remove("_mock_db")

    def test_read_persons_unit(self) -> None:
        """read from file, with a mock open implementation"""
        mock_data = "P1, 1\nP2, 2"
        with patch("builtins.open", mock_open(read_data=mock_data)) as mock:
            self.assertListEqual(
                [
                    Person(name="P1", age=1),
                    Person(name="P2", age=2),
                ],
                simulate_db_persons(),
            )
            mock.assert_called_with("person_db", encoding="utf-8")

    def test_ignore_non_splittable_lines(self) -> None:
        """read from file, with a mock open implementation"""
        mock_data = "P1, 1\n\nP2, 2"
        with patch("builtins.open", mock_open(read_data=mock_data)) as mock:
            self.assertListEqual(
                [
                    Person(name="P1", age=1),
                    Person(name="P2", age=2),
                ],
                simulate_db_persons(),
            )
            mock.assert_called_with("person_db", encoding="utf-8")

    def test_ignore_lines_additional_data_in_lines(self) -> None:
        """read from file, with a mock open implementation"""
        mock_data = "P1, 1\nP2, 2, 3\n"
        with patch("builtins.open", mock_open(read_data=mock_data)) as mock:
            self.assertListEqual(
                [
                    Person(name="P1", age=1),
                    Person(name="P2", age=2),
                ],
                simulate_db_persons(),
            )
            mock.assert_called_with("person_db", encoding="utf-8")

    def test_read_person_integration_name_injections(self) -> None:
        """test read from file, by using a mock file"""

        with open("_mock_db", "w", encoding="utf-8") as mock:
            mock.write("P1, 1\nP2, 2")

        with patch("server.DB_PATH", "_mock_db"):
            self.assertListEqual(
                [
                    Person(name="P1", age=1),
                    Person(name="P2", age=2),
                ],
                simulate_db_persons(),
            )

    def test_file_exists(self) -> None:
        """test that production file exists"""

        self.assertTrue(os.path.isfile("personen_db"))


class TestDBPersonsChangeName(TestCase):
    """test db_persons_change_name"""

    def tearDown(self) -> None:
        if os.path.isfile("_mock_persons_db"):
            os.remove("_mock_persons_db")

    def test_change_name(self) -> None:
        """test that name has changed"""
        mock_data = "Harry, 42\n"

        with patch("builtins.open", mock_open(read_data=mock_data)) as mock:
            db_persons_change_name("Harry", "Potter")
            mock_file = mock()
            mock_file.writelines.assert_called_once_with(["Potter, 42\n"])

    @skip("test broken")
    def test_use_utf_8(self) -> None:
        """opens with utf-8"""
        mock_data = "Harry, 42\n"

        with patch("builtins.open", mock_open(read_data=mock_data)) as mock:
            db_persons_change_name("Harry", "Potter")
            mock.assert_has_calls(
                [
                    call("person_db", encoding="utf-8"),
                    call("person_db", "w", encoding="utf-8"),
                ]
            )

    def test_change_name_with_tmp_file(self) -> None:
        """some dockstring"""
        mock_data = ["Harry, 42\n"]

        with open("_mock_persons_db", "w", encoding="utf-8") as file:
            file.writelines(mock_data)

        with patch("server.DB_PATH", "_mock_persons_db"):
            db_persons_change_name("Harry", "Potter")

        with open("_mock_persons_db", encoding="utf-8") as file:
            self.assertEqual(["Potter, 42\n"], file.readlines())

    def test_correct_change_name(self) -> None:
        """test that name has changed"""
        mock_data = "Harryyyy, 42\nHarry, 42\nHHaaaaarry, 42\n"

        with patch("builtins.open", mock_open(read_data=mock_data)) as mock:
            db_persons_change_name("Harry", "Potter")
            mock_file = mock()
            mock_file.writelines.assert_called_once_with(
                [
                    "Harryyyy, 42\n",
                    "Potter, 42\n",
                    "HHaaaaarry, 42\n",
                ]
            )


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
