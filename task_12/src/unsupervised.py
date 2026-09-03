import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


UNSUPERVISED_FEATURES = [
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


def prepare_unsupervised_data(df):

    X = df[UNSUPERVISED_FEATURES].copy()

    imputer = SimpleImputer(strategy="median")
    scaler = StandardScaler()

    X_imputed = imputer.fit_transform(X)

    X_scaled = scaler.fit_transform(X_imputed)

    return X_scaled


def run_kmeans(X, k):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X)

    return model, labels


def evaluate_k_values(X, k_values):
    results = []

    for k in k_values:
        model, labels = run_kmeans(X, k)
        score = silhouette_score(X, labels)
        results.append({
            "k": k,
            "silhouette_score": score
        })

    return pd.DataFrame(results)