from data_loader import load_data
from unsupervised import (
    prepare_unsupervised_data,
    evaluate_k_values,
    run_kmeans,
    UNSUPERVISED_FEATURES
)
import pandas as pd


DATA_PATH = r"Synergy_TP\task_12\data\Smart_Farming_Crop_Yield_2024.csv"


def main():

    df = load_data(DATA_PATH)

    print("=" * 60)
    print("K-MEANS CLUSTERING")
    print("=" * 60)

    print("Total observations:", len(df))

    X = prepare_unsupervised_data(df)

    k_values = [2, 3, 4, 5, 6]

    results = evaluate_k_values(
        X,
        k_values
    )

    print("\nSilhouette scores:")
    print(results.to_string(index=False))

    best_k = results.loc[
        results["silhouette_score"].idxmax(),
        "k"
    ]

    print("\nSelected k:", best_k)

    model, labels = run_kmeans(
        X,
        int(best_k)
    )

    df["cluster"] = labels

    print("\nCluster distribution:")
    print(df["cluster"].value_counts().sort_index())

    print("\nCluster characteristics:")
    cluster_summary = df.groupby("cluster")[UNSUPERVISED_FEATURES].mean()
    print(cluster_summary.round(2).to_string())

    print("\nCluster by region:")
    print(pd.crosstab(df["cluster"], df["region"]))

    print("\nCluster by crop:")
    print(pd.crosstab(df["cluster"], df["crop_type"]))

    print("\nCluster by disease status:")
    print(pd.crosstab(df["cluster"], df["crop_disease_status"]))


    print("\n" + "=" * 60)
    print("K-MEANS WITHOUT GEOGRAPHIC FEATURES")
    print("=" * 60)

    non_geographic_features = [
        "soil_moisture_%",
        "soil_pH",
        "temperature_C",
        "rainfall_mm",
        "humidity_%",
        "sunlight_hours",
        "pesticide_usage_ml",
        "total_days",
        "NDVI_index"
    ]

    X_no_geo = df[non_geographic_features].copy()

    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import silhouette_score
    from sklearn.cluster import KMeans

    X_no_geo = SimpleImputer(strategy="median").fit_transform(X_no_geo)
    X_no_geo = StandardScaler().fit_transform(X_no_geo)

    for k in [2, 3, 4, 5, 6]:
        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        labels = model.fit_predict(X_no_geo)

        score = silhouette_score(X_no_geo, labels)

        print(f"k={k}: silhouette={score:.6f}")



if __name__ == "__main__":
    main()