"""server with dependency injection"""

from typing import Callable

from server import Person


def _read_database_file():
    with open("database", encoding="utf-8") as file:
        return file.readlines()


def _write_to_database_file(lines: list[str]) -> None:
    with open("database", "w", encoding="utf-8") as file:
        file.writelines(lines)


def simulate_database_factory(
    get_lines: Callable[[], list[str]]
) -> Callable[[], list[Person]]:
    """..."""

    def run() -> list[Person]:
        persons: list[Person] = []
        for line in get_lines():
            name, age, *_ = line.split(",")
            person = Person(name=name, age=age)
            persons.append(person)
        return persons

    return run


def change_name_factory(
    get_lines: Callable[[], list[str]],
    write_lines: Callable[[list[str]], None],
) -> Callable[[str, str], None]:
    def run(name: str, new_name: str):
        new_lines: list[str] = []
        old_lines = get_lines()
        for line in old_lines:
            if name in line:
                _, age = line.split(",")
                new_lines.append(f"{new_name},{age}")
            else:
                new_lines.append(line)
        write_lines(new_lines)

    return run


def change_age_factory(
    get_lines: Callable[[], list[str]],
    write_lines: Callable[[list[str]], None],
) -> Callable[[str, int], None]:
    def run(name: str, age: int):
        new_lines: list[str] = []
        old_lines = get_lines()
        for line in old_lines:
            if name in line:
                new_lines.append(f"{name}, {age}\n")
            else:
                new_lines.append(line)
        write_lines(new_lines)

    return run


# read_lines = read_lines_factory(open)
# write_lines = write_lines_factory(open)
# simulate_db_person = simulate_db_person_factory(read_lines)
# change_name = change_name_factory(read_lines, write_lines)
# change_age = change_name_factory(read_lines, write_lines)


simulate_database_person = simulate_database_factory(_read_database_file)
change_name = change_name_factory(_read_database_file, _write_to_database_file)
change_age = change_name_factory(_read_database_file, _write_to_database_file)


def _foo(bar: str) -> float:
    """..."""
    return float(bar) ** 10


TStrToFloat = Callable[[str], float]
TStrListToFloatListFn = Callable[[list[str]], list[float]]


def use_foo_factory(foo: TStrToFloat) -> TStrListToFloatListFn:
    """..."""

    def _real_foo(bars: list[str]):
        return [foo(b) for b in bars]

    return _real_foo


use_foo = use_foo_factory(_foo)
