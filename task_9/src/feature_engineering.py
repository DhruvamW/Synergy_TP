import os
import numpy as np
import pandas as pd

STABLE_MAX = 0.05
MODERATE_MAX = 0.15


def add_rolling_average(df):

    df = df.sort_values(["domain", "condition", "time_step"]).copy()

    df["rolling_average_signal"] = (df.groupby(["domain", "condition"])["signal"].transform(lambda s: s.rolling(window=3, min_periods=1).mean()))

    return df


def add_normalized_signal(df):
    df = df.copy()

    valid = df["baseline_signal"].notna() & (df["baseline_signal"] != 0)

    df["normalized_signal"] = np.where(valid, df["signal"] / df["baseline_signal"], np.nan)

    return df


def add_power_feature(df):
    df = df.copy()

    valid = ((df["domain"] == "Electronics")& df["voltage_v"].notna()& df["current_a"].notna())

    df["power_w"] = np.where(valid, df["voltage_v"] * df["current_a"], np.nan)

    return df


def add_error_percent(df):
    df = df.copy()

    valid = df["expected_signal"].notna() & (df["expected_signal"] != 0)

    df["error_percent"] = np.where(valid,((df["signal"] - df["expected_signal"]) / df["expected_signal"]) * 100,np.nan,)

    return df


def add_stress_ratio(df):
    df = df.copy()

    valid = (
        (df["domain"] == "Mechanical")
        & df["stress_mpa"].notna()
        & df["reference_stress_mpa"].notna()
        & (df["reference_stress_mpa"] != 0)
    )

    df["stress_ratio"] = np.where(valid, df["stress_mpa"] / df["reference_stress_mpa"], np.nan)

    return df


def add_stability_flag(df):
    df = df.copy()

    group_cols = ["domain", "condition", "input_value"]

    stats = (
        df.groupby(group_cols)["signal"]
        .agg(_group_mean="mean", _group_std="std", _group_n="count")
        .reset_index()
    )

    valid = (
        (stats["_group_n"] >= 2)
        & stats["_group_mean"].notna()
        & (stats["_group_mean"] != 0)
    )

    stats["coefficient_of_variation"] = np.where(valid, stats["_group_std"] / stats["_group_mean"], np.nan)

    def classify(cv):
        if pd.isna(cv):
            return np.nan
        if cv <= STABLE_MAX:
            return "stable"
        if cv <= MODERATE_MAX:
            return "moderate"
        return "unstable"

    stats["stability_flag"] = stats["coefficient_of_variation"].apply(classify)

    df = df.merge(
        stats[group_cols + ["coefficient_of_variation", "stability_flag"]],
        on=group_cols,
        how="left",
    )

    return df


def add_ml_readiness_flag(df):
    df = df.copy()

    if "power_w" not in df.columns:
        df = add_power_feature(df)
    if "stress_ratio" not in df.columns:
        df = add_stress_ratio(df)
    if "stability_flag" not in df.columns:
        df = add_stability_flag(df)

    base_valid = (
        df["signal"].notna()
        & df["expected_signal"].notna()
        & (df["expected_signal"] != 0)
        & df["input_value"].notna()
        & df["domain"].notna()
        & df["condition"].notna()
    )

    electronics_ok = ~(df["domain"] == "Electronics") | df["power_w"].notna()
    mechanical_ok = ~(df["domain"] == "Mechanical") | df["stress_ratio"].notna()

    stability_ok = df["stability_flag"].notna() & (df["stability_flag"] != "unstable")

    df["ml_ready"] = base_valid & electronics_ok & mechanical_ok & stability_ok

    return df


def save_engineered_features(df, output_path: str) -> None:
    df.to_csv(os.path.join(output_path, "engineered_features.csv"), index=False)