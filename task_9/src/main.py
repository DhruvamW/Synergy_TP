import os
import sys

from replicate_statistics import (
    load_data,
    calculate_replicate_statistics,
    save_replicate_summary,
    save_replicate_analysis,
)

from correlation_analysis import (
    calculate_correlations,
    plot_calibration_curve,
    plot_signal_input_scatter,
)

from feature_engineering import (
    add_rolling_average,
    add_normalized_signal,
    add_power_feature,
    add_error_percent,
    add_stress_ratio,
    add_stability_flag,
    add_ml_readiness_flag,
    save_engineered_features,
)


def main():

    if len(sys.argv) != 3:
        print("Usage: python task_9/src/main.py task_9/data/calibration_measurements.csv task_9/output")
        return

    input_file = sys.argv[1]
    output_folder = sys.argv[2]

    os.makedirs(output_folder, exist_ok=True)

    print("Loading dataset...")
    df = load_data(input_file)

    print("Calculating replicate statistics...")
    replicate_summary = calculate_replicate_statistics(df)

    save_replicate_summary(replicate_summary,os.path.join(output_folder, "replicate_summary.csv"))

    save_replicate_analysis(replicate_summary,output_folder)

    print("Running correlation analysis...")
    correlation_summary = calculate_correlations(df)

    correlation_summary.to_csv(os.path.join(output_folder, "correlation_summary.csv"),index=False)

    print("Generating plots...")

    plot_signal_input_scatter(df,output_folder)

    for domain in ["Biochem", "Electronics", "Mechanical"]:
        plot_calibration_curve(df, domain, output_folder)

    print("Engineering features...")

    engineered_df = add_rolling_average(df)
    engineered_df = add_normalized_signal(engineered_df)
    engineered_df = add_power_feature(engineered_df)
    engineered_df = add_error_percent(engineered_df)
    engineered_df = add_stress_ratio(engineered_df)
    engineered_df = add_stability_flag(engineered_df)
    engineered_df = add_ml_readiness_flag(engineered_df)

    save_engineered_features(engineered_df,output_folder)

    engineered_df.to_csv(os.path.join(output_folder, "ml_ready_dataset.csv"),index=False)

    print("\nTask 9 completed successfully!")
    print(f"Outputs saved to: {output_folder}")


if __name__ == "__main__":
    main()