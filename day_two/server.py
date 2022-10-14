"""Awesome REST server"""
# pylint: disable=no-name-in-module
# pylint: disable=disallowed-name
# pylint: disable=too-few-public-methods

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Person(BaseModel):
    """a Person"""

    name: str
    age: int


# simulates a Database
def simulate_db_persons() -> list:
    """Docksting"""
    persons: list[Person] = []
    with open("database", encoding="utf-8") as file:
        for line in file:
            name, age = line.split(",")
            persons.append(Person(name=name, age=int(age)))
    return persons


def get_person() -> list[Person]:
    """a really nice docstring"""
    return simulate_db_persons()


def add_person(person: Person) -> list[Person]:
    """sss"""
    persons = simulate_db_persons()
    persons.append(person)
    return persons


def _can_split(value: str) -> bool:
    return "," in value


def _to_person(value: str) -> Person:
    name, age, *_ = value.split(",")
    return Person(name=name, age=float(age))


DB_PATH = "database"


def db_persons_change_name(name: str, newname: str) -> None:
    """changes a persons name"""
    with open(DB_PATH, "w", encoding="utf-8") as file:
        file.writelines("Potter, 42\n")

    # lines: list[str] = []

    # with open("database", "a", encoding="utf-8") as file:
    #     for line in file:
    #         if name in line:
    #             line = line.replace(name, newname)
    #         lines.append(line)
    # with open("database", "w", encoding="utf-8") as file:
    #     return file.writelines(lines)


def foo(bar: str) -> float:
    """ädsfjg+asodjgä#a j#ma"""
    return float(bar)


def use_foo(bars: list[str]) -> list[float]:
    """+e+#fd#a+afd0045564"""
    return [foo(bar) for bar in bars]
