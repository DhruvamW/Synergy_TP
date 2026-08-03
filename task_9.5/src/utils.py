import os
import json


def ensure_directory(output_dir):
    os.makedirs(output_dir, exist_ok=True)


def save_metrics(metrics, filepath):
    with open(filepath, "w") as f:
        json.dump(metrics, f, indent=4)


def print_results(title, metrics):
    print(f"\n{'=' * 50}")
    print(title)
    print(f"{'=' * 50}")

    for key, value in metrics.items():
        if isinstance(value, float):
            print(f"{key:<20}: {value:.4f}")
        else:
            print(f"{key:<20}: {value}")