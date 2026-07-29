import pandas as pd

def load_classification_dataset(filepath):
    heart_df=pd.read_csv(filepath)
    target_heart= "has_heart_disease"
    x_heart= heart_df.drop(columns=[target_heart, "patient_id"])
    y_heart= heart_df[target_heart]
    return x_heart, y_heart

def load_regression_dataset(filepath):
    oil_df=pd.read_csv(filepath)
    target_oil= "value_sales"
    x_oil= oil_df.drop(columns=[target_oil])
    y_oil= oil_df[target_oil]
    return x_oil, y_oil