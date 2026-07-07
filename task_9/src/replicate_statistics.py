import pandas as pd
import scipy.stats as st
import os

def load_data(file_path: str):
    df = pd.read_csv(file_path)
    return df

def calculate_replicate_statistics(df):
    groups = df.groupby(["domain","condition","input_type","input_value","input_unit","signal_unit"])
    summary=[]
    for name, group in groups:
        domain, condition, input_type, input_value, input_unit, signal_unit = name
        replicate_count = group["signal"].count()
        mean_signal = group["signal"].mean()
        median_signal = group["signal"].median()
        variance_signal = group["signal"].var(ddof=1)
        minimum_signal = group["signal"].min()
        maximum_signal = group["signal"].max()
        if replicate_count < 2:
            standard_deviation_signal = None
            standard_error_signal = None
            confidence_interval_lower = None
            confidence_interval_upper = None
            coefficient_of_variation = None
            stability_flag = None
        else:
            standard_deviation_signal = group["signal"].std(ddof=1)
            standard_error_signal = group["signal"].sem()
            confidence_interval_lower , confidence_interval_upper = calculate_confidence_interval(mean_signal,standard_error_signal,replicate_count)
            if mean_signal != 0:
                coefficient_of_variation = standard_deviation_signal / mean_signal
            else:
                coefficient_of_variation = None
            stability_flag = assign_stability_flag(coefficient_of_variation)
        record ={
            "domain" : domain,
            "condition" : condition,
            "input_type" : input_type,
            "input_value" : input_value,
            "input_unit" : input_unit,
            "signal_unit" : signal_unit,
            "replicate_count" : replicate_count,
            "mean_signal" : mean_signal,
            "median_signal" : median_signal,
            "variance_signal" : variance_signal,
            "minimum_signal" : minimum_signal,
            "maximum_signal" : maximum_signal,
            "standard_deviation_signal" : standard_deviation_signal,
            "standard_error_signal" : standard_error_signal,
            "confidence_interval_lower" : confidence_interval_lower,
            "confidence_interval_upper" : confidence_interval_upper,
            "coefficient_of_variation" : coefficient_of_variation,
            "stability_flag" : stability_flag
        }
        summary.append(record)
    summary_df = pd.DataFrame(summary)
    return summary_df

def calculate_confidence_interval(mean: float, sem: float, n: int) -> tuple[float, float]:
    df = n - 1
    lower_bound, upper_bound = st.t.interval(0.95, df=df, loc=mean, scale=sem)
    return float(lower_bound), float(upper_bound)

def assign_stability_flag(coefficient_of_variation: float) -> str:
    if coefficient_of_variation < 0:
        raise ValueError("Coefficient of variation cannot be negative.")
    if coefficient_of_variation <= 0.10:
        return 'Stable'
    elif coefficient_of_variation <= 0.20:
        return 'Moderately Stable'
    else:
        return 'Unstable'

def save_replicate_summary(summary_df, output_path: str) -> None:
    summary_df.to_csv(output_path, index=False)

def save_replicate_analysis(summary_df, output_path):
    most_stable = summary_df.loc[summary_df["coefficient_of_variation"].idxmin()]

    most_noisy = summary_df.loc[summary_df["coefficient_of_variation"].idxmax()]

    summary_df["ci_width"] = (summary_df["confidence_interval_upper"] - summary_df["confidence_interval_lower"])

    widest_ci = summary_df.loc[summary_df["ci_width"].idxmax()]

    highest_cv = summary_df.loc[summary_df["coefficient_of_variation"].idxmax()]

    file_path = os.path.join(output_path, "replicate_analysis.md")

    with open(file_path, "w") as file:

        file.write("# Replicate Analysis\n\n")

        file.write("## Which replicate group is most stable?\n")
        file.write(
            f"{most_stable['domain']} - {most_stable['condition']} "
            f"(Coefficient of Variation = {most_stable['coefficient_of_variation']:.4f})\n\n"
        )

        file.write("## Which replicate group is most noisy?\n")
        file.write(
            f"{most_noisy['domain']} - {most_noisy['condition']} "
            f"(Coefficient of Variation = {most_noisy['coefficient_of_variation']:.4f})\n\n"
        )

        file.write("## Which group has the widest confidence interval?\n")
        file.write(
            f"{widest_ci['domain']} - {widest_ci['condition']}\n\n"
        )

        file.write("## Which group has the highest coefficient of variation?\n")
        file.write(
            f"{highest_cv['domain']} - {highest_cv['condition']} "
            f"({highest_cv['coefficient_of_variation']:.4f})\n\n"
        )

        file.write("## Why is mean alone not enough for judging reliability?\n")
        file.write(
            "The mean only describes the average measurement. "
            "It does not show how much the replicate readings vary. "
            "Two groups may have the same mean but very different variability, "
            "making one reliable and the other unreliable.\n\n"
        )

        file.write("## Why does replicate count affect confidence interval width?\n")
        file.write(
            "As the number of replicate measurements increases, the standard error decreases. "
            "This results in a narrower confidence interval and a more precise estimate of the true mean.\n\n"
        )

        file.write("## Which readings should be investigated before using the data for machine learning?\n")
        file.write(
            "Groups with high coefficient of variation, wide confidence intervals, "
            "or unstable measurements should be investigated because they may indicate "
            "measurement noise, outliers, or experimental errors.\n"
        )