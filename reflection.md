# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
My initial UML design for PawPal+ used four main classes: Owner, Pet, Task, and Scheduler. I chose these classes because they represent the main parts of a pet care system in a simple and organized way.

The Owner class is responsible for storing the owner's basic information and the list of pets they manage. Its main responsibility is to add, remove, and view pets.

The Pet class represents each individual pet. It stores details such as the pet's name, species, breed, age, and the list of tasks assigned to that pet. Its responsibility is to manage pet-specific tasks.

The Task class represents a care activity, such as feeding, walking, or grooming. It stores information like task title, due date, type of task, and whether the task is completed. Its responsibility is to track individual care actions.

The Scheduler class is responsible for organizing tasks. It manages the overall list of tasks and provides methods for adding, removing, and retrieving tasks, such as getting today's tasks or tasks for a specific pet.

In the UML design, one Owner can have many Pets, one Pet can have many Tasks, and the Scheduler manages Tasks across the system.
- What classes did you include, and what responsibilities did you assign to each?

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
Ans: My design did not change significantly during implementation. After reviewing the class skeleton, I found that the original structure was already clear and matched the main needs of the PawPal+ app.

I kept the four main classes because each one had a specific responsibility: Owner manages pets, Pet manages its tasks, Task stores care details, and Scheduler organizes tasks. I considered possible changes suggested during review, but I decided to keep the design simple and beginner-friendly so it would be easier to implement and understand.


---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
Ans: I chose constraints that fit the real-world use case of a pet owner with limited time and multiple responsibilities, so the scheduler stays useful without being complicated. The system always orders tasks by time so owners can follow a natural daily flow, and it lets them filter by completion and pet name to focus on what’s still pending for a specific animal. Recurring daily/weekly tasks are handled automatically so routine care (walks, meds) is not lost after marking it done. Basic conflict detection checks if two tasks share the same date and time to avoid impossible overlaps, because a person and pet usually cannot do two things exactly at once. These constraints keep the app grounded, easy to understand, and directly connected to helping a busy caregiver manage pet routines.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
Ans: For this project I chose simplicity over completeness, so conflict detection only checks exact date/time matches instead of full duration overlaps. That means if one task is 10:00–10:30 and another is 10:15–10:45, the system won’t flag it, but it does catch two tasks both set to 10:00 exactly. This tradeoff keeps implementation easy to understand and avoids adding interval math or additional fields (start/end) in this phase.

That tradeoff is acceptable here because the app is meant for a beginner-friendly demo and early scheduling behavior. It still gives useful feedback on clear clashes, while keeping logic lightweight so the core workflow is easier to build and reason about before adding more advanced timing features later.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
Ans: I used Copilot extensively throughout the project for brainstorming, code generation, and iteration. Early on, Copilot helped me generate a Mermaid UML diagram that clearly showed the relationships between Owner, Pet, Task, and Scheduler. From that diagram, I asked Copilot to generate Python class skeletons with type hints and docstrings, which gave me a solid foundation to build from. Once I had the skeleton, Copilot generated full method logic for features like sorting, filtering, and recurring task handling—I just had to verify each method made sense for my use case.

For testing, Copilot wrote pytest test cases that covered the main features (task completion, adding tasks, sorting, recurring behavior, conflict detection). Rather than writing tests from scratch, I could focus on ensuring they tested the right scenarios. When I needed to refactor or simplify code—like when I considered whether to use defaultdict for conflict detection—Copilot suggested cleaner versions and explained the tradeoffs, which helped me make an informed choice. Throughout the process, useful prompts included asking Copilot to "generate a UML diagram for these classes," "write pytest tests for task completion and recurring tasks," and "simplify this method for beginners."


**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
Ans: One example where I exercised judgment was when Copilot suggested a "cleaner version" of the conflict detection method using defaultdict. The original version I had written used dict.setdefault() which was already working. When Copilot suggested the defaultdict approach, I had to decide: is this truly more beginner-friendly, or does it introduce a new import and concept that might confuse someone learning the code? I evaluated it by considering my project's requirement to keep code "beginner-friendly"—while defaultdict is cleaner for experienced Python developers, I realized a beginner might not be familiar with it. I chose to keep a slightly more explicit version that avoided the extra import, prioritizing clarity over elegance. This taught me that not every "improvement" Copilot suggests aligns with my specific goals, and I need to verify suggestions against the project's actual requirements and audience.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
Ans: I wrote pytest tests that covered the core behaviors of the scheduler: task completion sets completed=True, adding a task to a pet increases the task count, and sorting returns tasks in chronological order by time. I also tested that marking a daily recurring task complete automatically creates a new task for the next day. Finally, I tested conflict detection to ensure it flags when two tasks are scheduled at the same date and time.

These behaviors matter because they are the foundation of the app. If task completion doesn't work, recurring tasks can't be auto-generated. If sorting is broken, the schedule appears in random order instead of a useful timeline. If conflict detection misses overlaps, the owner might unknowingly schedule two impossible tasks at once. By testing these key features, I can be confident the scheduler's core logic is sound.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
Ans: I have moderate confidence in the system for its current scope. The happy path tests pass, and the main features work as designed. However, there are edge cases I haven't fully tested yet. For example: What happens if a pet list is empty and I try to filter tasks by pet name? What if someone enters an invalid time format instead of HH:MM? What if the due_date string is malformed? What if I try to complete a task that doesn't exist? These edge cases could cause crashes or unexpected behavior.

To increase confidence, I would write additional tests for these scenarios: invalid inputs, empty collections, and missing IDs. I would also test what happens when two tasks overlap in time (not just exact matches, but overlapping ranges). Right now the system is solid for normal use, but adding robustness around edge cases and error handling would make it production-ready.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
Ans: Building the system structure was surprisingly smooth. Starting with a clear UML diagram made it easy to define the classes and their relationships before writing any code. Having Owner, Pet, Task, and Scheduler as separate, focused classes kept the code organized and easy to understand. Connecting the Streamlit UI to the backend logic also worked well—once the scheduler methods were built, wiring them to the UI with tables and status messages felt natural. Using AI to generate code skeletons, tests, and refactoring suggestions saved me tons of time and let me focus on design decisions rather than boilerplate. The project came together faster than I expected, and the code is beginner-friendly.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
Ans: The Streamlit UI could be much better. Right now it's functional but basic—I'd love to add visual charts showing the daily schedule, pet icons, and maybe drag-and-drop to reschedule tasks. The scheduling logic itself could be smarter: currently it only catches exact time matches, but real conflict detection should handle overlapping durations (if a task runs 10:00–10:30, it shouldn't conflict with one at 10:31). I'd also add more advanced features like task priorities, task duration, and smarter recurrence patterns (e.g., "every other day"). Finally, the project structure could use better separation of concerns—maybe a separate utils.py file for helper functions to keep pawpal_system.py even cleaner.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
Ans: I learned that system design matters way more than I thought. Spending time on the UML upfront saved me from rewriting code later. I also learned that AI is an amazing brainstorming partner and code generator, but it's not a replacement for thinking. When Copilot suggested improvements, I had to evaluate them against my actual goals (keep it beginner-friendly, stay simple). The best approach was to use AI to speed up tedious parts (skeleton generation, test writing) while keeping the design decisions in my hands. Working with AI felt like having a knowledgeable friend who can instantly suggest code—but I'm still the architect.

