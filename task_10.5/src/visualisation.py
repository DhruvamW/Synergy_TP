import matplotlib.pyplot as plt
import numpy as np


def plot_actual_vs_predicted(y_true, y_pred, save_path):

    plt.figure(figsize=(6, 6))

    plt.scatter(y_true, y_pred, alpha=0.7)

    min_val = min(np.min(y_true), np.min(y_pred))
    max_val = max(np.max(y_true), np.max(y_pred))

    plt.plot(
        [min_val, max_val],
        [min_val, max_val],
        color="red",
        linestyle="--",
        label="Ideal Prediction"
    )

    plt.xlabel("Actual Temperature")
    plt.ylabel("Predicted Temperature")
    plt.title("Actual vs Predicted")
    plt.legend()

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def plot_residuals(y_true, y_pred, save_path):

    residuals = y_true - y_pred

    plt.figure(figsize=(6, 6))

    plt.scatter(y_pred, residuals, alpha=0.7)

    plt.axhline(
        y=0,
        color="red",
        linestyle="--"
    )

    plt.xlabel("Predicted Temperature")
    plt.ylabel("Residual")
    plt.title("Residual Plot")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()