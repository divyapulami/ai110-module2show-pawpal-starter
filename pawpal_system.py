from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
    task_id: int
    title: str
    description: str
    due_date: str
    time: str
    frequency: str
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def update_task(
        self,
        title: Optional[str] = None,
        description: Optional[str] = None,
        due_date: Optional[str] = None,
        time: Optional[str] = None,
        frequency: Optional[str] = None,
        completed: Optional[bool] = None,
    ) -> None:
        """Update task properties with non-None values."""
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if due_date is not None:
            self.due_date = due_date
        if time is not None:
            self.time = time
        if frequency is not None:
            self.frequency = frequency
        if completed is not None:
            self.completed = completed


@dataclass
class Pet:
    pet_id: int
    name: str
    species: str
    breed: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to the pet's task list."""
        existing = [t for t in self.tasks if t.task_id == task.task_id]
        if existing:
            return
        self.tasks.append(task)

    def remove_task(self, task_id: int) -> None:
        """Remove a task by ID from the pet's tasks."""
        self.tasks = [t for t in self.tasks if t.task_id != task_id]

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return list(self.tasks)


class Owner:
    def __init__(self, owner_id: int, name: str) -> None:
        self.owner_id = owner_id
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet if not already owned."""
        existing = [p for p in self.pets if p.pet_id == pet.pet_id]
        if existing:
            return
        self.pets.append(pet)

    def remove_pet(self, pet_id: int) -> None:
        """Remove a pet by ID."""
        self.pets = [p for p in self.pets if p.pet_id != pet_id]

    def get_pets(self) -> List[Pet]:
        """Return all pets for this owner."""
        return list(self.pets)

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks across all owned pets."""
        all_tasks: List[Task] = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    def __init__(self) -> None:
        self.tasks: List[Task] = []

    def add_task(self, task: Task, pet: Optional[Pet] = None) -> None:
        """Add a task globally and optionally assign it to a pet."""
        if not any(t.task_id == task.task_id for t in self.tasks):
            self.tasks.append(task)

        if pet is not None:
            pet.add_task(task)

    def remove_task(self, task_id: int, pet: Optional[Pet] = None) -> None:
        """Remove a task globally and optionally from a pet."""
        self.tasks = [t for t in self.tasks if t.task_id != task_id]
        if pet is not None:
            pet.remove_task(task_id)

    def get_tasks_for_today(self, date: str) -> List[Task]:
        """Return tasks with the matching due_date."""
        return [t for t in self.tasks if t.due_date == date]

    def get_tasks_for_pet(self, pet: Pet) -> List[Task]:
        """Return the given pet's tasks as known by its own record."""
        return pet.get_tasks()

    def get_pending_tasks(self) -> List[Task]:
        """Return tasks that are not completed."""
        return [t for t in self.tasks if not t.completed]

    def get_completed_tasks(self) -> List[Task]:
        """Return tasks that are completed."""
        return [t for t in self.tasks if t.completed]
