# Task 10.5 – Regression Pipeline using Scikit-learn

## Overview

This project implements a complete machine learning regression pipeline using **scikit-learn** to predict **Temperature** from five sensor readings. The project follows a standard supervised learning workflow, including data preparation, baseline comparison, multiple regression models, evaluation, visualization, and error analysis.

---

## Dataset

The dataset consists of numerical sensor readings collected from five sensors.

### Features

* Sensor1
* Sensor2
* Sensor3
* Sensor4
* Sensor5

### Target

* Temperature

Each row represents a single observation where the five sensor values are used to predict the corresponding temperature.

---

## Project Structure

```text
task_10.5/
│
├── data/
│   └── Data.csv
│
├── output/
│
├── src/
│   ├── config.py
│   ├── data_utils.py
│   ├── evaluation.py
│   ├── main.py
│   ├── models.py
│   └── visualisation.py
│
├── README.md
└── requirements.txt
```

---

## Models Implemented

### Baseline

* DummyRegressor

### Linear Models

* Linear Regression
* Ridge Regression

### Tree-Based Models

* Decision Tree Regressor
* Random Forest Regressor

Linear Regression and Ridge Regression are implemented using a **Pipeline** with `StandardScaler` so that feature scaling is automatically applied during both training and inference.

---

## Evaluation Metrics

Every model is evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* Coefficient of Determination (R²)

Both training and validation performance are compared to identify underfitting or overfitting.

---

## Visualizations

The project generates:

* Actual vs Predicted plot
* Residual plot

These plots help analyse prediction quality and model errors.

---

## Output Files

Running the project generates:

* `model_comparison.csv`
* `actual_vs_predicted.png`
* `residual_plot.png`
* `largest_errors.csv`

---

## Running the Project

From the root directory, run:

```bash
python task_10.5/src/main.py task_10.5/data/Data.csv task_10.5/output
```

---

## Why Ridge Regression Was Selected

The **DummyRegressor** achieved the highest validation performance because it predicts the mean temperature for every sample. This indicates that the available sensor features have only a weak relationship with the target variable, making the dataset difficult to model accurately.

Since the DummyRegressor is only a baseline and does not actually learn from the input features, it is not suitable as the final predictive model.

Among the machine learning models, **Ridge Regression** was selected as the final model because:

* It achieved the best validation performance among the trained learning models.
* It generalizes better than Decision Tree Regression, which significantly overfit the training data.
* It produced more stable predictions than Random Forest on this dataset.
* Ridge Regression applies **L2 regularization**, which reduces overfitting by preventing excessively large model coefficients while still learning relationships between the sensor readings and temperature.
* Its relatively simple model structure makes it easier to interpret and less prone to memorizing noise in small datasets.

Although the overall predictive performance remains close to the baseline, Ridge Regression provides the best trade-off between learning meaningful patterns and maintaining good generalization on unseen data.

---

## Libraries Used

* pandas
* numpy
* matplotlib
* scikit-learn

---

## Learning Outcomes

This project demonstrates:

* Building an end-to-end regression pipeline
* Data splitting into training, validation and test sets
* Using Pipelines for preprocessing
* Training multiple regression models
* Evaluating models using standard regression metrics
* Comparing learned models against a baseline
* Performing basic error analysis using residuals and prediction plots
* Selecting a final model based on both quantitative metrics and practical considerations
