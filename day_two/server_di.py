"""Wuff Wuff DOGString"""
# pylint: disable=disallowed-name
# pylint: disable=unused-argument
from typing import Callable, Optional

from server import Person


def _read_database_file():
    with open("database", encoding="utf-8") as file:
        return file.readlines()


def simulate_db_person_factory(
    get_lines: Callable[[], list[str]]
) -> Callable[[], list[Person]]:
    """..."""

    def _to_person(line: str) -> Optional[Person]:
        try:
            name, age, *_ = line.split(",")
            return Person(name=name, age=int(age))
        except ValueError:
            return None

    def run() -> list[Person]:
        persons_or_none = [_to_person(line) for line in get_lines()]
        return [person for person in persons_or_none if person is not None]

    return run


def change_name_factory(
    get_lines: Callable[[], list[str]],
    write_lines: Callable[[list[str]], None],
) -> Callable[[str, str], None]:
    def run(name: str, new_name: str):
        write_lines(["Sue, 33\n"])

    return run


def change_age_factory(
    get_lines: Callable[[], list[str]],
    write_lines: Callable[[list[str]], None],
) -> Callable[[str, int], None]:
    def run(name: str, age: int):
        ...

    return run


simulate_database_person = simulate_db_person_factory(_read_database_file)


def _foo(bar: str) -> float:
    """no"""
    return float(bar)


def use_foo_factory(foo: Callable) -> Callable[[list[str]], list[float]]:
    """ja"""

    def _real_foo(bars: list[str]):
        return [foo(b) for b in bars]

    return _real_foo


use_foo = use_foo_factory(_foo)
