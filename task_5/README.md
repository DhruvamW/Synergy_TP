# Task 5 - Data Visualization using Matplotlib

## Overview

This project visualizes the cleaned student dataset generated in Task 4 using Matplotlib.

The objective is to transform cleaned tabular data into meaningful visualizations that help identify trends, compare categories, and summarize information graphically.

---

## Features

* Load cleaned CSV data using Pandas
* Generate a bar chart of average score by domain
* Generate a scatter plot of attendance vs score
* Generate a bar chart showing submission status count
* Save all plots as PNG images
* Automatically generate a plot summary in Markdown format

---

## Project Structure

```text
task_5/
│
├── README.md
├── notes.md
│
├── output/
│   ├── attendance_vs_score.png
│   ├── domain_average_score.png
│   ├── submission_status_count.png
│   └── plot_summary.md
│
└── src/
    ├── visualize.py
    └── main.py
```

---

## Input

The project uses the cleaned dataset generated in Task 4.

```
task_4/output/cleaned_students.csv
```

---

## Visualizations Generated

### 1. Domain Average Score

Displays the average score of students belonging to each domain using a bar chart.

### 2. Attendance vs Score

Displays the relationship between attendance percentage and student scores using a scatter plot.

### 3. Submission Status Count

Displays the number of students who submitted and did not submit their work.

---

## Technologies Used

* Python 3
* Pandas
* Matplotlib

---

## How to Run

Run the following command from the project root:

```bash
python task_5/src/main.py task_4/output/cleaned_students.csv task_5/output
```

---

## Output Files

The following files are generated automatically:

* domain_average_score.png
* attendance_vs_score.png
* submission_status_count.png
* plot_summary.md

---

## Learning Outcomes

Through this project I learned:

* Loading cleaned datasets
* Basic data visualization
* Creating bar charts
* Creating scatter plots
* Grouping data with Pandas
* Counting categorical values
* Saving plots as image files
* Organizing visualization code into reusable functions
