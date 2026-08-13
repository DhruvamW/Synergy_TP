import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def plot_class_distribution(y, output_path):

    plt.figure(figsize=(12, 6))

    y.value_counts().sort_index().plot(kind="bar")

    plt.title("Crop Class Distribution")
    plt.xlabel("Crop")
    plt.ylabel("Number of Samples")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()


def plot_confusion_matrix(confusion_matrix, class_names, model_name, output_path):

    plt.figure(figsize=(12, 10))

    sns.heatmap(
        confusion_matrix,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=class_names,
        yticklabels=class_names
    )

    plt.title(f"Confusion Matrix - {model_name}")
    plt.xlabel("Predicted Label")
    plt.ylabel("Actual Label")
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()


def plot_model_comparison(results, output_path):

    models = list(results.keys())

    accuracy = [
        results[model]["accuracy"]
        for model in models
    ]

    precision = [
        results[model]["precision"]
        for model in models
    ]

    recall = [
        results[model]["recall"]
        for model in models
    ]

    f1 = [
        results[model]["f1_score"]
        for model in models
    ]

    x = range(len(models))
    width = 0.2

    plt.figure(figsize=(12, 6))

    plt.bar(
        [i - 1.5 * width for i in x],
        accuracy,
        width,
        label="Accuracy"
    )

    plt.bar(
        [i - 0.5 * width for i in x],
        precision,
        width,
        label="Precision"
    )

    plt.bar(
        [i + 0.5 * width for i in x],
        recall,
        width,
        label="Recall"
    )

    plt.bar(
        [i + 1.5 * width for i in x],
        f1,
        width,
        label="F1-score"
    )

    plt.xticks(list(x), models, rotation=20)
    plt.ylabel("Score")
    plt.title("Model Performance Comparison")
    plt.legend()
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()


def plot_train_validation_scores(results, output_path):

    models = list(results.keys())

    train_scores = [
        results[model]["train_accuracy"]
        for model in models
    ]

    validation_scores = [
        results[model]["validation_accuracy"]
        for model in models
    ]

    x = range(len(models))
    width = 0.35

    plt.figure(figsize=(12, 6))

    plt.bar(
        [i - width / 2 for i in x],
        train_scores,
        width,
        label="Training Accuracy"
    )

    plt.bar(
        [i + width / 2 for i in x],
        validation_scores,
        width,
        label="Validation Accuracy"
    )

    plt.xticks(list(x), models, rotation=20)
    plt.ylabel("Accuracy")
    plt.title("Training vs Validation Accuracy")
    plt.legend()
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()