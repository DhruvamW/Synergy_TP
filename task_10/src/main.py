import numpy as np
import json
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os  

from data_utils import *
from metrics import *
from baselines import *
from linear_regression_gd import *
from logistic_regression_gd import *
from kmeans import *


def main():
    print("Loading dataset...")

    input_file = sys.argv[1]
    output_folder = sys.argv[2]

    df = load_data(input_file)

    df = clean_data(df)

    df = create_classification_target(df)

    print("Dataset loaded successfully.\n")


    print("Running Linear Regression...")

    X, y = get_regression_data(df)

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    X_train, X_test = standardize_data(X_train, X_test)


    baseline_predictions = regression_baseline(y_train, X_test)


    weights, bias, regression_loss = train_linear_regression(
        X_train,
        y_train,
        learning_rate=0.001,
        epochs=1000
    )

    regression_predictions = test_linear_regression(X_test, weights, bias)

    regression_y_test = y_test

    regression_metrics = {
        "Baseline MAE": float(mae(regression_y_test, baseline_predictions)),
        "Model MAE": float(mae(regression_y_test, regression_predictions)),
        "MSE": float(mse(regression_y_test, regression_predictions)),
        "RMSE": float(rmse(regression_y_test, regression_predictions)),
        "R2 Score": float(r2_score(regression_y_test, regression_predictions))
    }

    print(regression_metrics)
    print()




    print("Running Logistic Regression...")

    X, y = get_classification_data(df)

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    X_train, X_test = standardize_data(X_train, X_test)

    # Baseline

    baseline_predictions = classification_baseline(y_train, X_test)

    # Train model

    weights, bias, classification_loss = train_logistic_regression(X_train, y_train, learning_rate=0.01, epochs=1000)

    classification_predictions = test_logistic_regression(X_test, weights, bias)

    classification_y_test = y_test

    classification_metrics = {
        "Baseline Accuracy": float(accuracy(classification_y_test, baseline_predictions)),
        "Accuracy": float(accuracy(classification_y_test, classification_predictions)),
        "Precision": float(precision(classification_y_test, classification_predictions)),
        "Recall": float(recall(classification_y_test, classification_predictions)),
        "F1 Score": float(f1_score(classification_y_test, classification_predictions))
    }

    print(classification_metrics)
    print()


    print("Running KMeans...")

    X_cluster = get_clustering_data(df)

    X_cluster = np.array(X_cluster)

    labels, centroids = kmeans( X_cluster, k=3)

    clustering_metrics = {
        "Inertia": float(inertia(X_cluster, labels, centroids)),
        "Cluster Counts": cluster_counts(labels),
        "Silhouette Score": float(silhouette_score(X_cluster, labels))
    }

    print(clustering_metrics)
    print()

    print("Training completed successfully.")
    
    with open(os.path.join(output_folder, "regression_metrics.json"), "w") as file:
        json.dump(regression_metrics, file, indent=4)

    with open(os.path.join(output_folder, "classification_metrics.json"), "w") as file:
        json.dump(classification_metrics, file, indent=4)

    with open(os.path.join(output_folder, "clustering_metrics.json"), "w") as file:
        json.dump(clustering_metrics, file, indent=4)

    print("Metrics saved.")

    regression_df = pd.DataFrame({
        "Actual": regression_y_test.values,
        "Predicted": regression_predictions
    })

    regression_df.to_csv(os.path.join(output_folder, "regression_predictions.csv"), index=False)

    classification_df = pd.DataFrame({
        "Actual": classification_y_test.values,
        "Predicted": classification_predictions
    })

    classification_df.to_csv( os.path.join(output_folder, "classification_predictions.csv"), index=False)

    cluster_df = pd.DataFrame(X_cluster)

    cluster_df["Cluster"] = labels

    cluster_df.to_csv(os.path.join(output_folder, "clustering_assignments.csv"), index=False)

    print("Prediction files saved.")
    print("Metrics saved.")

    # Regression Loss Curve
    plt.figure(figsize=(6,4))

    plt.plot(regression_loss)

    plt.title("Regression Loss Curve")

    plt.xlabel("Epoch")

    plt.ylabel("Loss")

    plt.savefig(os.path.join(output_folder, "regression_loss_curve.png"))

    plt.close()

    # Classification Loss Curve
    plt.figure(figsize=(6,4))

    plt.plot(classification_loss)

    plt.title("Classification Loss Curve")

    plt.xlabel("Epoch")

    plt.ylabel("Loss")

    plt.savefig(os.path.join(output_folder, "classification_loss_curve.png"))

    plt.close()

    # Actual vs Predicted Plot
    plt.figure(figsize=(6,6))

    plt.scatter(regression_y_test, regression_predictions)

    plt.xlabel("Actual")

    plt.ylabel("Predicted")

    plt.title("Actual vs Predicted")

    plt.savefig(os.path.join(output_folder, "actual_vs_predicted.png"))

    plt.close()

    # Confusion Matrix Plot
    cm = confusion_matrix(classification_y_test, classification_predictions)

    plt.figure(figsize=(5,5))

    plt.imshow(cm)

    plt.colorbar()

    plt.xticks([0,1], ["Low","High"])

    plt.yticks([0,1], ["Low","High"])

    plt.xlabel("Predicted")

    plt.ylabel("Actual")

    for i in range(2):
        for j in range(2):
            plt.text(j, i, cm[i][j],
                    ha="center",
                    va="center",
                    color="white")

    plt.savefig(os.path.join(output_folder, "confusion_matrix.png"))

    plt.close()

    # Clustering Plot
    plt.figure(figsize=(6,6))

    plt.scatter(X_cluster[:,0], X_cluster[:,1], c=labels)

    plt.scatter(centroids[:,0], centroids[:,1], marker="X", s=150)

    plt.xlabel("Feature 1")

    plt.ylabel("Feature 2")

    plt.title("KMeans Clusters")

    plt.savefig(os.path.join(output_folder, "clustering_plot.png"))

    plt.close()

    print("Plots saved successfully.")


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage:")
        print("python main.py <input_csv> <output_folder>")
        sys.exit()

    main()