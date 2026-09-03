# Task 12 — Robust Model Evaluation, Stability & Deployment Robustness

## Overview

This task evaluates whether a machine learning model's performance is genuinely reliable under realistic deployment conditions.

Instead of relying only on a single random train/test split, the task investigates:

* Generalization to genuinely unseen data
* Random vs. structure-aware evaluation
* Performance stability across repeated experiments
* Unsupervised clustering
* Anomaly detection
* Robustness to missing sensor information
* Possible causes of model failure

The supervised learning problem uses **crop disease status classification** on a public smart-farming dataset.

---

## Dataset

### Dataset Used

**Smart Farming Crop Yield 2024**

The dataset contains agricultural observations including environmental conditions, crop information, sensor-derived measurements, geographic information, and crop disease status.

### Dataset Characteristics

| Property                      |               Value |
| ----------------------------- | ------------------: |
| Observations                  |                 500 |
| Features                      |                  22 |
| Regions                       |                   5 |
| Crop types                    |                   5 |
| Farms                         |                 500 |
| Sensors                       |                 500 |
| Date range                    | Jan 2024 – Aug 2024 |
| Labelled disease observations |                 370 |
| Disease classes               |                   3 |

### Important Columns

* `farm_id` — farm identifier
* `region` — geographical region
* `crop_type` — type of crop
* `soil_moisture_%` — soil moisture
* `soil_pH` — soil pH
* `temperature_C` — temperature
* `rainfall_mm` — rainfall
* `humidity_%` — humidity
* `sunlight_hours` — sunlight exposure
* `irrigation_type` — irrigation method
* `fertilizer_type` — fertilizer type
* `pesticide_usage_ml` — pesticide usage
* `sowing_date` — sowing date
* `harvest_date` — harvest date
* `total_days` — crop duration
* `yield_kg_per_hectare` — crop yield
* `sensor_id` — sensor identifier
* `timestamp` — observation timestamp
* `latitude`, `longitude` — geographic location
* `NDVI_index` — vegetation index
* `crop_disease_status` — disease classification target

### Target

The supervised classification target is:

```text
crop_disease_status
```

The three classes are:

* Mild
* Moderate
* Severe

There are 370 labelled observations. The remaining observations have missing disease-status labels and are excluded from supervised classification experiments.

---

# Project Structure

```text
task_12/
│
├── data/
│   └── Smart_Farming_Crop_Yield_2024.csv
│
├── output/
│   └── data_exploration.txt
│
├── src/
│   ├── anomaly_detection.py
│   ├── data_loader.py
│   ├── evaluate.py
│   ├── exploration_data.py
│   ├── main.py
│   ├── model.py
│   ├── preprocessing.py
│   ├── robustness_test.py
│   ├── run_anomaly.py
│   ├── run_unsupervised.py
│   ├── splits.py
│   └── unsupervised.py
│
├── .gitignore
└── README.md
```

---

# Requirements

Python 3.13.5 was used for this task.

Install the required libraries:

```bash
pip install pandas numpy scikit-learn
```

If a virtual environment is being used:

```bash
python -m venv .venv
```

Activate it and install the dependencies.

---

# Running the Project

From the `task_12` directory:

```bash
python src/main.py
```

The main script performs:

1. Dataset loading
2. Supervised classification
3. Random train/validation/test evaluation
4. Leave-one-region-out evaluation
5. Repeated evaluation using five seeds
6. Robustness testing with missing NDVI

Anomaly detection can be run separately:

```bash
python src/run_anomaly.py
```

---

# Part 1 — Dataset Discovery and Generalization

## Observation Unit

Each row represents an agricultural observation associated with a particular farm/sensor measurement.

Although `farm_id` and `sensor_id` are present, each occurs only once in this dataset. Therefore, they cannot provide meaningful repeated-group holdouts.

The important natural structures are:

* **Region** — 5 geographical groups
* **Timestamp** — temporal structure spanning January–August 2024

Because region contains multiple observations, it can be used to simulate deployment on a previously unseen geographical region.

---

## Supervised Features

The classifier uses:

```text
crop_type
soil_moisture_%
soil_pH
temperature_C
rainfall_mm
humidity_%
sunlight_hours
irrigation_type
fertilizer_type
pesticide_usage_ml
sowing_date
NDVI_index
latitude
longitude
```

