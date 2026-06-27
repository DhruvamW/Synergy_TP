import sys
from manual_parser import (
    read_csv_manual,
    convert_types,
    calculate_summary,
    write_json,
)

from pandas_parser import (
    read_csv_pandas,
    calculate_summary_pandas,
)

from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: python task_3/src/main.py <csv_file>")
        return

    manual_output = "task_3/output/manual_summary.json"
    pandas_output = "task_3/output/pandas_summary.json"
    report_output = "task_3/output/comparison_report.md"
    
    manual_records= read_csv_manual(sys.argv[1])
    manual_records = convert_types(manual_records)
    manual_summary_dict = calculate_summary(manual_records)
    write_json(manual_summary_dict,manual_output)

    pandas_df = read_csv_pandas(sys.argv[1])
    pandas_summary = calculate_summary_pandas(pandas_df)
    write_json(pandas_summary, pandas_output)

    write_comparison_report(manual_summary_dict, pandas_summary, report_output)


def write_comparison_report(manual_summary: dict, pandas_summary: dict, output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    report = "# Comparison Report\n\n"

    if manual_summary == pandas_summary:
        report += (
            "## Result\n\n"
            "PASS\n\n"
            "Both the manual parser and the pandas parser produced identical summaries.\n"
            "No differences were found.\n"
        )
    else:
        report += (
            "## Result\n\n"
            "FAIL\n\n"
            "The manual parser and pandas parser produced different summaries.\n\n"
            "## Differences\n\n"
        )

        for key in manual_summary:
            if manual_summary[key] != pandas_summary[key]:
                report += (
                    f"### {key}\n"
                    f"- Manual: {manual_summary[key]}\n"
                    f"- Pandas: {pandas_summary[key]}\n\n"
                )

    with open(path, "w", encoding="utf-8") as file:
        file.write(report)

    print(f"Comparison report written to {path}")



if __name__ == "__main__":
    main()