## 🧺 Smart Fridge Manager

### Overview

A small Python project to simulate a smart fridge that processes text-based commands like `Add milk 2`, `Use eggs 1`, and `Report`.
It will help you practice **file parsing**, **state management**, and **error handling**.

---

### Getting Started

1. **Fork** this repository.
2. **Clone** your fork:

   ```bash
   git clone <your-fork-url>
   cd jhb58-mars_rover_prep
   ```
3. Run the program:

   ```bash
   python main.py path/to/instructions.txt
   ```

---

### Example Input

```
Add milk 2
Add eggs 12
Use milk 1
Use bread 1
Report
```

### Example Output

```
Fridge initialized. It's currently empty.
Adding 2 milk (instruction 1)
milk: 2
Adding 12 eggs (instruction 2)
milk: 2, eggs: 12
Using 1 milk (instruction 3)
milk: 1, eggs: 12
Item 'bread' not found, skipping (instruction 4)
milk: 1, eggs: 12
Reporting inventory (instruction 5)
milk: 1, eggs: 12
```

---

### Commands

* `Add <item> <quantity>`
* `Use <item> <quantity>`
* `Report`
* `Clear`

Commands are **case-insensitive** and blank lines are ignored.

---

### Notes

* Handle invalid input gracefully — the program should never crash.
* Output the instruction number in every message.
* You may add tests under `tests/test_smart_fridge.py`.

---

Would you like me to make the short sample `instructions.txt` file for them too?
