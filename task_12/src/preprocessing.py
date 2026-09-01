import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def create_preprocessor():
    numeric_features = [
        "soil_moisture_%",
        "soil_pH",
        "temperature_C",
        "rainfall_mm",
        "humidity_%",
        "sunlight_hours",
        "pesticide_usage_ml",
        "NDVI_index",
        "latitude",
        "longitude"
    ]

    categorical_features = [
        "crop_type",
        "irrigation_type",
        "fertilizer_type"
    ]

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median"))
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer([
        ("numeric", numeric_pipeline, numeric_features),
        ("categorical", categorical_pipeline, categorical_features)
    ])

    return preprocessor 