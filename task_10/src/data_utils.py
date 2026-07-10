import pandas as pd
import numpy as np


def load_data(file_path):
    df = pd.read_csv(file_path, sep=";", decimal=",")

    # Remove unwanted empty columns
    df = df.loc[:, ~df.columns.str.contains("Unnamed")]

    # Replace missing value indicator
    df.replace(-200, np.nan, inplace=True)

    return df


def clean_data(df):
    df = df.drop_duplicates()

    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].median())

    return df


def create_classification_target(df):
    threshold = df["CO(GT)"].median()

    df["HighPollution"] = 0

    df.loc[df["CO(GT)"] >= threshold, "HighPollution"] = 1

    return df


def train_test_split(X, y, test_size=0.2):

    np.random.seed(42)

    indices = np.random.permutation(len(X))

    split = int(len(X) * (1 - test_size))

    train_index = indices[:split]
    test_index = indices[split:]

    X_train = X.iloc[train_index]
    X_test = X.iloc[test_index]

    y_train = y.iloc[train_index]
    y_test = y.iloc[test_index]

    return X_train, X_test, y_train, y_test


def standardize_data(X_train, X_test):
    mean = X_train.mean()

    std = X_train.std()

    X_train = (X_train - mean) / std

    X_test = (X_test - mean) / std

    return X_train, X_test


def get_regression_data(df):
    features = [
        "PT08.S1(CO)",
        "NMHC(GT)",
        "C6H6(GT)",
        "PT08.S2(NMHC)",
        "NOx(GT)",
        "PT08.S3(NOx)",
        "NO2(GT)",
        "PT08.S4(NO2)",
        "PT08.S5(O3)",
        "T",
        "RH",
        "AH"
    ]

    X = df[features]

    y = df["CO(GT)"]

    return X, y


def get_classification_data(df):
    features = [
        "PT08.S1(CO)",
        "NMHC(GT)",
        "C6H6(GT)",
        "PT08.S2(NMHC)",
        "NOx(GT)",
        "PT08.S3(NOx)",
        "NO2(GT)",
        "PT08.S4(NO2)",
        "PT08.S5(O3)",
        "T",
        "RH",
        "AH"
    ]

    X = df[features]

    y = df["HighPollution"]

    return X, y


def get_clustering_data(df):
    features = [
        "CO(GT)",
        "NOx(GT)",
        "NO2(GT)",
        "C6H6(GT)",
        "T",
        "RH",
        "AH"
    ]

    return df[features]