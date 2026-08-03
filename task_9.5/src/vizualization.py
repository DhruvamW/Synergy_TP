import matplotlib.pyplot as plt
import numpy as np


def plot_training_loss(loss_history, title, save_path):
    plt.figure(figsize=(8, 5))
    plt.plot(loss_history)
    plt.title(title)
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def plot_regression_predictions(y_true, y_pred, save_path):
    plt.figure(figsize=(6, 6))

    plt.scatter(y_true, y_pred, alpha=0.6)

    minimum = min(np.min(y_true), np.min(y_pred))
    maximum = max(np.max(y_true), np.max(y_pred))

    plt.plot([minimum, maximum],
             [minimum, maximum],
             color="red",
             linestyle="--")

    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title("Actual vs Predicted")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def plot_confusion_matrix(confusion_matrix, save_path):
    matrix = np.array([
        [confusion_matrix["tn"], confusion_matrix["fp"]],
        [confusion_matrix["fn"], confusion_matrix["tp"]]
    ])

    plt.figure(figsize=(5, 5))
    plt.imshow(matrix, cmap="Blues")

    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    plt.xticks([0, 1], ["0", "1"])
    plt.yticks([0, 1], ["0", "1"])

    for i in range(2):
        for j in range(2):
            plt.text(
                j,
                i,
                matrix[i, j],
                ha="center",
                va="center",
                color="black",
                fontsize=12
            )

    plt.colorbar()
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()