import sys
import json

from clean_data import *
from validate_data import *


def main():

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Load data
    df = load_data(input_file)

    # Generate summary before cleaning
    summary_before = generate_summary(df)

    with open("task_4/output/summary_before.json", "w") as file:
        json.dump(summary_before, file, indent=4)

    # Cleaning
    df = remove_duplicates(df)
    df = standardize_domains(df)
    df = clean_attendance(df)
    df = clean_scores(df)
    df = clean_study_hours(df)
    df = clean_height(df)
    df = clean_weight(df)
    df = clean_submitted(df)
    df = handle_missing_values(df)

    # Validate
    if validate_cleaned_data(df):

        # Save cleaned CSV
        save_cleaned_data(df, output_file)

        # Generate summary after cleaning
        summary_after = generate_summary(df)

        with open("task_4/output/summary_after.json", "w") as file:
            json.dump(summary_after, file, indent=4)

        # Write report
        write_report("task_4/output/cleaning_report.md")

        print("Cleaning completed successfully!")

    else:
        print("Validation failed. Files were not saved.")


if __name__ == "__main__":
    main()