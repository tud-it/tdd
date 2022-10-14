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


def db_persons_change_name(name: str, new_name: str) -> None:
    """asdlaksd"""
    lines: list[str] = []
    with open(DB_PATH, encoding="utf-8") as file:
        for line in file:
            line_name, *_ = line.split(",")
            if line_name == name:
                line = line.replace(name, new_name)
            lines.append(line)
    with open(DB_PATH, "w", encoding="utf-8") as file:
        file.writelines(lines)


def get_persons() -> list[Person]:
    """get all persons"""
    return simulate_db_persons()


def foo(bar: str) -> float:
    return float(bar)


def use_foo(bars: list[str]) -> list[float]:
    return [foo(bar) for bar in bars]