Identifiers such as `farm_id` and `sensor_id` are not used as predictive features.

The target `crop_disease_status` is also excluded from the input features.

---

## Model

A regularized Random Forest classifier is used.

The model is placed inside a preprocessing pipeline so that preprocessing is fitted using the training data and then consistently applied to validation and test data.

The model configuration is:

```text
RandomForestClassifier
n_estimators = 200
max_depth = 8
min_samples_leaf = 5
random_state = 42
```

A dummy classifier is also used as a baseline.

---

## Random Split

The first experiment uses a stratified random split:

```text
Training set:   258 observations
Validation set:  56 observations
Test set:       56 observations
```

This represents the conventional evaluation scenario where observations are assumed to be exchangeable.

### Random Split Result

For seed `42`:

| Metric              | Result |
| ------------------- | -----: |
| Train Accuracy      | 98.45% |
| Validation Accuracy | 32.14% |
| Test Accuracy       | 44.64% |
| Test Macro F1       | 0.3991 |

The very high training accuracy compared with the much lower validation and test performance indicates substantial overfitting.

---

# Realistic Generalization — Leave-One-Region-Out

A more realistic deployment question is:

> **Can a model trained using data from several regions generalize to a completely unseen geographical region?**

To test this, each of the five regions is held out once as the test set.

The remaining four regions are used for training and validation.

This prevents observations from the same region appearing in both training and test data.

### Regional Test Results

| Held-out Region | Model Accuracy | Dummy Accuracy |
| --------------- | -------------: | -------------: |
| North India     |         32.47% |         37.66% |
| South USA       |         22.73% |         25.76% |
| Central USA     |         31.65% |         29.11% |
| East Africa     |         42.17% |         36.14% |
| South India     |         36.92% |         38.46% |

Mean regional test accuracy is approximately:

```text
33.0%
```

Compared with:

```text
44.6%
```

for the seed-42 random test split.

### Interpretation

Performance decreases when the model is evaluated on an unseen geographical region.

This suggests that the random split gives an overly optimistic estimate of deployment performance.

The model only outperforms the dummy baseline on some regions, showing that generalization across regions is weak.

---

# Part 2 — Stability and Repeated Evaluation

A single train/test split can produce a misleading result.

Therefore, the random stratified experiment was repeated using five different split seeds:

```text
42
43
44
45
46
```

The model's random state was kept fixed at `42`, allowing the experiment to primarily measure variability caused by different data splits.

## Results

| Seed | Train Accuracy | Validation Accuracy | Test Accuracy | Test Macro F1 |
| ---: | -------------: | ------------------: | ------------: | ------------: |
|   42 |         98.45% |              32.14% |        44.64% |        0.3991 |
|   43 |         97.67% |              32.14% |        30.36% |        0.3030 |
|   44 |         97.67% |              39.29% |        30.36% |        0.2757 |
|   45 |         97.29% |              28.57% |        32.14% |        0.2992 |
|   46 |         97.29% |              39.29% |        37.50% |        0.3532 |

### Mean and Standard Deviation

| Metric              |   Mean | Standard Deviation |
| ------------------- | -----: | -----------------: |
| Train Accuracy      | 97.67% |              0.47% |
| Validation Accuracy | 34.29% |              4.79% |
| Test Accuracy       | 35.00% |              6.13% |
| Test Macro F1       | 0.3260 |             0.0497 |

The main stability result is:

```text
Test Macro F1 = 0.326 ± 0.050
```

and:

```text
Test Accuracy = 35.0% ± 6.1 percentage points
```

### Interpretation

The test accuracy ranges from approximately:

```text
30.36% → 44.64%
```

Therefore, reporting only the best run would give a misleading impression of model quality.

The model also shows a large generalization gap:

```text
Training Accuracy ≈ 97.7%
Test Accuracy     ≈ 35.0%
```

This indicates that the model fits the training data well but does not generalize reliably to unseen observations.

---

# Part 3 — Unsupervised Learning

## K-Means Clustering

K-Means clustering was used to investigate whether the agricultural observations contain naturally separated groups.

The clustering features include environmental, agricultural, and sensor-derived numerical measurements.

Before clustering:

1. Missing numerical values are median-imputed.
2. Features are standardized using `StandardScaler`.
3. K-Means is applied.

The evaluated values of `k` were:

