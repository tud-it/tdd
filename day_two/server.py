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
