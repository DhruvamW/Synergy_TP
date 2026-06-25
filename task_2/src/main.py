import sys
from analyzer import *

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_csv> <output_json>")
        return
    input_file=sys.argv[1]
    output_file= sys.argv[2]

    students= read_submissions(input_file)
    submitted_students= get_submitted_students(students)
    total_students= len(students)
    submitted_count=len(submitted_students)
    missing_students= get_missing_submissions(students)
    missing_count=len(missing_students)
    avg_score= calculate_average_score(students)
    domain_wise_avg = get_domain_wise_average(students)
    highest_scorer = get_highest_scorer(students)
    lowest_scorer = get_lowest_scorer(students)
    students_below_five =  get_students_below_five(students)

    summary = {
        "total students" : total_students,
        "submitted students" : submitted_students,
        "submitted count": submitted_count,
        "missing students" : missing_students,
        "missing count" : missing_count,
        "average score" : avg_score,
        "domain wise average" : domain_wise_avg,
        "highest scorer" : list(highest_scorer)[0],
        "highest score" : list(highest_scorer.values())[0],
        "lowest scorer" : list(lowest_scorer)[0],
        "lowest score" : list(lowest_scorer.values())[0],
        "students below five" : students_below_five
    }

    print(f"Total Students: {total_students}")
    print(f"Submitted Count: {submitted_count}")
    print(f"Missing Count: {missing_count}")
    print(f"Average Score: {avg_score:.2f}")
    print(f"Highest Scorer: {list(highest_scorer)[0]} ({list(highest_scorer.values())[0]})")
    print(f"Lowest Scorer: {list(lowest_scorer)[0]} ({list(lowest_scorer.values())[0]})")
    print(f"Domain-wise Average: {domain_wise_avg}")
    print(f"Missing Submissions: {missing_students}")
    print(f"Students Scoring Below 5: {students_below_five}")
    print(f"Summary written to {output_file}")

    write_summary(summary, output_file)


if __name__ == "__main__":
    main()

