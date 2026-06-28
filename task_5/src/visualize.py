import pandas as pd
import matplotlib.pyplot as plt

def load_cleaned_data(file_path):
    return pd.read_csv(file_path)


def plot_domain_average_score(df, output_path):
    average_scores = df.groupby("domain")["score"].mean()

    plt.figure(figsize=(6, 4))
    plt.bar(average_scores.index, average_scores.values)

    plt.title("Average Score by Domain")
    plt.xlabel("Domain")
    plt.ylabel("Average Score")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_attendance_vs_score(df, output_path):
    plt.figure(figsize=(6, 4))

    plt.scatter(df["attendance_percent"], df["score"])

    plt.title("Attendance vs Score")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Score")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_submission_status_count(df, output_path):
    submission_count = df["submitted"].value_counts()

    plt.figure(figsize=(5, 4))

    plt.bar(submission_count.index, submission_count.values)

    plt.title("Submission Status Count")
    plt.xlabel("Submission Status")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def write_plot_summary(output_path):
    summary = """
# Plot Summary

## 1. Domain Average Score

This bar chart shows the average score of students in each domain.
It helps compare the academic performance of different domains.
Higher bars indicate higher average scores.

---

## 2. Attendance vs Score

This scatter plot shows the relationship between attendance and score.
Students with higher attendance generally tend to have better scores.
It helps identify trends and possible outliers.

---

## 3. Submission Status Count

This bar chart displays the number of students who submitted and did not submit.
It provides a quick overview of overall submission status.
"""

    with open(output_path, "w") as file:
        file.write(summary)