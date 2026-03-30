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
My design did not change significantly during implementation. After reviewing the class skeleton, I found that the original structure was already clear and matched the main needs of the PawPal+ app.

I kept the four main classes because each one had a specific responsibility: Owner manages pets, Pet manages its tasks, Task stores care details, and Scheduler organizes tasks. I considered possible changes suggested during review, but I decided to keep the design simple and beginner-friendly so it would be easier to implement and understand.


---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
