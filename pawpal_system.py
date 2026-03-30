from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional, Tuple


@dataclass
class Task:
    task_id: int
    title: str
    description: str
    due_date: str  # format YYYY-MM-DD
    time: str      # format HH:MM
    frequency: str
    completed: bool = False

    def mark_complete(self) -> Tuple[bool, Optional["Task"]]:
        """Mark this task as completed and create next occurrence when recurring."""
        self.completed = True

        if self.frequency.lower() not in ("daily", "weekly"):
            return True, None

        try:
            base_date = datetime.strptime(self.due_date, "%Y-%m-%d")
        except ValueError:
            return True, None

        delta = timedelta(days=1 if self.frequency.lower() == "daily" else 7)
        next_date = base_date + delta
        next_task = Task(
            task_id=self.task_id + 1,
            title=self.title,
            description=self.description,
            due_date=next_date.strftime("%Y-%m-%d"),
            time=self.time,
            frequency=self.frequency,
            completed=False,
        )

        return True, next_task

    def update_task(
        self,
        title: Optional[str] = None,
        description: Optional[str] = None,
        time: Optional[str] = None,
        frequency: Optional[str] = None,
        completed: Optional[bool] = None,
    ) -> None:
        """Update task properties with non-None values."""
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
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

    def complete_task(self, task_id: int, pet: Optional[Pet] = None) -> Optional[Task]:
        """Mark task completed and optionally create the next recurring occurrence."""
        task = next((t for t in self.tasks if t.task_id == task_id), None)
        if task is None:
            return None

        _, next_task = task.mark_complete()

        if next_task is not None:
            self.add_task(next_task, pet=pet)
        return next_task

    def get_tasks_for_today(self, date: str) -> List[Task]:
        """Return tasks with the matching due_date."""
        return [t for t in self.tasks if t.due_date == date]

    def get_tasks_for_pet(self, pet: Pet) -> List[Task]:
        """Return the given pet's tasks as known by its own record."""
        return pet.get_tasks()

    def sort_by_time(self, tasks: Optional[List[Task]] = None) -> List[Task]:
        """Return tasks sorted by time (HH:MM) using a lambda key."""
        target_tasks = tasks if tasks is not None else self.tasks
        return sorted(target_tasks, key=lambda t: t.time)

    def get_pending_tasks(self) -> List[Task]:
        """Return tasks that are not completed."""
        return [t for t in self.tasks if not t.completed]

    def get_completed_tasks(self) -> List[Task]:
        """Return tasks that are completed."""
        return [t for t in self.tasks if t.completed]

    def filter_by_completion(self, completed: bool) -> List[Task]:
        """Filter tasks by completion status."""
        return [t for t in self.tasks if t.completed == completed]

    def detect_conflicts(self) -> List[str]:
        """Return warnings for tasks that share the same date and time."""
        clashes: dict[tuple[str, str], List[Task]] = {}
        for task in self.tasks:
            key = (task.due_date, task.time)
            clashes.setdefault(key, []).append(task)

        warnings: List[str] = []
        for (due_date, time), tasks in clashes.items():
            if len(tasks) > 1:
                titles = ", ".join([t.title for t in tasks])
                warnings.append(
                    f"Conflict on {due_date} {time}: {len(tasks)} tasks ({titles})"
                )

        return warnings

    def filter_by_pet_name(self, pet_name: str, owner: Optional[Owner] = None) -> List[Task]:
        """Filter tasks by the pet name using owner data."""
        if owner is None:
            return []
        matched_pets = [p for p in owner.get_pets() if p.name.lower() == pet_name.lower()]
        tasks = []
        for pet in matched_pets:
            tasks.extend(pet.get_tasks())
        return tasks
