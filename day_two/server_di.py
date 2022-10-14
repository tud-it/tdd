"""server with dependency injection"""
# pylint: disable=disallowed-name

from typing import Any, Callable, Iterator, Optional, Protocol, TypeVar

from server import Person

Self = TypeVar("Self")


class PHandler(Protocol):
    """Handler protocol"""

    def __enter__(self: Self) -> Self:
        ...

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        ...

    def __iter__(self) -> Iterator[str]:
        ...

    def readlines(self) -> list[str]:
        """read lines"""

    def writelines(self, lines: list[str]) -> None:
        """write lines"""


def read_lines_factory(
    open_file: Callable[[str, str], PHandler]
) -> Callable[[], list[str]]:
    """..."""

    def run() -> list[str]:
        with open_file("person_db", "r") as file:
            return file.readlines()

    return run


def write_lines_factory(
    open_file: Callable[[str, str], PHandler]
) -> Callable[[list[str]], None]:
    """..."""

    def run(lines: list[str]) -> None:
        with open_file("person_db", "w") as file:
            file.writelines(lines)

    return run


def _read_from_db_file() -> list[str]:
    with open("person_db", encoding="utf-8") as file:
        return list(file)


def _write_to_db_file(lines: list[str]) -> None:
    with open("person_db", "w", encoding="utf-8") as file:
        file.writelines(lines)


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


# read_lines = read_lines_factory(open)
# write_lines = write_lines_factory(open)
# simulate_db_person = simulate_db_person_factory(read_lines)
# change_name = change_name_factory(read_lines, write_lines)
# change_age = change_name_factory(read_lines, write_lines)

simulate_db_person = simulate_db_person_factory(_read_from_db_file)
change_name = change_name_factory(_read_from_db_file, _write_to_db_file)
change_age = change_name_factory(_read_from_db_file, _write_to_db_file)


def _foo(bar: str) -> float:
    return float(bar) ** 10


def use_foo_factory(
    foo: Callable[[str], float]
) -> Callable[[list[str]], list[float]]:
    """..."""

    def _real_foo(bars: list[str]):
        return [foo(b) for b in bars]

    return _real_foo


use_foo = use_foo_factory(_foo)
