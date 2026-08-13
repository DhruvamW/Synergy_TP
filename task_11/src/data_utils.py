import pandas as pd
from config import TARGET_COLUMN


def load_data(filepath):
    df = pd.read_csv(filepath)

    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    return X, y