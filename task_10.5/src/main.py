import os
import sys
import pandas as pd

from data_utils import load_data, split_data
from models import (
    train_dummy,
    train_linear,
    train_ridge,
    train_decision_tree,
    train_random_forest,
)
from evaluation import (
    evaluate_model,
    largest_errors
)
from visualisation import (
    plot_actual_vs_predicted,
    plot_residuals,
)


def main():

    if len(sys.argv) != 3:
        print("Usage: python src/main.py <input_csv> <output_directory>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = sys.argv[2]

    os.makedirs(output_dir, exist_ok=True)

    print("Loading dataset...")
    X, y = load_data(input_file)

    print("Splitting dataset...")
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(X, y)

    models = {
        "Dummy": train_dummy(X_train, y_train),
        "Linear Regression": train_linear(X_train, y_train),
        "Ridge Regression": train_ridge(X_train, y_train),
        "Decision Tree": train_decision_tree(X_train, y_train),
        "Random Forest": train_random_forest(X_train, y_train),
    }

    results = {}

    print("\nEvaluating models...\n")

    for name, model in models.items():

        train_metrics = evaluate_model(model, X_train, y_train)
        val_metrics = evaluate_model(model, X_val, y_val)

        results[name] = {
            "Train MAE": train_metrics["MAE"],
            "Validation MAE": val_metrics["MAE"],
            "Train MSE": train_metrics["MSE"],
            "Validation MSE": val_metrics["MSE"],
            "Train RMSE": train_metrics["RMSE"],
            "Validation RMSE": val_metrics["RMSE"],
            "Train R2": train_metrics["R2"],
            "Validation R2": val_metrics["R2"],
        }

    comparison_df = pd.DataFrame(results).T

    print(comparison_df)

    comparison_df.to_csv(os.path.join(output_dir, "model_comparison.csv"))

    baseline_rmse = results["Dummy"]["Validation RMSE"]

    print("\nComparison Against Dummy Baseline")

    for model_name, metrics in results.items():

        if model_name == "Dummy":
            continue

        improvement = baseline_rmse - metrics["Validation RMSE"]

        print(
            f"{model_name}: "
            f"Validation RMSE = {metrics['Validation RMSE']:.4f}, "
            f"Improvement = {improvement:.4f}"
        )

    candidate_models = [
    "Linear Regression",
    "Ridge Regression",
    "Decision Tree",
    "Random Forest"]
    best_model_name = max( candidate_models, key=lambda model: results[model]["Validation R2"])
    print(f"\nBest Model: {best_model_name}")
    final_model = models[best_model_name]
    y_pred = final_model.predict(X_test)

    plot_actual_vs_predicted(
        y_test,
        y_pred,
        os.path.join(output_dir, "actual_vs_predicted.png"),
    )

    plot_residuals(
        y_test,
        y_pred,
        os.path.join(output_dir, "residual_plot.png"),
    )

    error_df = largest_errors(final_model, X_test, y_test)
    error_df.to_csv( os.path.join(output_dir, "largest_errors.csv"), index=False)

    print("\nFinished successfully!")


if __name__ == "__main__":
    main()