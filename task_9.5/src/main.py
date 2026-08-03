import os
import sys

from data_utils import load_regression_dataset, load_classification_dataset
from split import train_val_test_split
from data_preprocessing import encode_categorical, standardize_features

from linear_regression import LinearRegression
from logistic_regression import LogisticRegression

from baselines import regression_baseline, classification_baseline

from metrics import (
    mean_squared_error,
    root_mean_squared_error,
    mean_absolute_error,
    r2_score,
    accuracy,
    precision,
    recall,
    f1_score,
    confusion_matrix
)

from utils import ensure_directory, save_metrics, print_results

from vizualization import (
    plot_training_loss,
    plot_regression_predictions,
    plot_confusion_matrix
)


def regression_workflow(dataset_path, output_dir):

    print("\n========== REGRESSION ==========")

    X, y = load_regression_dataset(dataset_path)

    X_train, X_val, X_test, y_train, y_val, y_test = train_val_test_split(X, y)

    X_train, X_val, X_test = encode_categorical(X_train, X_val, X_test)

    X_train, X_val, X_test, _, _ = standardize_features(X_train, X_val, X_test)

    model = LinearRegression( learning_rate=0.01, epochs=1000)

    model.fit(X_train.values, y_train.values)

    predictions = model.predict(X_test.values)

    metrics = {
        "MSE": mean_squared_error(y_test.values, predictions),
        "RMSE": root_mean_squared_error(y_test.values, predictions),
        "MAE": mean_absolute_error(y_test.values, predictions),
        "R2": r2_score(y_test.values, predictions)
    }

    print_results("Linear Regression", metrics)

    save_metrics( metrics, os.path.join(output_dir, "regression_metrics.json"))

    plot_training_loss( model.loss_history, "Linear Regression Loss", os.path.join(output_dir, "linear_loss.png"))

    plot_regression_predictions( y_test.values, predictions, os.path.join(output_dir, "regression_predictions.png"))

    baseline_predictions = regression_baseline( y_train.values, X_test)

    baseline_metrics = {
        "MSE": mean_squared_error(y_test.values, baseline_predictions),
        "RMSE": root_mean_squared_error(y_test.values, baseline_predictions),
        "MAE": mean_absolute_error(y_test.values, baseline_predictions),
        "R2": r2_score(y_test.values, baseline_predictions)
    }

    print_results("Regression Baseline", baseline_metrics)

    save_metrics( baseline_metrics, os.path.join(output_dir, "regression_baseline_metrics.json"))


def classification_workflow(dataset_path, output_dir):

    print("\n========== CLASSIFICATION ==========")

    X, y = load_classification_dataset(dataset_path)

    X_train, X_val, X_test, y_train, y_val, y_test = train_val_test_split( X, y)

    X_train, X_val, X_test = encode_categorical( X_train, X_val, X_test)

    X_train, X_val, X_test, _, _ = standardize_features( X_train, X_val, X_test)

    model = LogisticRegression( learning_rate=0.01, epochs=1000)

    model.fit(X_train.values, y_train.values)

    predictions = model.predict(X_test.values)

    metrics = {
        "Accuracy": accuracy(y_test.values, predictions),
        "Precision": precision(y_test.values, predictions),
        "Recall": recall(y_test.values, predictions),
        "F1": f1_score(y_test.values, predictions)
    }

    print_results("Logistic Regression", metrics)

    save_metrics( metrics, os.path.join(output_dir, "classification_metrics.json"))

    plot_training_loss( model.loss_history, "Logistic Regression Loss", os.path.join(output_dir, "logistic_loss.png"))

    cm = confusion_matrix(y_test.values, predictions)

    plot_confusion_matrix( cm, os.path.join(output_dir, "confusion_matrix.png"))

    baseline_predictions = classification_baseline( y_train.values, X_test)

    baseline_metrics = {
        "Accuracy": accuracy(y_test.values, baseline_predictions),
        "Precision": precision(y_test.values, baseline_predictions),
        "Recall": recall(y_test.values, baseline_predictions),
        "F1": f1_score(y_test.values, baseline_predictions)
    }

    print_results("Classification Baseline", baseline_metrics)

    save_metrics( baseline_metrics, os.path.join(output_dir, "classification_baseline_metrics.json"))


def main():

    if len(sys.argv) != 4:
        print(
            "Usage: python main.py <regression_csv> <classification_csv> <output_dir>"
        )
        return

    regression_dataset = sys.argv[1]
    classification_dataset = sys.argv[2]
    output_dir = sys.argv[3]

    ensure_directory(output_dir)

    regression_workflow( regression_dataset, output_dir)

    classification_workflow( classification_dataset, output_dir)

    print("\nDone.")


if __name__ == "__main__":
    main()