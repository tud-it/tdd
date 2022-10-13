"""test API"""


import os
from unittest import TestCase
from unittest.mock import mock_open, patch

from server import (DB_PATH, Person, _can_split, _to_person,
                    db_persons_change_name, get_persons, simulate_db_persons)


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
            mock.assert_called_with("personen_db", encoding="utf-8")

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
            mock.assert_called_with("personen_db", encoding="utf-8")

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
            mock.assert_called_with("personen_db", encoding="utf-8")

    def test_file_exists(self) -> None:
        """test that production file exists"""

        self.assertTrue(os.path.isfile("personen_db"))
    def test_person_name_changed(self)->None:
        """tests wheteher personns name was changed"""
        with open(DB_PATH, encoding="utf-8") as file:
            testliste= [_to_person(line) for line in file if _can_split(line)]
            self.assertListEqual([
               testliste,
                db_persons_change_name("Heinz","Gustav")
            ])



