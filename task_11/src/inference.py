import sys
from pathlib import Path

import joblib
import pandas as pd


def load_model(model_path):

    model_path = Path(model_path)

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model not found: {model_path}"
        )

    return joblib.load(model_path)


def load_input_data(input_path):

    input_path = Path(input_path)

    if not input_path.exists():
        raise FileNotFoundError(
            f"Input file not found: {input_path}"
        )

    return pd.read_csv(input_path)


def predict(model, input_data):

    predictions = model.predict(input_data)

    result = input_data.copy()
    result["predicted_label"] = predictions

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_data)

        result["confidence"] = probabilities.max(axis=1)

    return result


def main():

    if len(sys.argv) != 3:
        print(
            "Usage: python inference.py "
            "<model_path> <input_csv>"
        )
        return

    model_path = sys.argv[1]
    input_path = sys.argv[2]

    model = load_model(model_path)

    input_data = load_input_data(input_path)

    results = predict(model, input_data)

    print("\nPredictions:")
    print(results)

    output_path = Path("output/predictions.csv")
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    results.to_csv(
        output_path,
        index=False
    )

    print(
        f"\nPredictions saved to: {output_path}"
    )


if __name__ == "__main__":
    main()