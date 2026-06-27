from pathlib import Path
import json

def read_csv_manual(file_path: str) -> list[dict]:
    students_dict=[] #list of dictionaries
    with open(file_path) as file:
        header = next(file).strip()
        header = header.split(",")
        for record in file:
            record = record.strip()
            if not record:
                continue
            record = record.split(",")
            if len(record) != len(header):
                 print("Invalid Record!!")
                 continue
            student={}
            for i in range (len(header)):
                 student[header[i]]=record[i]
            students_dict.append(student)
        #print(students_dict)
        
    return students_dict


def convert_types(students: list[dict]) -> list[dict]:
     for record in students:
                 try:
                    record["score"] = int(record["score"])
                 except ValueError:
                      print("Invalid Score!!")
                      continue
                 if record["submitted"].lower()== "yes":
                      record["submitted"] = True
                 elif record["submitted"].lower() == "no":
                      record["submitted"] = False
     return students

def calculate_summary(students: list[dict]) -> dict:
     total_score = 0
     total_records = 0
     highest_score = float("-inf")
     submitted_students = 0
     missing_submissions=0
     highest_scorer = None
     lowest_score = float("inf")
     lowest_scorer = None
     domain_wise_avg = {}
     domain_wise_scores={}
     domain_wise_count={}
     not_submitted_students = []
     below_five = []
     for record in students:
          total_records += 1
          total_score += record["score"]
          if record["score"] > highest_score:
               highest_score = record["score"]
               highest_scorer = record["name"]
          if record["submitted"]:
               submitted_students += 1
               if record["score"] < lowest_score:
                lowest_score = record["score"]
                lowest_scorer = record["name"]
          else:
               missing_submissions += 1
               not_submitted_students.append(record["name"])
          if record["score"] < 5:
               below_five.append(record["name"])
          domain_wise_scores[record["domain"]] = domain_wise_scores.get(record["domain"],0) + record["score"]
          domain_wise_count[record["domain"]] = domain_wise_count.get(record["domain"],0) + 1

     for domain in domain_wise_scores:
          domain_wise_avg[domain]= domain_wise_scores[domain] / domain_wise_count[domain]
     
     summary = {
          "total score" : total_score,
          "total students" : total_records,
          "highest score" : highest_score,
          "highest scorer" : highest_scorer,
          "lowest score" : lowest_score,
          "lowest scorer" : lowest_scorer,
          "avg score" : total_score/total_records,
          "number of submitted students" : submitted_students,
          "number of missing submissions" : missing_submissions,
          "students who did not submit" : not_submitted_students,
          "students scoring below five" : below_five,
          "domain wise avg" : domain_wise_avg
     }

     return summary
          
def write_json(summary: dict, output_path: str) -> None:
     path = Path(output_path)
     path.parent.mkdir(parents=True, exist_ok=True)
     try:
        with open(path, "w") as file:
            json.dump(summary, file, indent=4)
        print(f"Summary written to {path}")
     except OSError as e:
        print(f"Error writing JSON: {e}")
     
          

                