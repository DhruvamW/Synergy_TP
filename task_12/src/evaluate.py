from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


def evaluate_model(model, X, y):
    predictions = model.predict(X)

    return {
        "accuracy": accuracy_score(y, predictions),
        "precision_macro": precision_score(
            y,
            predictions,
            average="macro",
            zero_division=0
        ),
        "recall_macro": recall_score(
            y,
            predictions,
            average="macro",
            zero_division=0
        ),
        "f1_macro": f1_score(
            y,
            predictions,
            average="macro",
            zero_division=0
        ),
        "confusion_matrix": confusion_matrix(
            y,
            predictions
        )
    }