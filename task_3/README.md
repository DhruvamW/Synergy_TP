# CSV Parser and Data Analysis in Python

## Project Overview

This project demonstrates how CSV data can be parsed and analyzed in two different ways:

1. **Manual CSV Parsing** using Python's built-in file handling without relying on the `csv` module.
2. **CSV Parsing using pandas** to perform the same analysis with a high-level library.

The objective is to understand what happens behind the scenes when libraries like pandas read CSV files and why they make data analysis significantly easier.

---

## Folder Structure

```
task_3/
│
├── data/
│   └── submissions.csv
│
├── output/
│   ├── manual_summary.json
│   ├── pandas_summary.json
│   └── comparison_report.md
│
├── src/
│   ├── manual_parser.py
│   ├── pandas_parser.py
│   └── main.py
│
└── README.md
```

---

## Features

### Manual CSV Parser

* Reads CSV files using `open()`
* Uses context managers (`with`)
* Parses CSV rows manually using `split(",")`
* Creates dictionaries from CSV rows
* Converts data types
* Handles malformed rows
* Ignores empty lines
* Calculates summary statistics
* Exports results to JSON

### Pandas Parser

* Reads CSV using `pandas.read_csv()`
* Converts column data types
* Uses DataFrame operations to compute statistics
* Produces the same output as the manual parser
* Exports results to JSON

### Comparison Report

Compares the outputs of the manual parser and pandas parser and generates a Markdown report indicating whether both implementations produce identical results.

---

## Summary Generated

The program calculates:

* Total number of students
* Number of submitted students
* Number of missing submissions
* Average score
* Highest scorer
* Lowest scorer among submitted students
* Domain-wise average score
* Students who did not submit
* Students scoring below 5

---

## Technologies Used

* Python 3
* pandas
* pathlib
* json

---

## How to Run

From the project root directory:

```bash
python task_3/src/main.py task_3/data/submissions.csv
```

---

## Output Files

After execution, the following files are generated automatically:

```
task_3/output/
│
├── manual_summary.json
├── pandas_summary.json
└── comparison_report.md
```

---

## Concepts Practiced

* File Handling
* Context Managers
* Manual CSV Parsing
* Dictionaries
* Lists
* JSON Serialization
* Exception Handling
* Command-Line Arguments
* Pandas DataFrames
* Grouping and Aggregation
* Boolean Indexing
* Modular Programming
* Separation of Concerns

---

## Learning Outcome

This project helped me understand how CSV files are manually parsed before using high-level libraries such as pandas. It also demonstrated how pandas simplifies data processing while producing the same results with significantly less code.
