import sys
import joblib
import pandas as pd


def main():

    if len(sys.argv) != 4:
        print(
            "Usage: python inference.py <model> <input_csv> <output_csv>"
        )
        return

    model = joblib.load(sys.argv[1])

    new_data = pd.read_csv(sys.argv[2])

    predictions = model.predict(new_data)

    pd.DataFrame({"Predicted Temperature": predictions}).to_csv( sys.argv[3], index=False)

    print("Prediction complete.")


if __name__ == "__main__":
    main()
