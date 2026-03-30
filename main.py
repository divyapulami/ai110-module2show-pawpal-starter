from pawpal_system import Owner, Pet, Task, Scheduler


def main() -> None:
    owner = Owner(owner_id=1, name="Alex")

    pet1 = Pet(pet_id=101, name="Buddy", species="Dog", breed="Labrador", age=4)
    pet2 = Pet(pet_id=102, name="Mittens", species="Cat", breed="Siamese", age=2)

    owner.add_pet(pet1)
    owner.add_pet(pet2)

    # create tasks out of chronological order
    task_a = Task(
        task_id=1001,
        title="Evening play",
        description="Play with toys for 20 minutes",
        time="18:30",
        frequency="daily",
    )

    task_b = Task(
        task_id=1002,
        title="Morning walk",
        description="30-minute walk in the park",
        time="08:00",
        frequency="daily",
    )

    task_c = Task(
        task_id=1003,
        title="Medication",
        description="Give heartworm medicine",
        time="13:00",
        frequency="weekly",
    )

    # assign tasks to pets and scheduler
    scheduler = Scheduler()
    scheduler.add_task(task_a, pet=pet1)
    scheduler.add_task(task_b, pet=pet2)
    scheduler.add_task(task_c, pet=pet1)

    # mark one complete
    task_c.mark_complete()

    def print_section(title: str, tasks: list[Task]) -> None:
        print("\n" + title)
        print("-" * len(title))
        for t in tasks:
            pet_name = "Buddy" if t in pet1.tasks else "Mittens" if t in pet2.tasks else "Unknown"
            status = "Done" if t.completed else "Pending"
            print(f"{t.time} | {t.title} | {pet_name} | {status}")

    # 1. all tasks
    print_section("All tasks", scheduler.tasks)

    # 2. tasks sorted by time
    sorted_tasks = scheduler.sort_by_time()
    print_section("Tasks sorted by time", sorted_tasks)

    # 3. incomplete tasks only
    incomplete_tasks = scheduler.filter_by_completion(False)
    print_section("Incomplete tasks", incomplete_tasks)

    # 4. tasks for one pet
    tasks_for_buddy = scheduler.filter_by_pet_name("Buddy", owner)
    print_section("Tasks for pet Buddy", tasks_for_buddy)


if __name__ == "__main__":
    main()
