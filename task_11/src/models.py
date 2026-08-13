from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def create_dummy_classifier():

    return DummyClassifier(
        strategy="most_frequent"
    )


def create_logistic_regression():

    return Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(
            max_iter=1000,
            random_state=42
        ))
    ])


def create_knn():

    return Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", KNeighborsClassifier(
            n_neighbors=5
        ))
    ])


def create_decision_tree():

    return DecisionTreeClassifier(
        random_state=42
    )


def create_random_forest():

    return RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )