# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.


## Smarter Scheduling

PawPal+ now includes smarter scheduling features to help organize pet care tasks more effectively. Tasks can be sorted by time, filtered by pet or completion status, and checked for simple scheduling conflicts. The system also supports recurring daily and weekly tasks by automatically creating the next occurrence when a recurring task is completed.

## Testing PawPal+

PawPal+ includes an automated pytest test suite to verify the main system behaviors.

To run the tests, use:

```bash
python -m pytest

## Features

- Add and manage pets
- Create and track care tasks
- Sort tasks by time for better scheduling
- Filter tasks by pet or completion status
- Automatically generate recurring daily and weekly tasks
- Detect scheduling conflicts and show warnings

## Demo
<a href="/course_images/ai110/pawpal_demo.jpeg" target="_blank">
<img src='/course_images/ai110/pawpal_demo.jpeg' title='PawPal App' alt='PawPal App' />
</a>