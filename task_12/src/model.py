from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

from preprocessing import create_preprocessor


def create_model_pipeline():
    preprocessor = create_preprocessor()

    model = RandomForestClassifier( n_estimators=200, random_state=42)

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    return pipeline