# Task 9 – Calibration Analysis, Replicate Statistics & Feature Engineering

## Overview

This project analyzes experimental calibration data by performing statistical analysis on replicate measurements, evaluating calibration quality, measuring correlations between variables, generating visualization plots, and engineering features for machine learning.

The workflow demonstrates a complete data analysis pipeline, beginning with raw experimental measurements and ending with an ML-ready dataset.

---

# Objectives

* Analyze replicate measurements and evaluate measurement reliability.
* Compute statistical summaries for every replicate group.
* Measure correlations between controlled input variables and measured signals.
* Fit calibration lines and evaluate their performance.
* Generate calibration and scatter plots.
* Engineer additional features for downstream machine learning tasks.
* Produce a cleaned, summarized, and ML-ready dataset.

---

# Project Structure

```
task_9/
│
├── data/
│   └── calibration_measurements.csv
│
├── output/
│   ├── replicate_summary.csv
│   ├── replicate_analysis.md
│   ├── correlation_summary.csv
│   ├── correlation_limitations.md
│   ├── calibration_curve_biochem.png
│   ├── calibration_curve_electronics.png
│   ├── calibration_curve_mechanical.png
│   ├── correlation_signal_input.png
│   └── ml_ready_dataset.csv
│
├── src/
│   ├── main.py
│   ├── replicate_statistics.py
│   ├── correlation_analysis.py
│   └── feature_engineering.py
│
└── README.md
```

---

# Features

## Part 1 – Replicate Statistics

The project groups replicate measurements using:

* Domain
* Experimental condition
* Input type
* Input value
* Input unit
* Signal unit

For each replicate group it calculates:

* Replicate count
* Mean signal
* Median signal
* Sample variance
* Sample standard deviation
* Standard error
* 95% confidence interval
* Coefficient of variation
* Minimum signal
* Maximum signal
* Stability classification

The project also generates a markdown report summarizing the reliability of replicate measurements.

---

## Part 2 – Calibration and Correlation Analysis

The following relationships are analyzed:

* Biochem — Signal vs Concentration
* Electronics — Signal vs Load
* Electronics — Signal vs Temperature
* Mechanical — Signal vs Load
* Mechanical — Stress vs Load

For every relationship the following metrics are calculated:

* Pearson correlation
* Spearman correlation
* Number of samples
* Calibration slope
* Calibration intercept
* R² value
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

Calibration curves and scatter plots are generated automatically.

---

## Part 3 – Feature Engineering

Additional features are generated for machine learning, including:

* Rolling average
* Normalized signal
* Power feature
* Percentage error
* Stress ratio
* Stability flag
* Machine-learning readiness flag

The engineered dataset is exported as an ML-ready CSV file.

---

# Technologies Used

* Python 3
* Pandas
* NumPy
* SciPy
* Matplotlib
* Scikit-learn

---

# Statistical Concepts Used

* GroupBy aggregation
* Sample variance
* Sample standard deviation
* Standard error
* Confidence intervals
* Coefficient of variation
* Pearson correlation
* Spearman correlation
* Linear regression
* Calibration curves
* Error analysis
* Feature engineering

---

# Output Files

| File                         | Description                                    |
| ---------------------------- | ---------------------------------------------- |
| replicate_summary.csv        | Statistical summary for every replicate group  |
| replicate_analysis.md        | Reliability analysis of replicate measurements |
| correlation_summary.csv      | Correlation and calibration statistics         |
| correlation_limitations.md   | Discussion of correlation limitations          |
| calibration_curve_*.png      | Calibration plots for each domain              |
| correlation_signal_input.png | Scatter plot of raw signal versus input value  |
| ml_ready_dataset.csv         | Dataset containing engineered features         |

---

# How to Run

From the project root:

```bash
python task_9/src/main.py task_9/data/calibration_measurements.csv task_9/output
```

---

# Learning Outcomes

This project demonstrates practical understanding of:

* Statistical analysis of repeated measurements
* Measurement reliability assessment
* Experimental calibration
* Correlation analysis
* Linear regression
* Model evaluation metrics
* Scientific data visualization
* Feature engineering
* Data preprocessing for machine learning
* Modular Python programming
* File handling and report generation