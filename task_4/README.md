# Task 4 - Data Cleaning and Validation using Pandas

## Overview

This project demonstrates a complete data cleaning workflow using Python and the Pandas library. A messy student dataset is cleaned, validated, summarized, and exported into a structured format suitable for further analysis or machine learning.

The project focuses on understanding the importance of preprocessing real-world data before performing any analysis.

---

## Features

* Load CSV data using Pandas
* Generate dataset summaries before and after cleaning
* Remove duplicate records
* Standardize categorical values
* Convert mixed data formats into consistent numeric values
* Handle missing and invalid values
* Validate cleaned data
* Export cleaned dataset
* Generate a cleaning report automatically

---

## Project Structure

```
task_4/
│
├── README.md
├── notes.md
│
├── data/
│   └── messy_students.csv
│
├── output/
│   ├── cleaned_students.csv
│   ├── cleaning_report.md
│   ├── summary_before.json
│   └── summary_after.json
│
└── src/
    ├── clean_data.py
    ├── validate_data.py
    └── main.py
```

---

## Cleaning Steps Performed

* Removed duplicate rows
* Standardized domain names
* Converted attendance percentages into numeric values
* Converted textual scores into numeric values
* Converted study hours into numeric values
* Converted height values into centimeters
* Converted weight values into kilograms
* Standardized submitted values
* Handled missing values
* Validated cleaned dataset

---

## Validation Checks

The cleaned dataset is validated to ensure:

* No duplicate student IDs
* Attendance is between 0 and 100
* Allowed domain values only
* Allowed submitted values only
* No missing values in critical columns

---

## Technologies Used

* Python 3
* Pandas
* JSON

---

## How to Run

From the project root directory:

```bash
python task_4/src/main.py task_4/data/messy_students.csv task_4/output/cleaned_students.csv
```

---

## Output Files

After execution, the following files are generated inside the `output` folder:

* cleaned_students.csv
* summary_before.json
* summary_after.json
* cleaning_report.md

---

## Learning Outcomes

Through this project I learned:

* Working with Pandas DataFrames
* Cleaning messy datasets
* Handling missing and invalid values
* Converting data types
* Standardizing categorical data
* Data validation
* JSON generation
* Writing modular Python programs
* Organizing larger Python projects
