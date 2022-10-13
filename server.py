"""Awesome REST server"""
from fastapi import FastAPI
from pydantic import BaseModel  # pylint: disable=no-name-in-module

app = FastAPI()

# pylint: disable=too-few-public-methods
class Person(BaseModel):
    """a person"""

    name: str
    age: int


DB_PATH = "person_db"


def _can_split(value: str) -> bool:
    return "," in value


def _to_person(value: str) -> Person:
    name, age, *_ = value.split(",")
    return Person(name=name, age=float(age))


# simulates Database
def simulate_db_persons() -> list[Person]:
    """simulate persosn"""
    with open(DB_PATH, encoding="utf-8") as file:
        return [_to_person(line) for line in file if _can_split(line)]


def get_persons() -> list[Person]:
    """get all persons"""
    return simulate_db_persons()
