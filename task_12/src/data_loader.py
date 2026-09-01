import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def prepare_supervised_data(df):
    df = df.dropna(subset=['crop_disease_status'])