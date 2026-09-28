# PLP Python Week 6 Assignment - Error Handling

## File Descriptions
* **safe_tools.py**: Contains utility functions (`safe_divide`, `safe_number`, `get_field`) utilizing `try / except` blocks to catch specific runtime exceptions.
* **unbreakable.py**: Demonstrates how to keep a program running continuously and gracefully handle bad user inputs without crashing.

## Question & Answer
**Why can the `if` check not catch `"abc"` on its own?**
An `if` check cannot easily anticipate or prevent conversion exceptions like `int("abc")` because Python evaluates the conversion attempt at runtime and raises a `ValueError` directly when the conversion fails. A `try / except` block catches this exception after it occurs, allowing the program to recover smoothly instead of crashing.
