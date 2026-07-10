# Model Comparison

## Overview

This project implemented three machine learning algorithms from scratch:

1. Linear Regression
2. Logistic Regression
3. KMeans Clustering

Simple baseline models were also implemented for regression and classification to compare the performance of the trained models.

---

## Regression

**Task:** Predict the CO(GT) value using sensor measurements.

### Baseline Model
- Always predicts the mean value of the training target.
- Very simple but provides a reference for comparison.

### Linear Regression
- Learns the relationship between input features and the target using Gradient Descent.
- Updates weights iteratively to reduce prediction error.
- Performs better than the baseline because it uses the information from all selected features.

### Evaluation Metrics
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## Classification

**Task:** Predict whether the pollution level is High or Low.

### Baseline Model
- Always predicts the majority class from the training data.
- Useful for comparing whether the trained model actually learns meaningful patterns.

### Logistic Regression
- Uses the sigmoid function to calculate probabilities.
- Gradient Descent is used to optimize the model parameters.
- Produces binary predictions (0 or 1).

### Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Clustering

**Task:** Group similar air quality observations without using labels.

### KMeans Clustering
- Randomly initializes cluster centers.
- Assigns each sample to the nearest centroid.
- Updates centroids until they no longer change significantly.

### Evaluation Metrics
- Inertia
- Silhouette Score
- Cluster Counts

---

## Overall Comparison

| Model | Learning Type | Target | Purpose |
|--------|---------------|--------|---------|
| Linear Regression | Supervised | Continuous | Predict CO(GT) values |
| Logistic Regression | Supervised | Binary | Predict High or Low Pollution |
| KMeans | Unsupervised | None | Group similar observations |

---

## Conclusion

The baseline models provide a simple reference for evaluating performance. The implemented machine learning models perform better because they learn patterns from the dataset rather than making constant predictions. Linear Regression models continuous values, Logistic Regression performs binary classification, and KMeans identifies groups of similar observations without requiring class labels.