```text
k = 2, 3, 4, 5, 6
```

The silhouette score was used to evaluate cluster separation.

---

## K-Means Results

### Original Feature Set

|  k | Silhouette Score |
| -: | ---------------: |
|  2 |           0.0770 |
|  3 |           0.0714 |
|  4 |           0.0729 |
|  5 |           0.0736 |
|  6 |           0.0736 |

The highest score was:

```text
k = 2
Silhouette = 0.077
```

This indicates weak cluster separation.

---

## Geographic Feature Check

Latitude and longitude can cause clustering based mainly on geographic proximity.

Therefore, a second experiment was performed after removing:

```text
latitude
longitude
```

Results:

|  k | Silhouette Score |
| -: | ---------------: |
|  2 |           0.0929 |
|  3 |           0.0886 |
|  4 |           0.0898 |
|  5 |           0.0889 |
|  6 |           0.0952 |

The best result was:

```text
k = 6
Silhouette = 0.095
```

Although slightly higher, the score remains low.

### Interpretation

The dataset does not exhibit strongly separated natural clusters in the selected feature space.

The observations appear to contain largely overlapping agricultural conditions rather than clearly separated groups.

---

## Clusters Are Not Automatically Classes

The clustering results do not correspond directly to disease classes.

For example:

| Cluster | Mild | Moderate | Severe |
| ------- | ---: | -------: | -----: |
| 0       |   68 |       61 |     64 |
| 1       |   57 |       51 |     69 |

Each cluster contains substantial numbers of all three disease classes.

Therefore:

> A cluster discovered by an unsupervised algorithm should not automatically be interpreted as a semantic class.

Clustering describes similarity in the selected feature space, not necessarily the target variable.

---

# Anomaly Detection — Isolation Forest

Isolation Forest was used to identify observations with unusual combinations of numerical features.

The disease label was **not used during anomaly detection**.

The following numerical information was used:

* Soil moisture
* Soil pH
* Temperature
* Rainfall
* Humidity
* Sunlight
* Pesticide usage
* Crop duration
* Latitude
* Longitude
* NDVI

The features were median-imputed and standardized before applying Isolation Forest.

Configuration:

```text
n_estimators = 200
contamination = 0.05
random_state = 42
```

---

## Results

With:

```text
contamination = 0.05
```

the model identified:

```text
25 anomalies
475 normal observations
```

Therefore:

```text
Anomaly rate = 5%
```

Some groups showed higher anomaly rates than others.

For example:

* South India had a relatively high anomaly rate.
* Maize had a relatively high anomaly rate.
* Severe disease had a lower anomaly rate than Mild and Moderate.

However, these differences do not mean that the corresponding regions or crops are faulty.

An anomaly represents an unusual **feature pattern**, not necessarily disease or failure.

---

## Contamination Sensitivity

The number of detected anomalies changes according to the contamination assumption.

| Contamination | Detected Anomalies |
| ------------: | -----------------: |
|          0.02 |                 10 |
|          0.05 |                 25 |
|          0.10 |                 50 |

This demonstrates that anomaly detection results depend strongly on the assumed proportion of abnormal observations.

Therefore, anomaly flags should be treated as **investigation candidates**, rather than confirmed faults.

---

# Part 4 — Robustness Stress Test

## Stress Condition

A deployment scenario was simulated where the:

```text
NDVI sensor is unavailable
```

during evaluation.

The model was **not retrained**.

Instead, the `NDVI_index` feature was replaced with missing values in the test set:

```python
X_stressed["NDVI_index"] = np.nan
```

The existing preprocessing pipeline handles the missing value through median imputation.

This simulates a realistic sensor-availability failure.

---

## Normal vs. Stressed Performance

| Condition        | Accuracy | Macro F1 |
| ---------------- | -------: | -------: |
| Normal           |   44.64% |   0.3991 |
| NDVI unavailable |   35.71% |   0.3091 |
| Change           | -8.93 pp |  -0.0900 |

The Macro F1 score decreased by approximately:

```text
22.5%
```

relative to its original value.

---

## Class-Level Effect

The class order in the confusion matrices is:

```text
Mild, Moderate, Severe
```

### Normal

```text
[[ 6  1 12]
 [ 7  3  7]
 [ 3  1 16]]
```

### NDVI unavailable

