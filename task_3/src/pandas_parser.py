import pandas as pd
import json
from pathlib import Path

def read_csv_pandas(file_path: str):
    df= pd.read_csv(file_path)
    df["score"] = df["score"].astype(int)
    df["submitted"]=df["submitted"].map({"yes":True,"no":False})
    return df

def calculate_summary_pandas(df) -> dict:
    total_students = len(df)
    avg_score= float(df["score"].mean())
    highest_score = int(df["score"].max())
    submitted_students = int(df["submitted"].sum())
    missing_submissions =  total_students - submitted_students
    submitted = df[df["submitted"]]
    lowest_score = int(submitted["score"].min())
    highest_scorer = df.loc[df["score"].idxmax(),"name"]
    lowest_scorer= df.loc[submitted["score"].idxmin(), "name"]
    domain_wise_avg= df.groupby("domain")["score"].mean().to_dict()
    not_submitted_students = df[df["submitted"] == False]["name"].tolist()
    below_five = df[df["score"]<5]["name"].tolist()
    total_score = int(df["score"].sum())

    summary = {
          "total score" : total_score,
          "total students" : total_students,
          "highest score" : highest_score,
          "highest scorer" : highest_scorer,
          "lowest score" : lowest_score,
          "lowest scorer" : lowest_scorer,
          "avg score" : avg_score,
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
