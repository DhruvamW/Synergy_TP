import pandas as pd

from data_loader import load_data
from model import create_model_pipeline, create_dummy_pipeline
from splits import random_split, leave_one_region_out
from evaluate import evaluate_model
from robustness_test import run_robustness_test


DATA_PATH = r"data\Smart_Farming_Crop_Yield_2024.csv"

FEATURES = [
    "crop_type",
    "soil_moisture_%",
    "soil_pH",
    "temperature_C",
    "rainfall_mm",
    "humidity_%",
    "sunlight_hours",
    "irrigation_type",
    "fertilizer_type",
    "pesticide_usage_ml",
    "sowing_date",
    "NDVI_index",
    "latitude",
    "longitude"
]

SEEDS = [42, 43, 44, 45, 46]


def run_random_experiment(df, seed):

    train, validation, test = random_split(
        df,
        random_state=seed
    )

    X_train = train[FEATURES]
    y_train = train["crop_disease_status"]

    X_val = validation[FEATURES]
    y_val = validation["crop_disease_status"]

    X_test = test[FEATURES]
    y_test = test["crop_disease_status"]

    model = create_model_pipeline()

    model.fit(X_train, y_train)

    train_results = evaluate_model(
        model,
        X_train,
        y_train
    )

    val_results = evaluate_model(
        model,
        X_val,
        y_val
    )

    test_results = evaluate_model(
        model,
        X_test,
        y_test
    )

    return {
        "seed": seed,
        "train_accuracy": train_results["accuracy"],
        "validation_accuracy": val_results["accuracy"],
        "test_accuracy": test_results["accuracy"],
        "test_f1_macro": test_results["f1_macro"]
    }


def main():

    df = load_data(DATA_PATH)

    # Keep only labelled observations
    df = df.dropna(
        subset=["crop_disease_status"]
    ).copy()

    results = []

    for seed in SEEDS:

        result = run_random_experiment(
            df,
            seed
        )

        results.append(result)

    results_df = pd.DataFrame(results)

    print("\n" + "=" * 60)
    print("REPEATED STRATIFIED RANDOM EVALUATION")
    print("=" * 60)

    print(results_df.to_string(index=False))

    print("\nMean:")
    print(results_df.mean(numeric_only=True))

    print("\nStandard deviation:")
    print(results_df.std(numeric_only=True))

    # ============================================================
    # PART 4 - ROBUSTNESS STRESS TEST
    # ============================================================

    print("\n" + "=" * 60)
    print("ROBUSTNESS STRESS TEST")
    print("=" * 60)

    # Use seed 42 as the controlled baseline
    train, validation, test = random_split(
        df,
        random_state=42
    )

    X_train = train[FEATURES]
    y_train = train["crop_disease_status"]

    X_test = test[FEATURES]
    y_test = test["crop_disease_status"]

    # Train normally
    model = create_model_pipeline()

    model.fit(
        X_train,
        y_train
    )

    # Run robustness test
    robustness_results = run_robustness_test(
        model,
        X_test,
        y_test,
        stressed_feature="NDVI_index"
    )

    print("\nStress condition:")
    print("NDVI_index unavailable during evaluation")

    print("\nNormal test performance:")
    print(
        f"Accuracy: "
        f"{robustness_results['normal_accuracy']:.4f}"
    )

    print(
        f"Macro F1: "
        f"{robustness_results['normal_f1']:.4f}"
    )

    print("\nStressed test performance:")
    print(
        f"Accuracy: "
        f"{robustness_results['stressed_accuracy']:.4f}"
    )

    print(
        f"Macro F1: "
        f"{robustness_results['stressed_f1']:.4f}"
    )

    accuracy_change = (
        robustness_results["stressed_accuracy"]
        - robustness_results["normal_accuracy"]
    )

    f1_change = (
        robustness_results["stressed_f1"]
        - robustness_results["normal_f1"]
    )

    print("\nPerformance change:")
    print(
        f"Accuracy change: {accuracy_change:+.4f}"
    )

    print(
        f"Macro F1 change: {f1_change:+.4f}"
    )

    print("\nNormal confusion matrix:")
    print(
        robustness_results["normal_confusion_matrix"]
    )

    print("\nStressed confusion matrix:")
    print(
        robustness_results["stressed_confusion_matrix"]
    )


if __name__ == "__main__":
    main()