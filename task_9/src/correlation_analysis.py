

import os
import numpy as np
import pandas as pd
from scipy import stats as st
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt


RELATIONSHIPS = [
    # domain, x_col, y_col, relationship label
    ("Biochem", "input_value", "signal", "Signal vs Concentration"),
    ("Electronics", "input_value", "signal", "Signal vs Load"),
    ("Electronics", "temperature_c", "signal", "Signal vs Temperature"),
    ("Mechanical", "input_value", "signal", "Signal vs Load"),
    ("Mechanical", "input_value", "stress_mpa", "Stress vs Load"),
]


def calculate_correlations(df):
    summary = []

    for domain, x_col, y_col, relationship in RELATIONSHIPS:

        domain_df = df[df["domain"] == domain]

        data = (domain_df[[x_col, y_col]].dropna().rename(columns={x_col: "x", y_col: "y"}))

        if len(data) < 3:
            continue

        pearson_corr, _ = st.pearsonr(data["x"], data["y"])
        spearman_corr, _ = st.spearmanr(data["x"], data["y"])
        slope, intercept, r_squared = fit_calibration_line(data)

        data = data.copy()
        data["predicted"] = slope * data["x"] + intercept

        mae, rmse = calculate_fit_metrics(data)

        record = {
            "domain": domain,
            "relationship": relationship,
            "x_variable": x_col,
            "y_variable": y_col,
            "pearson_correlation": pearson_corr,
            "spearman_correlation": spearman_corr,
            "number_of_samples": len(data),
            "slope": slope,
            "intercept": intercept,
            "r_squared": r_squared,
            "mean_absolute_error": mae,
            "root_mean_squared_error": rmse,
        }

        summary.append(record)

    return pd.DataFrame(summary)


def fit_calibration_line(df):

    result = st.linregress(df["x"], df["y"])

    slope = result.slope
    intercept = result.intercept
    r_squared = result.rvalue ** 2

    return slope, intercept, r_squared


def calculate_fit_metrics(df):

    mae = mean_absolute_error(df["y"], df["predicted"])
    rmse = np.sqrt(mean_squared_error(df["y"], df["predicted"]))

    return mae, rmse


def plot_calibration_curve(df, domain: str, output_path: str) -> None:

    domain_df = df[df["domain"] == domain]

    grouped = (domain_df.groupby("input_value")["signal"].agg(mean_signal="mean", sem="sem", n="count").reset_index())

    
    t_val = st.t.ppf(0.975, (grouped["n"] - 1).clip(lower=1))
    error = (t_val * grouped["sem"]).fillna(0)

    plt.figure(figsize=(7, 5))

    plt.errorbar(grouped["input_value"],grouped["mean_signal"],yerr=error,marker="o",capsize=5,)

    plt.xlabel("Input Value")
    plt.ylabel("Mean Signal")
    plt.title(f"{domain} Calibration Curve")
    plt.grid(True)

    plt.savefig(os.path.join(output_path, f"calibration_curve_{domain.lower()}.png"))
    plt.close()


def plot_signal_input_scatter(df, output_path: str) -> None:

    plt.figure(figsize=(8, 6))

    for domain in df["domain"].unique():
        domain_df = df[df["domain"] == domain]
        plt.scatter(domain_df["input_value"], domain_df["signal"], label=domain)

    plt.xlabel("Input Value")
    plt.ylabel("Signal")
    plt.title("Signal vs Input Value")
    plt.legend()
    plt.grid(True)

    plt.savefig(os.path.join(output_path, "correlation_signal_input.png"))
    plt.close()