```text
[[ 9  1  9]
 [10  1  6]
 [ 9  1 10]]
```

The Moderate class was particularly affected.

Its correct predictions decreased from:

```text
3 / 17
```

to:

```text
1 / 17
```

Severe-class recall also decreased:

```text
80% → 50%
```

Although Mild recall increased, this was partly caused by more Moderate and Severe observations being classified as Mild.

---

# Analysis of Model Failure

The observed failure is primarily associated with **data shift caused by the loss of NDVI information**.

### 1. Data Shift — Primary Factor

During normal training, the model had access to NDVI.

During the stress test, NDVI was unavailable.

Therefore, the evaluation conditions differed from the training conditions.

This represents a deployment-time feature-availability shift.

### 2. Insufficient Representation — Important Secondary Factor

Once NDVI was removed, the remaining features were not sufficient to maintain the original classification performance.

This was especially visible for the Moderate class.

### 3. Model Capacity — Probably Not the Main Cause

The model achieved approximately:

```text
97.7% training accuracy
```

This shows that the model has enough capacity to fit the training data.

Therefore, simple inability to learn the training patterns is unlikely to be the primary problem.

Instead, the problem is generalization and robustness.

### 4. Remaining Experimental Uncertainty

The experiment does not prove that NDVI loss is the **only** cause of failure.

Only one stress condition and one controlled test split were evaluated.

Other possible stress conditions could produce different results.

Therefore, the conclusion is that the model is **sensitive to loss of NDVI information**, rather than claiming NDVI is definitively the sole cause of all model failures.

---

# Overall Findings

The experiments show that the model's performance is **not highly defensible under realistic deployment conditions**.

The major findings are:

1. **Random evaluation is optimistic.**

   * Random test accuracy: approximately 44.6% for seed 42.
   * Mean repeated test accuracy: 35.0%.

2. **Performance changes across splits.**

   * Test accuracy ranged from 30.36% to 44.64%.
   * Macro F1 ranged from 0.276 to 0.399.

3. **Geographical generalization is weak.**

   * Mean leave-one-region-out accuracy was approximately 33%.

4. **The model strongly overfits the training data.**

   * Training accuracy was approximately 97.7%.
   * Test accuracy was only approximately 35.0% on average.

5. **The dataset has weak natural cluster structure.**

   * Best silhouette score was only 0.095 after removing geographic features.

6. **Clusters do not represent disease classes.**

   * Each cluster contained substantial numbers of Mild, Moderate, and Severe observations.

7. **Anomaly detection identifies unusual observations, not necessarily diseased observations.**

   * At 5% contamination, 25 observations were flagged.

8. **The model is sensitive to missing sensor information.**

   * Removing NDVI decreased accuracy by 8.93 percentage points.
   * Macro F1 decreased by 0.0900.

---

# Conclusion

This task demonstrates why a machine learning model should not be considered reliable based solely on a single random train/test split.

The Random Forest classifier achieved very high training accuracy but substantially lower validation and test performance. Repeated evaluation showed considerable variability, while leave-one-region-out testing demonstrated weaker generalization to unseen geographical conditions.

The unsupervised experiments also showed that the dataset does not contain strongly separated natural clusters, and the discovered clusters do not correspond directly to disease classes. Isolation Forest successfully identified unusual observations, but anomaly status was not equivalent to disease severity.

Finally, the robustness experiment demonstrated a significant performance degradation when the NDVI sensor was unavailable. This indicates that the model depends on information that may not always be available during deployment.

Overall, the results show that **model evaluation must consider deployment structure, repeated variability, unsupervised structure, anomaly behavior, and robustness to realistic failures rather than relying on a single favorable test score.**

---

# Reproducibility

The experiments use fixed random seeds where applicable.

### Supervised repeated evaluation

```text
Seeds: 42, 43, 44, 45, 46
```

### Random Forest

```text
n_estimators = 200
max_depth = 8
min_samples_leaf = 5
random_state = 42
```

### K-Means

```text
n_init = 10
random_state = 42
```

### Isolation Forest

```text
n_estimators = 200
contamination = 0.05
random_state = 42
```

All preprocessing is performed through the model pipeline or explicitly before unsupervised/anomaly experiments.

The primary experimental variable in the repeated supervised evaluation is the **data split seed**, while the model configuration remains fixed.
