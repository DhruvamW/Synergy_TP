import sys
from pathlib import Path

import joblib
import pandas as pd

from data_utils import load_data
from preprocessing import split_data

from models import (
    create_dummy_classifier,
    create_logistic_regression,
    create_knn,
    create_decision_tree,
    create_random_forest
)

from metrics import (
    calculate_metrics,
    get_classification_report,
    get_confusion_matrix
)

from visualisation import (
    plot_class_distribution,
    plot_confusion_matrix,
    plot_model_comparison,
    plot_train_validation_scores
)

from config import RANDOM_STATE


def train_and_evaluate_model(model, X_train, y_train, X_val, y_val):

    model.fit(X_train, y_train)

    train_predictions = model.predict(X_train)
    validation_predictions = model.predict(X_val)

    train_metrics = calculate_metrics(y_train, train_predictions)

    validation_metrics = calculate_metrics(y_val, validation_predictions)

    return (
        model,
        train_predictions,
        validation_predictions,
        train_metrics,
        validation_metrics
    )


def save_classification_report(model_name, y_true, y_pred, output_dir):

    report = get_classification_report(y_true, y_pred)

    report_path = (output_dir / f"{model_name}_classification_report.txt")

    with open(report_path, "w") as file:
        file.write(report)


def save_misclassified_samples(X, y_true, y_pred, model_name, output_dir):

    misclassified = X.copy()

    misclassified["actual_label"] = y_true.values
    misclassified["predicted_label"] = y_pred

    misclassified = misclassified[misclassified["actual_label"] != misclassified["predicted_label"]]

    output_path = ( output_dir / f"{model_name}_misclassified.csv")

    misclassified.to_csv( output_path, index=False)


def main():

    if len(sys.argv) != 3:
        print(
            "Usage: python main.py "
            "<input_csv> <output_dir>"
        )
        return

    csv_path = sys.argv[1]
    output_dir = Path(sys.argv[2])

    figures_dir = output_dir / "figures"
    metrics_dir = output_dir / "metrics"
    model_dir = output_dir / "model"

    figures_dir.mkdir(parents=True, exist_ok=True)

    metrics_dir.mkdir( parents=True, exist_ok=True)

    model_dir.mkdir(parents=True, exist_ok=True)


    print("Loading dataset...")

    X, y = load_data(csv_path)

    print(f"Dataset shape: {X.shape}")


    plot_class_distribution(y, figures_dir / "class_distribution.png")



    print("\nSplitting dataset...")

    (X_train, X_val, X_test, y_train, y_val, y_test) = split_data(X, y)

    print(f"Training samples   : {len(X_train)}")
    print(f"Validation samples : {len(X_val)}")
    print(f"Testing samples    : {len(X_test)}")



    models = {
        "Dummy": create_dummy_classifier(),
        "Logistic Regression": create_logistic_regression(),
        "KNN": create_knn(),
        "Decision Tree": create_decision_tree(),
        "Random Forest": create_random_forest()
    }



    validation_results = {}
    training_validation_results = {}

    trained_models = {}
    validation_predictions = {}

    class_names = sorted(y.unique())

    for model_name, model in models.items():

        print(f"\nTraining {model_name}...")

        (trained_model, train_predictions, val_predictions, train_metrics, val_metrics) = train_and_evaluate_model(model, X_train, y_train, X_val, y_val)

        trained_models[model_name] = trained_model

        validation_predictions[model_name] = val_predictions

        validation_results[model_name] = val_metrics

        training_validation_results[model_name] = {
            "train_accuracy":
                train_metrics["accuracy"],

            "validation_accuracy":
                val_metrics["accuracy"]
        }

        print(
            f"Validation Accuracy: "
            f"{val_metrics['accuracy']:.4f}"
        )

        print(
            f"Validation Precision: "
            f"{val_metrics['precision']:.4f}"
        )

        print(
            f"Validation Recall: "
            f"{val_metrics['recall']:.4f}"
        )

        print(
            f"Validation F1: "
            f"{val_metrics['f1_score']:.4f}"
        )

        # Confusion matrix
        cm = get_confusion_matrix(
            y_val,
            val_predictions
        )

        plot_confusion_matrix(
            cm,
            class_names,
            model_name,
            figures_dir /
            f"confusion_matrix_{model_name.lower().replace(' ', '_')}.png"
        )

        # Classification report
        save_classification_report(
            model_name.lower().replace(" ", "_"),
            y_val,
            val_predictions,
            metrics_dir
        )

        # Misclassified samples
        save_misclassified_samples(
            X_val,
            y_val,
            val_predictions,
            model_name.lower().replace(" ", "_"),
            metrics_dir
        )

   

    results_df = pd.DataFrame(
        validation_results
    ).T

    results_df.index.name = "model"

    results_df.to_csv(
        metrics_dir /
        "model_comparison.csv"
    )

    print("\nModel Comparison:")
    print(results_df)

 

    plot_train_validation_scores(
        training_validation_results,
        figures_dir /
        "train_validation_accuracy.png"
    )



    plot_model_comparison(
        validation_results,
        figures_dir /
        "model_comparison.png"
    )

 

    best_model_name = max(
        validation_results,
        key=lambda model:
        validation_results[model]["f1_score"]
    )

    final_model = trained_models[
        best_model_name
    ]

    print(
        f"\nSelected final model: "
        f"{best_model_name}"
    )



    print("\nEvaluating final model on test set...")

    test_predictions = final_model.predict(X_test)

    test_metrics = calculate_metrics(
        y_test,
        test_predictions
    )

    print("\nFinal Test Results:")

    for metric, value in test_metrics.items():
        print(
            f"{metric}: {value:.4f}"
        )

    # Save final test metrics
    test_results = pd.DataFrame(
        [test_metrics]
    )

    test_results.to_csv(
        metrics_dir /
        "final_test_metrics.csv",
        index=False
    )

    # Final confusion matrix
    test_cm = get_confusion_matrix(
        y_test,
        test_predictions
    )

    plot_confusion_matrix(
        test_cm,
        class_names,
        f"{best_model_name} - Test",
        figures_dir /
        "final_confusion_matrix.png"
    )

    # Final classification report
    final_report = get_classification_report(
        y_test,
        test_predictions
    )

    with open(
        metrics_dir /
        "final_classification_report.txt",
        "w"
    ) as file:
        file.write(final_report)

    # Final misclassified samples
    save_misclassified_samples(
        X_test,
        y_test,
        test_predictions,
        "final_model",
        metrics_dir
    )



    model_path = (
        model_dir /
        "crop_classifier.joblib"
    )

    joblib.dump(
        final_model,
        model_path
    )

    print(
        f"\nFinal model saved to: "
        f"{model_path}"
    )

    print("\nExperiment completed successfully.")


if __name__ == "__main__":
    main()