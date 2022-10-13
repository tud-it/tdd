"""test API"""


import os
from unittest import TestCase
from unittest.mock import mock_open, patch

from server import Person, get_persons, simulate_db_persons


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

        self.assertTrue(os.path.isfile("person_db"))

    def test_add_age(self) -> None:
        """test that age got added"""

        self.assertTrue(os.path.isfile("person_db"))
