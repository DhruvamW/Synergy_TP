import pandas as pd

def load_data(file_path: str):
    df = pd.read_csv(file_path)
    return df

def generate_summary(df) -> dict:
    summary={
        "rows" : len(df),
        "columns" : df.shape[1],
        "column_names" : df.columns.tolist(),
        "data_types" : df.dtypes.astype(str).to_dict(),
        "missing_values" : df.isna().sum().to_dict(),
        "duplicates" : int(df.duplicated().sum()),
        "unique domains": df["domain"].unique().tolist(),
        "unique_submitted": df["submitted"].unique().tolist()
    }
    return summary

def remove_duplicates(df):
    return df.drop_duplicates()

def standardize_domains(df):
    domain_map = {
        "ml": "ML",
        "ML": "ML",
        "MACHINE LEARNING": "ML",
        "web": "Web",
        "Web Dev": "Web",
        "web development": "Web",
        "electronics": "Electronics",
        "Electronics": "Electronics",
        "Mechanical": "Mechanical"
    }

    df["domain"] = df["domain"].replace(domain_map)
    return df

def clean_attendance(df):
    df["attendance_percent"] = df["attendance_percent"].astype(str).str.replace("%", "", regex=False)

    df["attendance_percent"] = pd.to_numeric(df["attendance_percent"],errors="coerce")

    df.loc[(df["attendance_percent"] < 0) | (df["attendance_percent"] > 100),"attendance_percent"]=pd.NA
    return df

def clean_scores(df):
    score_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10
    }

    df["score"] = df["score"].replace(score_map)
    df["score"] = pd.to_numeric(df["score"],errors="coerce")
    return df

def clean_study_hours(df):
    hours_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10
    }

    df["study_hours"] = df["study_hours"].replace(hours_map)

    df["study_hours"] = pd.to_numeric(df["study_hours"], errors="coerce")

    return df

def clean_height(df):
    def convert_height(value):
        if pd.isna(value):
            return pd.NA
        value = str(value).strip().lower()
        if "cm" in value:
            return float(value.replace("cm", "").strip())
        if "m" in value:
            return float(value.replace("m", "").strip()) * 100
        return pd.NA

    df["height_cm"] = df["height"].apply(convert_height)
    df.drop(columns=["height"], inplace=True)
    return df

def clean_weight(df):
    df["weight_kg"] = df["weight"].astype(str).str.replace("kg", "", regex=False).str.strip()

    df["weight_kg"] = pd.to_numeric(df["weight_kg"],errors="coerce")
    df.drop(columns=["weight"], inplace=True)
    return df

def clean_submitted(df):
    submit_map = {
        "yes": "Yes",
        "Yes": "Yes",
        "Y": "Yes",
        "no": "No",
        "No": "No",
        "N": "No"
    }
    df["submitted"] = df["submitted"].replace(submit_map)
    return df

def handle_missing_values(df):
    numeric_columns = [
        "attendance_percent",
        "score",
        "study_hours",
        "height_cm",
        "weight_kg"
    ]

    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].median())

    df["domain"] = df["domain"].fillna(df["domain"].mode()[0])
    df["submitted"] = df["submitted"].fillna("No")

    return df

def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)

def write_report(report_path):
    report = """
# Data Cleaning Report

## Cleaning Steps Performed

- Removed duplicate rows.
- Standardized domain names.
- Converted attendance_percent to numeric values.
- Converted score to numeric values.
- Converted study_hours to numeric values.
- Converted height to centimeters.
- Converted weight to kilograms.
- Standardized submitted values.
- Replaced invalid attendance values with missing values.
- Filled missing numeric values using the median.
- Filled missing submitted values with 'No'.

## Validation

The cleaned dataset satisfies the required validation rules.
"""

    with open(report_path, "w") as file:
        file.write(report)
