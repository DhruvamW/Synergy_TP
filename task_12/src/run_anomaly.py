import pandas as pd

from data_loader import load_data
from anomaly_detection import (
    prepare_anomaly_data,
    run_isolation_forest
)


DATA_PATH = r"Synergy_TP\task_12\data\Smart_Farming_Crop_Yield_2024.csv"   


def main():

    print("=" * 60)
    print("ISOLATION FOREST ANOMALY DETECTION")
    print("=" * 60)

    df = load_data(DATA_PATH)

    print("Total observations:", len(df))

    X = prepare_anomaly_data(df)

    model, predictions, scores = run_isolation_forest(
        X,
        contamination=0.05
    )

    df["anomaly_prediction"] = predictions
    df["anomaly_score"] = scores

    df["anomaly"] = df["anomaly_prediction"].map({
        1: "Normal",
        -1: "Anomaly"
    })

    print("\nAnomaly distribution:")
    print(df["anomaly"].value_counts())

    print("\nAnomaly percentage:")
    print(
        (df["anomaly"].value_counts(normalize=True) * 100)
        .round(2)
    )

    print("\nMost anomalous observations:")

    print(
        df[
            [
                "farm_id",
                "region",
                "crop_type",
                "soil_moisture_%",
                "temperature_C",
                "rainfall_mm",
                "pesticide_usage_ml",
                "NDVI_index",
                "anomaly_score"
            ]
        ]
        .sort_values("anomaly_score")
        .head(10)
        .to_string(index=False)
    )

    print("\nAnomalies by region:")
    print(
        pd.crosstab(
            df["region"],
            df["anomaly"],
            normalize="index"
        ).round(3)
    )

    print("\nAnomalies by crop:")
    print(
        pd.crosstab(
            df["crop_type"],
            df["anomaly"],
            normalize="index"
        ).round(3)
    )

    print("\nAnomalies by disease status:")
    print(
        pd.crosstab(
            df["crop_disease_status"],
            df["anomaly"],
            normalize="index"
        ).round(3)
    )

    print("\n" + "=" * 60)
    print("CONTAMINATION SENSITIVITY")
    print("=" * 60)

    for contamination in [0.02, 0.05, 0.10]:
        model, predictions, scores = run_isolation_forest(
            X,
            contamination=contamination
        )

        anomaly_count = (predictions == -1).sum()

        print(
            f"contamination={contamination:.2f} "
            f"-> anomalies={anomaly_count} "
            f"({anomaly_count / len(df) * 100:.1f}%)"
        )


if __name__ == "__main__":
    main()