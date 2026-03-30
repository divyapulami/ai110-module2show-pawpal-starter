from pawpal_system import Owner, Pet, Task, Scheduler


def main() -> None:
    # create owner
    owner = Owner(owner_id=1, name="Alex")

    # create pets
    pet1 = Pet(pet_id=101, name="Buddy", species="Dog", breed="Labrador", age=4)
    pet2 = Pet(pet_id=102, name="Mittens", species="Cat", breed="Siamese", age=2)

    owner.add_pet(pet1)
    owner.add_pet(pet2)

    # create tasks
    task1 = Task(
        task_id=1001,
        title="Morning walk",
        description="30-minute walk in the park",
        due_date="2026-03-29",
        time="08:00",
        frequency="daily",
    )

    task2 = Task(
        task_id=1002,
        title="Medication",
        description="Give heartworm medicine",
        due_date="2026-03-29",
        time="13:00",
        frequency="weekly",
    )

    task3 = Task(
        task_id=1003,
        title="Evening play",
        description="Play with toys for 20 minutes",
        due_date="2026-03-29",
        time="18:30",
        frequency="daily",
    )

    # scheduler
    scheduler = Scheduler()
    scheduler.add_task(task1, pet=pet1)
    scheduler.add_task(task2, pet=pet1)
    scheduler.add_task(task3, pet=pet2)

    # print today's schedule
    today = "2026-03-29"
    todays_tasks = scheduler.get_tasks_for_today(today)

    print("Today's Schedule (", today, ")")
    print("==========================")
    for task in sorted(todays_tasks, key=lambda x: x.time):
        assigned_pet = None
        if task in pet1.tasks:
            assigned_pet = pet1.name
        elif task in pet2.tasks:
            assigned_pet = pet2.name
        else:
            assigned_pet = "Unknown"

        status = "Done" if task.completed else "Pending"
        print(f"{task.time} - {task.title} [{assigned_pet}] - {status}")


if __name__ == "__main__":
    main()
