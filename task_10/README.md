# Task 10 - Machine Learning from Scratch

## Overview

This project implements three fundamental machine learning algorithms from scratch using the **AirQualityUCI** dataset. The objective is to understand how machine learning models work internally without relying on libraries such as Scikit-learn.

The project includes:

- Linear Regression using Gradient Descent
- Logistic Regression using Gradient Descent
- KMeans Clustering
- Baseline models for comparison
- Manual implementation of evaluation metrics
- Data preprocessing and feature scaling
- Performance visualization using Matplotlib

---

## Project Structure

```
task_10/
├── README.md
├── theory/
│   └── Task_10_ML_Theory_Notes.pdf
├── data/
│   └── AirQualityUCI.csv
├── output/
│   ├── regression_metrics.json
│   ├── classification_metrics.json
│   ├── clustering_metrics.json
│   ├── regression_predictions.csv
│   ├── classification_predictions.csv
│   ├── clustering_assignments.csv
│   ├── regression_loss_curve.png
│   ├── classification_loss_curve.png
│   ├── actual_vs_predicted.png
│   ├── confusion_matrix.png
│   ├── clustering_plot.png
│   ├── model_comparison.md
│   └── error_analysis.md
└── src/
    ├── data_utils.py
    ├── metrics.py
    ├── baselines.py
    ├── linear_regression_gd.py
    ├── logistic_regression_gd.py
    ├── kmeans.py
    └── main.py
```

---

## Machine Learning Tasks

### Regression

**Goal**

Predict the continuous value of **CO(GT)** using air quality sensor measurements.

**Features Used**

- PT08.S1(CO)
- NMHC(GT)
- C6H6(GT)
- PT08.S2(NMHC)
- NOx(GT)
- PT08.S3(NOx)
- NO2(GT)
- PT08.S4(NO2)
- PT08.S5(O3)
- Temperature
- Relative Humidity
- Absolute Humidity

**Target**

- CO(GT)

---

### Classification

**Goal**

Predict whether pollution is **High** or **Low**.

The class label is created using the median value of CO(GT).

**Target**

- HighPollution (0 or 1)

---

### Clustering

**Goal**

Group similar air quality observations based on feature similarity without using class labels.

---

## Models Implemented

### Baseline Models

- Mean Predictor for Regression
- Majority Class Predictor for Classification

### Machine Learning Models

- Linear Regression (Gradient Descent)
- Logistic Regression (Gradient Descent)
- KMeans Clustering

All models are implemented from scratch using NumPy.

---

## Evaluation Metrics

### Regression

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### Classification

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

### Clustering

- Inertia
- Silhouette Score
- Cluster Counts

---

## Generated Outputs

After running the program, the following files are created inside the **output** folder:

- Regression Metrics
- Classification Metrics
- Clustering Metrics
- Regression Predictions
- Classification Predictions
- Cluster Assignments
- Regression Loss Curve
- Classification Loss Curve
- Actual vs Predicted Plot
- Confusion Matrix Plot
- Clustering Visualization
- Model Comparison Report
- Error Analysis Report

---

## How to Run

Navigate to the source folder and execute:

```bash
python main.py
```

or from the project root:

```bash
python task_10/src/main.py
```

---

## Libraries Used

- Python
- NumPy
- Pandas
- Matplotlib
- JSON

---

## Concepts Covered

This project demonstrates the following concepts:

- Data Cleaning
- Feature Selection
- Feature Scaling
- Train-Test Split
- Gradient Descent
- Linear Regression
- Logistic Regression
- Binary Classification
- Sigmoid Function
- Cross Entropy Loss
- KMeans Clustering
- Euclidean Distance
- Evaluation Metrics
- Model Comparison
- Error Analysis
- Data Visualization

---

## Learning Outcomes

After completing this project, I learned:

- How Linear Regression learns using Gradient Descent.
- How Logistic Regression performs binary classification.
- How the Sigmoid function converts values into probabilities.
- How KMeans clustering groups similar data points.
- How baseline models help evaluate machine learning models.
- How to manually calculate common evaluation metrics.
- How preprocessing and feature scaling improve model performance.
- How to visualize model performance using different plots.
- How machine learning algorithms work internally without using Scikit-learn.
