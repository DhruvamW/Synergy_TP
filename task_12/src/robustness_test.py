import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix


def run_robustness_test(
    model,
    X_test,
    y_test,
    stressed_feature="NDVI_index"
):
    """
    Evaluate a trained model under a missing-feature stress condition.

    The model is NOT retrained. The specified feature is set to
    missing values in the evaluation data only.
    """

    # Normal test evaluation
    normal_predictions = model.predict(X_test)

    normal_accuracy = accuracy_score(
        y_test,
        normal_predictions
    )

    normal_f1 = f1_score(
        y_test,
        normal_predictions,
        average="macro"
    )

    # Create stressed copy
    X_stressed = X_test.copy()

    # Simulate sensor/feature failure
    X_stressed[stressed_feature] = np.nan

    # Prediction using the original trained model
    stressed_predictions = model.predict(X_stressed)

    stressed_accuracy = accuracy_score(
        y_test,
        stressed_predictions
    )

    stressed_f1 = f1_score(
        y_test,
        stressed_predictions,
        average="macro"
    )

    return {
        "normal_predictions": normal_predictions,
        "stressed_predictions": stressed_predictions,
        "normal_accuracy": normal_accuracy,
        "stressed_accuracy": stressed_accuracy,
        "normal_f1": normal_f1,
        "stressed_f1": stressed_f1,
        "normal_confusion_matrix": confusion_matrix(
            y_test,
            normal_predictions
        ),
        "stressed_confusion_matrix": confusion_matrix(
            y_test,
            stressed_predictions
        )
    }