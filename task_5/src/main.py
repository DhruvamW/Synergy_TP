import sys
import os
from visualize import *

def main():
    input_file = sys.argv[1]
    output_folder = sys.argv[2]
    os.makedirs(output_folder, exist_ok=True)

    df = load_cleaned_data(input_file)

    plot_domain_average_score(df, os.path.join(output_folder, "domain_average_score.png"))

    plot_attendance_vs_score(df, os.path.join(output_folder, "attendance_vs_score.png"))

    plot_submission_status_count(df, os.path.join(output_folder, "submission_status_count.png"))

    write_plot_summary(os.path.join(output_folder, "plot_summary.md"))

    print("All plots generated successfully!")


if __name__ == "__main__":
    main()