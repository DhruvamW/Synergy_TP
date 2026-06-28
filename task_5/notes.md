# Task 5 Notes

## New Concepts Learned

This project introduced the basics of data visualization using Matplotlib.

Data visualization helps convert numerical information into charts that are easier to understand and analyze.

---

# Libraries Used

## Pandas

Used for loading and preparing data.

```python
import pandas as pd
```

---

## Matplotlib

Used for creating charts and saving them as images.

```python
import matplotlib.pyplot as plt
```

---

# New Pandas Functions

## groupby()

Groups rows having the same value.

Example:

```python
df.groupby("domain")
```

Useful for calculating statistics for each category.

---

## mean()

Calculates the average value.

Example:

```python
df.groupby("domain")["score"].mean()
```

Returns the average score for every domain.

---

## value_counts()

Counts occurrences of each unique value.

Example:

```python
df["submitted"].value_counts()
```

Useful for creating frequency charts.

---

# Matplotlib Functions

## figure()

Creates a new figure.

```python
plt.figure(figsize=(6,4))
```

The figsize parameter controls the width and height of the graph.

---

## bar()

Creates a bar chart.

```python
plt.bar(x_values, y_values)
```

Used when comparing categories.

Example:

* Average score by domain
* Submission count

---

## scatter()

Creates a scatter plot.

```python
plt.scatter(x_values, y_values)
```

Useful for visualizing relationships between two numerical variables.

Example:

Attendance vs Score.

---

## title()

Adds a title to the graph.

```python
plt.title("Attendance vs Score")
```

---

## xlabel()

Adds a label to the x-axis.

```python
plt.xlabel("Attendance")
```

---

## ylabel()

Adds a label to the y-axis.

```python
plt.ylabel("Score")
```

---

## tight_layout()

```python
plt.tight_layout()
```

Automatically adjusts spacing so labels are not cut off.

---

## savefig()

```python
plt.savefig("graph.png")
```

Saves the graph as an image file.

---

## close()

```python
plt.close()
```

Closes the current figure after saving.

This prevents multiple graphs from overlapping.

---

# os.path.join()

```python
os.path.join(folder, filename)
```

Creates file paths that work correctly across different operating systems.

Instead of writing:

```python
"task_5/output/file.png"
```

we write:

```python
os.path.join(output_folder, "file.png")
```

---

# os.makedirs()

```python
os.makedirs(output_folder, exist_ok=True)
```

Creates a folder if it does not already exist.

The parameter:

```python
exist_ok=True
```

prevents an error if the folder already exists.

---

# Visualization Types Learned

## Bar Chart

Best used for comparing categories.

Examples:

* Average score by domain
* Number of submitted students

---

## Scatter Plot

Best used for showing relationships between two numerical variables.

Example:

Attendance percentage vs Score.

---

# Project Structure Learned

```text
main.py
│
└── visualize.py
```

main.py controls the program flow.

visualize.py contains reusable plotting functions.

Keeping visualization logic separate from program execution makes the project easier to maintain.

---

# Key Takeaways

* Always clean data before visualization.
* Choose the appropriate graph for the type of data.
* Label every graph properly.
* Save plots instead of relying on opening plot windows.
* Keep plotting functions modular and reusable.
* Separate visualization logic from the main program.
