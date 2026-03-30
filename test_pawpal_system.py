import pytest
from pawpal_system import Pet, Task


def test_task_mark_complete_sets_completed_true():
    task = Task(
        task_id=1,
        title="Water plants",
        description="Water indoor plants",
        due_date="2026-03-29",
        time="09:00",
        frequency="daily",
        completed=False,
    )

    task.mark_complete()

    assert task.completed is True


def test_pet_add_task_increases_task_count():
    pet = Pet(pet_id=1, name="Fin", species="Fish", breed="Goldfish", age=1)
    initial_count = len(pet.get_tasks())

    task = Task(
        task_id=2,
        title="Clean tank",
        description="Change water and clean tank",
        due_date="2026-03-29",
        time="10:00",
        frequency="weekly",
    )

    pet.add_task(task)

    assert len(pet.get_tasks()) == initial_count + 1
