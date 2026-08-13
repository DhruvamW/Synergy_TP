# Task 11 — Crop Recommendation Classification

## Overview

This project implements a complete **multiclass classification experiment** using the Crop Recommendation dataset.

The objective is to predict the most suitable crop based on soil and environmental conditions.

The input features are:

* Nitrogen (`N`)
* Phosphorus (`P`)
* Potassium (`K`)
* Temperature
* Humidity
* Soil pH
* Rainfall

The target variable is `label`, which represents the recommended crop.

---

## Dataset

The dataset contains:

* **2200 samples**
* **7 numerical features**
* **22 crop classes**
* **100 samples per crop class**

### Features

| Feature       | Description        |
| ------------- | ------------------ |
| `N`           | Nitrogen content   |
| `P`           | Phosphorus content |
| `K`           | Potassium content  |
| `temperature` | Temperature        |
| `humidity`    | Relative humidity  |
| `ph`          | Soil pH            |
| `rainfall`    | Rainfall           |

### Target

```text
label
```

The target represents the crop considered most suitable for the given soil and environmental conditions.

---

## Project Structure

```text
task_11/
│
├── data/
│   └── Crop_recommendation.csv
│
├── output/
│   ├── figures/
│   ├── metrics/
│   ├── model/
│   └── predictions.csv
│
├── src/
│   ├── data_utils.py
│   ├── preprocessing.py
│   ├── models.py
│   ├── metrics.py
│   ├── visualization.py
│   ├── inference.py
│   └── main.py
│
├── config.py
├── requirements.txt
└── README.md
```

---

## Machine Learning Workflow

```text
Dataset
   ↓
Load Data
   ↓
Separate Features and Target
   ↓
Stratified Train / Validation / Test Split
   ↓
Train Classification Models
   ↓
Validation Evaluation
   ↓
Model Comparison
   ↓
Error Analysis
   ↓
Final Model Selection
   ↓
Test Evaluation
   ↓
Save Final Pipeline
   ↓
Inference
```

---

## Data Splitting

The dataset is divided into:

| Dataset    | Percentage | Samples |
| ---------- | ---------: | ------: |
| Training   |        70% |    1540 |
| Validation |        15% |     330 |
| Test       |        15% |     330 |

`stratify` is used during splitting to preserve the distribution of the 22 crop classes across the datasets.

The test set is kept separate until the final model has been selected.

---

## Models

Five classifiers are evaluated.

### 1. DummyClassifier

A majority-class baseline is created using:

```python
DummyClassifier(strategy="most_frequent")
```

This provides a reference point for determining whether the machine learning models learn useful patterns beyond a simple baseline.

### 2. Logistic Regression

A pipeline containing `StandardScaler` and `LogisticRegression` is used.

```text
Input
  ↓
StandardScaler
  ↓
Logistic Regression
  ↓
Prediction
```

Scaling is used because Logistic Regression is affected by feature magnitudes during optimization.

### 3. K-Nearest Neighbors

A pipeline containing `StandardScaler` and `KNeighborsClassifier` is used.

```text
Input
  ↓
StandardScaler
  ↓
KNN
  ↓
Prediction
```

Scaling is important because KNN relies on distances between samples.

### 4. Decision Tree

`DecisionTreeClassifier` is used without feature scaling.

Decision Trees make threshold-based splits and therefore do not require standardized features.

### 5. Random Forest

`RandomForestClassifier` is used without feature scaling.

Random Forest consists of multiple decision trees, so feature scaling is not required.

---

## Evaluation Metrics

Every model is evaluated using:

* Accuracy
* Macro Precision
* Macro Recall
* Macro F1-score

Macro averaging is used because this is a multiclass classification problem and gives equal importance to each crop class.

Additional evaluation includes:

* Classification reports
* Confusion matrices
* Misclassified samples
* Training vs validation accuracy
* Model comparison

---

## Error Analysis

Misclassified samples are saved for further inspection.

Confusion matrices are used to identify which crop classes are commonly confused.

Incorrect crop recommendations can have real-world consequences such as:

* Reduced crop yield
* Wasted fertilizer or irrigation resources
* Poor crop growth
* Increased cultivation costs
* Financial losses

Therefore, final model selection considers both metric performance and the nature of classification errors.

---

## Model Selection

Models are initially compared using their validation performance.

Macro F1-score is used as an important selection metric because it evaluates performance across all crop classes equally.

However, the final model should also be checked using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion matrix
* Misclassification patterns
* Training vs validation behaviour

