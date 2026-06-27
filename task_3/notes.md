# Notes - Task 3

## 1. Reading Files

```python
with open(file_path) as file:
```

* Opens a file safely.
* Automatically closes the file after use.

---

## 2. Reading One Line

```python
header = next(file)
```

* Reads only the first line of a file.
* Useful for extracting CSV headers.

---

## 3. Removing Extra Spaces

```python
line.strip()
```

Removes:

* Leading spaces
* Trailing spaces
* Newline (`\n`)

Example:

```
"Aarav,ML\n"

↓

"Aarav,ML"
```

---

## 4. Splitting Strings

```python
line.split(",")
```

Converts

```
Aarav,ML,Task2,8,yes
```

into

```python
[
    "Aarav",
    "ML",
    "Task2",
    "8",
    "yes"
]
```

---

## 5. Creating Dictionaries

```python
student[header[i]] = record[i]
```

Maps CSV headers to corresponding values.

Result:

```python
{
    "name": "Aarav",
    "score": "8"
}
```

---

## 6. Converting Data Types

```python
int()
```

Converts strings to integers.

```python
.lower()
```

Converts text to lowercase.

Used for converting

```
YES

↓

yes
```

---

## 7. Exception Handling

```python
try:
    ...
except ValueError:
```

Prevents the program from crashing when invalid values are encountered.

---

## 8. Dictionary `.get()`

```python
dictionary.get(key, default)
```

Returns the value if the key exists.

Otherwise returns the default value.

Useful for counting and accumulating values.

Example:

```python
counts[key] = counts.get(key, 0) + 1
```

---

## 9. JSON

```python
json.dump(data, file, indent=4)
```

Writes Python dictionaries into JSON files.

`indent=4` formats the output for readability.

---

## 10. pathlib

```python
Path(output_path)
```

Represents file paths as objects.

```python
path.parent.mkdir(parents=True, exist_ok=True)
```

Creates directories automatically if they do not exist.

---

## 11. Command-Line Arguments

```python
sys.argv
```

Stores arguments passed when running the program.

Example:

```bash
python main.py data.csv
```

```python
sys.argv[1]
```

contains

```
data.csv
```

---

## 12. `if __name__ == "__main__":`

Used to execute code only when a file is run directly.

Prevents `main()` from executing when the file is imported by another Python file.

---

# Pandas Concepts

## Reading CSV

```python
pd.read_csv()
```

Reads a CSV file into a DataFrame.

---

## DataFrame

A DataFrame is a table consisting of rows and columns.

Similar to an Excel spreadsheet.

---

## Converting Column Types

```python
.astype()
```

Example:

```python
df["score"] = df["score"].astype(int)
```

---

## Mapping Values

```python
.map()
```

Used to replace values.

Example:

```python
df["submitted"] = df["submitted"].map({
    "yes": True,
    "no": False
})
```

---

## Selecting Columns

```python
df["score"]
```

Returns a single column.

---

## Filtering Rows

```python
df[df["score"] < 5]
```

Returns rows satisfying a condition.

---

## Boolean Indexing

```python
df[df["submitted"]]
```

Returns only submitted students.

---

## Aggregation Functions

```python
.mean()
```

Average

```python
.max()
```

Maximum

```python
.min()
```

Minimum

```python
.sum()
```

Sum

---

## Grouping

```python
.groupby()
```

Groups rows by a column.

Example:

```python
df.groupby("domain")["score"].mean()
```

Computes the average score for each domain.

---

## Accessing Rows

```python
.loc[]
```

Retrieves rows and columns by label.

Example:

```python
df.loc[index, "name"]
```

---

## Finding Maximum/Minimum Index

```python
.idxmax()
```

Returns the index of the maximum value.

```python
.idxmin()
```

Returns the index of the minimum value.

---

## Converting Pandas Objects

```python
.tolist()
```

Converts a Series into a Python list.

```python
.to_dict()
```

Converts a Series into a Python dictionary.

---

# Important Programming Concepts Learned

* Manual CSV parsing
* Data cleaning
* Type conversion
* File handling
* Exception handling
* JSON serialization
* Modular programming
* Separation of concerns
* Data aggregation
* Dictionary accumulation
* Pandas DataFrame operations
* Command-line interfaces (CLI)
* Comparing outputs from two independent implementations
* Writing Markdown reports
