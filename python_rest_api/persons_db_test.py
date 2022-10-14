import os
from unittest import TestCase
from unittest.mock import mock_open, patch

from genericpath import isfile

import persons_db


class TestPersons(TestCase):
    def test_get_persons(self) -> None:
        """Attempts to get all persons."""

        expected = [
            persons_db.Person(name="Foo", age=12),
            persons_db.Person(name="Bar", age=34),
        ]

        with patch("persons_db.simulate_db_persons") as mock:
            mock.return_value = expected

            got = persons_db.get_persons()
            self.assertListEqual(expected, got)

    def test_serialize_person(self) -> None:
        person_foo = persons_db.Person(name="Foo", age=12)
        person_bar = persons_db.Person(name="Bar", age=34)
        person_baz = persons_db.Person(name="Baz", age=56)

        self.assertEqual(persons_db.serialize_person(person_foo), "Foo,12")
        self.assertEqual(persons_db.serialize_person(person_bar), "Bar,34")
        self.assertEqual(persons_db.serialize_person(person_baz), "Baz,56")

    def test_add_person(self) -> None:
        """Attempts to add a person."""

        person_to_add = persons_db.Person(name="Qux", age=78)
        test_db = "Foo,12\nBar,34\nBaz,56\n"

        with patch("builtins.open", mock_open(read_data=test_db)) as mock:
            persons_db.add_person(person_to_add)

            mock_file = mock()
            mock_file.write.assert_called_once_with("Qux,78")

            # got = persons_db.get_persons()

            # self.assertEqual(got[-1], person_to_add)
