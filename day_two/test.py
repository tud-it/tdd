"""Testing server.py"""
from unittest import TestCase
from unittest.mock import patch

from server import Person, add_person, get_person, simulate_db_persons


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

    def test_is_same_person(self) -> None:
        """ss"""
        temp = Person(name="Peter", age=18)
        temp2 = add_person(temp)
        self.assertEqual(temp2[-1], temp)
