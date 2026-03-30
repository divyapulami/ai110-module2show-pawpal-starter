from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
    task_id: int
    title: str
    due_date: str
    task_type: str
    completed: bool = False

    def mark_complete(self) -> None:
        pass

    def update_task(
        self,
        title: Optional[str] = None,
        due_date: Optional[str] = None,
        task_type: Optional[str] = None,
        completed: Optional[bool] = None,
    ) -> None:
        pass


@dataclass
class Pet:
    pet_id: int
    name: str
    species: str
    breed: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task_id: int) -> None:
        pass

    def get_tasks(self) -> List[Task]:
        pass


class Owner:
    def __init__(self, owner_id: int, name: str) -> None:
        self.owner_id = owner_id
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet_id: int) -> None:
        pass

    def get_pets(self) -> List[Pet]:
        pass


class Scheduler:
    def __init__(self) -> None:
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task_id: int) -> None:
        pass

    def get_tasks_for_today(self, date: str) -> List[Task]:
        pass

    def get_tasks_for_pet(self, pet_id: int) -> List[Task]:
        pass