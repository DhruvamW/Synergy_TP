# Task 9.5 – Regression and Classification from Scratch

## Overview

This project implements complete **Regression** and **Classification** machine learning workflows **from scratch**, without using any machine learning libraries such as **scikit-learn**.

Only the following libraries are used:

* NumPy
* pandas
* matplotlib

The objective is to understand the complete machine learning pipeline by implementing every major component manually, including data preprocessing, model training, evaluation, visualization, and baseline comparisons.

---

# Features

## Regression Workflow

* Data loading
* Train/Validation/Test split
* One-hot encoding of categorical variables
* Feature standardization
* Linear Regression implemented from scratch
* Gradient Descent optimization
* Regression metrics:

  * Mean Squared Error (MSE)
  * Root Mean Squared Error (RMSE)
  * Mean Absolute Error (MAE)
  * R² Score
* Mean-value baseline model
* Training loss visualization
* Actual vs Predicted visualization

---

## Classification Workflow

* Data loading
* Train/Validation/Test split
* One-hot encoding of categorical variables
* Feature standardization
* Logistic Regression implemented from scratch
* Sigmoid activation
* Binary Cross-Entropy Loss
* Gradient Descent optimization
* Classification metrics:

  * Accuracy
  * Precision
  * Recall
  * F1 Score
  * Confusion Matrix
* Majority-class baseline model
* Training loss visualization
* Confusion Matrix visualization

---

# Project Structure

```
task_9.5/
│
├── data/
│   ├── heart_disease_dataset.csv
│   └── oil_sales_dataset.csv
│
├── output/
│
├── src/
│   ├── main.py
│   ├── data_utils.py
│   ├── split.py
│   ├── preprocessing.py
│   ├── linear_regression.py
│   ├── logistic_regression.py
│   ├── metrics.py
│   ├── baselines.py
│   ├── utils.py
│   └── vizualization.py
│
└── README.md
```

---

# Implemented Modules

## `data_utils.py`

* Loads regression dataset
* Loads classification dataset
* Separates features and target variables

---

## `split.py`

Implements custom train-validation-test splitting using shuffled indices.

Default split:

* Training: 70%
* Validation: 15%
* Testing: 15%

---

## `preprocessing.py`

Implements preprocessing from scratch:

* One-hot encoding
* Feature standardization using training statistics

---

## `linear_regression.py`

Implements Linear Regression using Gradient Descent.

Includes:

* Prediction
* Cost function (MSE)
* Gradient computation
* Model training

---

## `logistic_regression.py`

Implements Logistic Regression using Gradient Descent.

Includes:

* Sigmoid activation
* Probability prediction
* Binary Cross-Entropy Loss
* Gradient computation
* Binary prediction

---

## `metrics.py`

### Regression Metrics

* Mean Squared Error
* Root Mean Squared Error
* Mean Absolute Error
* R² Score

### Classification Metrics

* Confusion Matrix
* Accuracy
* Precision
* Recall
* F1 Score

---

## `baselines.py`

Implements simple baseline models.

Regression

* Mean Predictor

Classification

* Majority Class Predictor

---

## `vizualization.py`

Creates:

* Training Loss Curves
* Actual vs Predicted Scatter Plot
* Confusion Matrix Heatmap

---

## `utils.py`

Contains helper functions for:

* Output directory creation
* Saving metrics
* Printing formatted results

---

# Output

Running the project generates:

```
output/

├── regression_metrics.json
├── regression_baseline_metrics.json
├── classification_metrics.json
├── classification_baseline_metrics.json

├── linear_loss.png
├── logistic_loss.png

├── regression_predictions.png
└── confusion_matrix.png
```

---

# How to Run

From the project root directory, execute:

```bash
python task_9.5/src/main.py task_9.5/data/oil_sales_dataset.csv task_9.5/data/heart_disease_dataset.csv task_9.5/output
```

---

# Learning Outcomes

This project demonstrates an understanding of:

* Data preprocessing
* Train/Validation/Test splitting
* Feature encoding
* Feature scaling
* Gradient Descent optimization
* Linear Regression
* Logistic Regression
* Binary Cross-Entropy Loss
* Regression evaluation metrics
* Classification evaluation metrics
* Baseline model comparison
* Error analysis
* Model visualization

---

# Technologies Used

* Python 3
* NumPy
* pandas
* matplotlib

---

# Notes

* No machine learning libraries (such as scikit-learn) were used for model implementation.
* All regression and classification algorithms were implemented manually using NumPy.
* Gradient Descent is used to optimize both Linear Regression and Logistic Regression models.
* Baseline models are included to provide meaningful comparisons with the trained models.
