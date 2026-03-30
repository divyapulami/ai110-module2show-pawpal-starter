
```mermaid
classDiagram

class Owner {
  +int owner_id
  +string name
  +list~Pet~ pets
  +add_pet()
  +remove_pet()
  +get_pets()
}

class Pet {
  +int pet_id
  +string name
  +string species
  +string breed
  +int age
  +list~Task~ tasks
  +add_task()
  +remove_task()
  +get_tasks()
}

class Task {
  +int task_id
  +string title
  +string due_date
  +string task_type
  +bool completed
  +mark_complete()
  +update_task()
}

class Scheduler {
  +list~Task~ tasks
  +add_task()
  +remove_task()
  +get_tasks_for_today()
  +get_tasks_for_pet()
}

Owner "1" --> "*" Pet : owns
Pet "1" --> "*" Task : has
Scheduler "1" --> "*" Task : manages