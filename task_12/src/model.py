from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.dummy import DummyClassifier

from preprocessing import create_preprocessor


def create_model_pipeline():
    preprocessor = create_preprocessor()

    model = RandomForestClassifier( n_estimators=200, max_depth= 8, min_samples_leaf=5, random_state=42)

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    return pipeline

def create_dummy_pipeline():
    preprocessor = create_preprocessor()

    model = DummyClassifier(
        strategy="most_frequent"
    )

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    return pipeline