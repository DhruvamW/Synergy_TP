# Python Notes - Student Submission Analyzer

## Project Overview

This project reads student submission data from a CSV file, performs various analyses, and writes the results to a JSON file.

---

# New Python Concepts Learned

## 1. Modular Programming

Instead of writing everything in one file:

* `main.py` controls the flow of the program.
* `analyzer.py` contains reusable functions.

Benefits:

* Easier to debug
* Easier to maintain
* Functions can be reused in other projects

---

## 2. Command Line Arguments

Import:

```python
import sys
```

Access arguments:

```python
sys.argv
```

Example:

```bash
python main.py input.csv output.json
```

Produces:

```python
sys.argv[0]  # main.py
sys.argv[1]  # input.csv
sys.argv[2]  # output.json
```

---

## 3. Type Hints

Example:

```python
def calculate_average_score(students: list[dict]) -> float:
```

Common type hints:

```python
str
int
float
bool
list[str]
list[dict]
dict[str, int]
dict[str, float]
None
```

Purpose:

* Improves readability
* Helps IDEs detect mistakes
* Makes function expectations clear

---

## 4. Reading CSV Files

Import:

```python
import csv
```

Read CSV:

```python
with open(file_path) as file:
    reader = csv.DictReader(file)
```

`DictReader` converts each row into a dictionary.

Example:

CSV

```text
name,score
Aarav,8
```

becomes

```python
{
    "name": "Aarav",
    "score": "8"
}
```

---

## 5. Lists of Dictionaries

Data structure used throughout the project:

```python
students = [
    {
        "name": "Aarav",
        "score": 8,
        "submitted": "yes"
    },
    {
        "name": "Meera",
        "score": 6,
        "submitted": "yes"
    }
]
```

Advantages:

* Easy filtering
* Easy searching
* Easy calculations

---

## 6. Converting Data Types

CSV stores everything as strings.

Convert score:

```python
row["score"] = int(row["score"])
```

---

## 7. Dictionary Methods

### get()

```python
dictionary.get(key, default)
```

Example:

```python
scores.get("ML", 0)
```

Returns:

* value if key exists
* default value otherwise

Useful for counting and summing.

---

## 8. Dictionary Aggregation

Used for domain-wise averages.

Instead of writing many variables:

```python
ml_score
web_score
electronics_score
```

Use dictionaries:

```python
scores = {}
counts = {}
```

Update values:

```python
scores[domain] = scores.get(domain, 0) + score
counts[domain] = counts.get(domain, 0) + 1
```

---

## 9. Working with JSON

Import:

```python
import json
```

Write dictionary:

```python
json.dump(summary, file, indent=4)
```

`indent=4` formats the JSON nicely.

---

## 10. pathlib

Import:

```python
from pathlib import Path
```

Create Path object:

```python
path = Path(output_path)
```

Parent folder:

```python
path.parent
```

Create folders:

```python
path.parent.mkdir(
    parents=True,
    exist_ok=True
)
```

---

## 11. File Modes

Read

```python
"r"
```

Write (overwrite)

```python
"w"
```

Append

```python
"a"
```

Create only if file doesn't exist

```python
"x"
```

---

## 12. Error Handling

General syntax:

```python
try:
    ...
except ExceptionType:
    ...
```

Errors handled:

### FileNotFoundError

```python
except FileNotFoundError:
```

When file doesn't exist.

---

### ValueError

```python
except ValueError:
```

When converting invalid values.

Example:

```python
int("abc")
```

---

### OSError

```python
except OSError:
```

File cannot be created or written.

---

## 13. continue

Skip current iteration.

Example:

```python
for row in reader:

    try:
        row["score"] = int(row["score"])

    except ValueError:
        continue
```

Moves to next row.

---

## 14. return

Immediately exits a function.

Example:

```python
return average
```

Everything after `return` is ignored.

Important lesson:

Do **not** return inside loops unless you intentionally want to stop after the first match.

---

## 15. if not

Instead of

```python
if len(students) == 0:
```

Pythonic version:

```python
if not students:
```

Works for:

* empty list
* empty dictionary
* empty string

---

## 16. len()

Returns number of elements.

```python
len(students)
```

Examples:

```python
len(list)
len(dictionary)
len(string)
```

---

## 17. Building Summary Dictionaries

Instead of many variables:

```python
summary = {
    ...
}
```

Store everything in one dictionary.

Easy to print.

Easy to save.

Easy to send between functions.

---

## 18. Function Design

Good functions should:

* Do one job
* Accept arguments
* Return values
* Avoid global variables

Example:

```python
students = read_submissions(input_file)
```

Instead of reading the file repeatedly inside every function.

---

## 19. Main Program Structure

Typical Python program:

```python
imports

↓

functions

↓

main()

↓

if __name__ == "__main__":
    main()
```

Keeps code organized.

---

# Useful Built-in Functions

```python
len()

int()

float()

print()

open()

list()

dict()

sum()

max()

min()
```

---

# Modules Learned

```python
csv
json
sys
pathlib
```

---

# Python Concepts Practiced

* Variables
* Functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* File handling
* JSON serialization
* CSV parsing
* Type hints
* Error handling
* Modular programming
* Command-line arguments
* Data aggregation

---

# Key Takeaways

* Avoid global variables.
* Read the input file only once.
* Pass data between functions.
* Use dictionaries for grouped calculations.
* Handle exceptions gracefully.
* Keep functions focused on a single responsibility.
* Separate business logic (`analyzer.py`) from execution flow (`main.py`).
* Prefer readable and modular code over repeated code.
* Use Python's standard library whenever possible before looking for external packages.

---
