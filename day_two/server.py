"""Awesome REST server"""
# pylint: disable=no-name-in-module
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


def db_persons_change_name(name, newname) -> list[Person]:
    """changes a persons name"""
    with open("database", "a", encoding="utf-8") as file:
        for line in file:
            if name in line:
                line.replace(name, newname)
    file.close()
    with open("database", encoding="utf-8") as file:
        return [_to_person(line) for line in file if _can_split(line)]
