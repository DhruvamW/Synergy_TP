# Student Submission Analyzer

## Overview

The Student Submission Analyzer is a Python program that reads student submission data from a CSV file, analyzes the records, and generates a summary report in JSON format.

The project demonstrates the use of modular programming, file handling, CSV processing, JSON serialization, dictionaries, lists, command-line arguments, and error handling.

---

## Project Structure

```
task_2/
│
├── data/
│   └── submissions.csv
│
├── output/
│   └── summary.json
│
└── src/
    ├── analyzer.py
    └── main.py
```

---

## Features

* Reads submission records from a CSV file.
* Calculates:

  * Total number of students
  * Number of submitted students
  * Number of missing submissions
  * Average score
  * Highest scorer
  * Lowest scorer among submitted students
  * Domain-wise average score
  * Students who did not submit
  * Students scoring below 5
* Generates a formatted JSON summary.
* Handles common errors gracefully.

---

## Technologies Used

* Python 3
* csv module
* json module
* pathlib module
* sys module

---

## Error Handling

The program handles:

* Missing input CSV file
* Invalid score values
* Empty CSV files
* Missing output directory

---

## Running the Program

From the repository root, run:

```bash
python task_2/src/main.py task_2/data/submissions.csv task_2/output/summary.json
```

---

## Output

The terminal displays:

* Total Students
* Submitted Count
* Missing Count
* Average Score
* Highest Scorer
* Lowest Scorer
* Domain-wise Average
* Missing Submissions
* Students Scoring Below 5
* Confirmation that the summary file was written

A JSON summary report is generated inside:

```
task_2/output/summary.json
```

---

## Concepts Practiced

* Modular Programming
* Functions
* Type Hints
* Lists and Dictionaries
* CSV File Handling
* JSON File Handling
* Command-Line Arguments
* Error Handling using try-except
* Path Handling using pathlib
* Data Aggregation
* Dictionary Methods
* Python Standard Library

