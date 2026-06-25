import csv
from pathlib import Path
import json

def read_submissions(file_path: str) -> list[dict]:
    students=[]

    try:
        with open(file_path) as file:
            #print("Opened successfully")
            reader = csv.DictReader(file)
            #print(reader.fieldnames)

            for row in reader:
                try:
                    row["score"]=int(row["score"])
                except ValueError:
                    print(f"Invalid score for {row['name']}")
                    continue
                students.append(row)
                
    except FileNotFoundError:
        print("Input file not found.")
        return []
    
    if not students:
        print("CSV file is empty.")
    
    return students
    

def get_submitted_students(students: list[dict]) -> list[str]:
    submitted_students=[]
    for record in students:
        if record["submitted"]=="yes":
            name=record["name"]
            submitted_students.append(name)
    return submitted_students

def calculate_average_score(students: list[dict]) -> float:
    total_score=0
    total_students=0
    for record in students:
        if record["submitted"]=="yes":
            total_students+=1
            try:
                total_score+= record["score"]
            except ValueError:
                print("Invalid Score Value")
    if total_students == 0:
        return 0
    average_score= total_score / total_students
    return average_score

def get_domain_wise_average(students: list[dict]) -> dict[str,float]:
    domain_wise_scores={}
    domain_wise_count={}
    domain_wise_avg={}
    for record in students:
        if record["submitted"] == "yes":
            domain=record["domain"]
            domain_wise_scores[domain]= domain_wise_scores.get(domain,0)+record["score"]
            domain_wise_count[domain]= domain_wise_count.get(domain,0)+1
    for domain in domain_wise_scores:
        domain_wise_avg[domain]= domain_wise_scores[domain] / domain_wise_count[domain]
    return domain_wise_avg



def get_missing_submissions(students: list[dict]) -> list[str]:
    missing_submissions=[]
    for record in students:
        if record["submitted"]=="no":
            name=record["name"]
            missing_submissions.append(name)
    return missing_submissions

def get_highest_scorer(students: list[dict]) -> dict[str,int]:
    highest_scorer= None
    highest_score = 0
    for record in students:
        if record["submitted"]=="yes":
            if record["score"]>highest_score:
                highest_score = record["score"]
                highest_scorer = record["name"]
    if highest_scorer is None:
        return {}
    return {highest_scorer:highest_score}

def get_lowest_scorer(students: list[dict]) -> dict[str,int]:
    lowest_scorer= None
    lowest_score = float("inf")
    for record in students:
        if record["submitted"]=="yes":
            if record["score"] < lowest_score:
                lowest_score = record["score"]
                lowest_scorer = record["name"]
    if lowest_scorer is None:
        return {}
    return {lowest_scorer:lowest_score}

def get_students_below_five(students: list[dict]) -> list[str]:
    students_below_five = []
    for record in students:
        if record["submitted"]=="yes":
            if record["score"] < 5:
                students_below_five.append(record["name"])
    return students_below_five

def write_summary(summary: dict, output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(path, "w") as file:
            json.dump(summary, file, indent=4)
        print(f"Summary written to {path}")
    except OSError:
        print("Python can't create file")

