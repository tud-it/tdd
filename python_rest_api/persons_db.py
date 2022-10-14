"""Python database."""

from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int


DB_PATH = "persons.db"


def simulate_db_persons() -> list[Person]:
    with open(DB_PATH, encoding="utf-8") as db_file:
        return [
            Person(name=name, age=int(age))
            for name, age in [line.split(",") for line in db_file]
        ]


def get_persons() -> list[Person]:
    return simulate_db_persons()


def serialize_person(person: Person) -> str:
    return f"{person.name},{person.age}"


def add_person(to_add: Person) -> None:
    with open(DB_PATH, "w", encoding="utf-8") as db_file:
        db_file.write(serialize_person(to_add))