The test set is used only after the final model has been selected.

---

## Model Saving

The final preprocessing-and-model pipeline is saved using `joblib`.

```text
output/model/crop_classifier.joblib
```

For models requiring preprocessing, the scaler and classifier are saved together inside the pipeline.

This ensures that new data receives the same preprocessing used during training.

---

## Binary Threshold Analysis

The dataset contains **22 target classes**, so binary classification threshold analysis is not applicable.

Instead, models that support `predict_proba()` provide class probabilities. The predicted class is the class with the highest probability.

For example:

```text
Predicted crop: rice
Confidence: 0.97
```

The reported confidence represents the model's highest predicted probability and should not be interpreted as a guarantee that the prediction is correct.

---

## Requirements

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

Recommended `requirements.txt`:

```text
pandas
numpy
scikit-learn
matplotlib
joblib
```

---

## Running the Training Experiment

From the project root:

```bash
python task_11/src/main.py task_11/data/Crop_recommendation.csv task_11/output
```

If already inside the `task_11` directory:

```bash
python src/main.py data/Crop_recommendation.csv output
```

The training script will:

1. Load the dataset.
2. Separate features and target.
3. Create stratified train, validation, and test sets.
4. Train the DummyClassifier.
5. Train Logistic Regression.
6. Train KNN.
7. Train Decision Tree.
8. Train Random Forest.
9. Evaluate validation performance.
10. Generate confusion matrices.
11. Generate classification reports.
12. Save misclassified samples.
13. Compare model performance.
14. Select a final model.
15. Evaluate the final model on the test set.
16. Save the final model pipeline.

---

## Running Inference

After training, the saved model will be located at:

```text
output/model/crop_classifier.joblib
```

Create a CSV containing the seven input features:

```text
N,P,K,temperature,humidity,ph,rainfall
90,42,43,20.8,82.0,6.5,202.9
```

Then run:

```bash
python task_11/src/inference.py task_11/output/model/crop_classifier.joblib task_11/data/new_samples.csv
```


The inference script:

1. Loads the saved pipeline.
2. Loads the new input CSV.
3. Predicts the crop.
4. Calculates the highest predicted probability when available.
5. Displays the predictions.
6. Saves the results to:

```text
output/predictions.csv
```

---

## Generated Outputs

### Figures

```text
output/figures/
├── class_distribution.png
├── confusion_matrix_dummy.png
├── confusion_matrix_logistic_regression.png
├── confusion_matrix_knn.png
├── confusion_matrix_decision_tree.png
├── confusion_matrix_random_forest.png
├── model_comparison.png
├── train_validation_accuracy.png
└── final_confusion_matrix.png
```

### Metrics and Error Analysis

```text
output/metrics/
├── model_comparison.csv
├── final_test_metrics.csv
├── final_classification_report.txt
├── dummy_classification_report.txt
├── logistic_regression_classification_report.txt
├── knn_classification_report.txt
├── decision_tree_classification_report.txt
├── random_forest_classification_report.txt
└── *_misclassified.csv
```

### Saved Model

```text
output/model/
└── crop_classifier.joblib
```

---

## Reproducibility

A fixed random state is used throughout the experiment:

```python
RANDOM_STATE = 42
```

This ensures that the data splitting and models involving randomness produce reproducible results.

---

## Important Design Decisions

### Why use stratified splitting?

Because this is a multiclass classification problem. Stratification ensures that the crop-class distribution remains representative across the training, validation, and test sets.

### Why scale Logistic Regression and KNN?

Logistic Regression benefits from comparable feature scales during optimization, while KNN uses feature distances directly.

### Why not scale Decision Tree and Random Forest?

Tree-based models use threshold-based splits and are not dependent on feature magnitude or distance calculations.

### Why use a validation set?

The validation set allows different models to be compared and the final model to be selected without using the test set.

### Why keep the test set untouched?

The test set provides an unbiased estimate of how well the selected final model generalizes to unseen data.

---

## Deliverables

The project provides the required deliverables:

* Classification training code
* Majority-class baseline
* Logistic Regression
* K-Nearest Neighbors
* Decision Tree
* Random Forest
* Train/validation/test split
* Accuracy, precision, recall and F1-score
* Per-class classification reports
* Confusion matrices
* Misclassified-sample analysis
* Training vs validation comparison
* Model comparison table
* Final model selection
* Saved classification pipeline
* Separate inference script
* Prediction output
* Relevant comparison plots
* Setup and execution instructions

