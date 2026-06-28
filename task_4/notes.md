# Task 4 Notes

## New Concepts Learned

### 1. Data Cleaning

Data cleaning is the process of preparing raw data before analysis.

Common cleaning tasks include:

* Removing duplicates
* Fixing inconsistent values
* Handling missing values
* Converting data types
* Standardizing units
* Validating data

---

## Pandas Functions Learned

### Reading CSV

```python
pd.read_csv("file.csv")
```

Loads a CSV file into a DataFrame.

---

### Saving CSV

```python
df.to_csv("output.csv", index=False)
```

Saves a DataFrame as a CSV file.

---

### Summary Functions

```python
len(df)
```

Returns number of rows.

```python
df.shape
```

Returns (rows, columns).

```python
df.columns
```

Returns column names.

```python
df.dtypes
```

Returns data types of every column.

```python
df.isna()
```

Returns a DataFrame showing missing values.

```python
df.isna().sum()
```

Counts missing values in every column.

```python
df.duplicated()
```

Returns duplicate rows.

```python
df.duplicated().sum()
```

Counts duplicate rows.

```python
df.unique()
```

Returns unique values of a column.

---

## Cleaning Functions

### drop_duplicates()

```python
df.drop_duplicates()
```

Removes duplicate rows.

---

### replace()

```python
df["column"].replace(mapping)
```

Replaces values using a dictionary.

Example:

```python
{
    "ml": "ML",
    "web": "Web"
}
```

---

### to_numeric()

```python
pd.to_numeric(column, errors="coerce")
```

Converts values into numeric data.

Invalid values become NaN.

---

### fillna()

```python
df["score"].fillna(df["score"].median())
```

Replaces missing values.

---

### apply()

```python
df["height"].apply(function)
```

Applies a custom function to every value in a column.

Useful when built-in functions are not enough.

---

### str Methods

```python
.str.replace()
```

Replaces text inside strings.

```python
.str.strip()
```

Removes leading and trailing spaces.

```python
.str.lower()
```

Converts text to lowercase.

---

## JSON

### Saving JSON

```python
json.dump(dictionary, file, indent=4)
```

Used to save Python dictionaries as JSON files.

---

## Command Line Arguments

```python
sys.argv
```

Used to read arguments from the terminal.

Example:

```bash
python main.py input.csv output.csv
```

---

## Validation Techniques

Checking duplicate values:

```python
df["student_id"].duplicated().sum()
```

Checking allowed values:

```python
df["domain"].isin(allowed_domains)
```

Checking missing values:

```python
df.isna().sum().sum()
```

Checking ranges:

```python
(df["attendance_percent"] < 0) | (df["attendance_percent"] > 100)
```

---

## Project Structure Learned

```
main.py
│
├── clean_data.py
│       Cleaning functions
│
└── validate_data.py
        Validation functions
```

Keeping different responsibilities in separate files makes code easier to understand, maintain, and debug.

---

## Key Takeaways

* Always inspect data before cleaning.
* Clean data before analysis.
* Validate cleaned data before saving.
* Keep functions small and focused.
* Separate cleaning logic from validation logic.
* Write reusable and readable code.
* Document every important step.
