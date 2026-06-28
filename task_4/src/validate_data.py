import pandas as pd


def validate_cleaned_data(df):
    valid = True

    # 1. Duplicate student IDs
    if df["student_id"].duplicated().sum() > 0:
        print("Duplicate student IDs found.")
        valid = False

    # 2. Attendance should be between 0 and 100
    if ((df["attendance_percent"] < 0) | (df["attendance_percent"] > 100)).any():
        print("Invalid attendance values found.")
        valid = False

    # 3. Check domains
    allowed_domains = ["ML", "Web", "Electronics", "Mechanical"]

    if not df["domain"].isin(allowed_domains).all():
        print("Invalid domain values found.")
        valid = False

    # 4. Check submitted values
    allowed_submitted = ["Yes", "No"]

    if not df["submitted"].isin(allowed_submitted).all():
        print("Invalid submitted values found.")
        valid = False

    # 5. Check missing values
    if df.isna().sum().sum() > 0:
        print("Missing values still exist.")
        valid = False

    if valid:
        print("Validation Successful!")

    return valid