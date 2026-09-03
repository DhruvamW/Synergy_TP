import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest


ANOMALY_FEATURES = [
    "soil_moisture_%",
    "soil_pH",
    "temperature_C",
    "rainfall_mm",
    "humidity_%",
    "sunlight_hours",
    "pesticide_usage_ml",
    "total_days",
    "latitude",
    "longitude",
    "NDVI_index"
]


def prepare_anomaly_data(df):
    X = df[ANOMALY_FEATURES].copy()

    imputer = SimpleImputer(strategy="median")
    scaler = StandardScaler()

    X_imputed = imputer.fit_transform(X)
    X_scaled = scaler.fit_transform(X_imputed)

    return X_scaled


def run_isolation_forest(X, contamination=0.05):
    model = IsolationForest(
        n_estimators=200,
        contamination=contamination,
        random_state=42
    )

    predictions = model.fit_predict(X)
    scores = model.decision_function(X)

    return model, predictions, scores