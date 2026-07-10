# Error Analysis

## Regression Errors

The Linear Regression model predicts the CO(GT) concentration using different air quality sensor readings. Although the model performs better than the baseline model, some prediction errors are still present.

Possible reasons for these errors include:

- The relationship between the sensor readings and CO(GT) may not be perfectly linear.
- Some measurements contain noise or uncertainty.
- Missing values were replaced using the median, which may reduce the accuracy of some predictions.
- Environmental conditions such as temperature and humidity can also affect sensor readings.

The Actual vs Predicted plot helps identify where the model makes larger prediction errors.

---

## Classification Errors

The Logistic Regression model predicts whether the pollution level is High or Low.

Classification errors mainly occur when:

- The pollution value is close to the chosen threshold.
- Some sensor readings from different classes are very similar.
- The model assumes a linear decision boundary, which may not perfectly separate the classes.

The confusion matrix shows the number of correctly and incorrectly classified samples and helps identify false positives and false negatives.

---

## Clustering Errors

KMeans clustering groups similar observations without using class labels.

Some limitations of KMeans include:

- The initial centroids are selected randomly, so different runs may produce slightly different clusters.
- The algorithm assumes clusters are roughly spherical.
- Outliers can affect the position of cluster centroids.
- Choosing an inappropriate value of K may reduce clustering quality.

The clustering plot provides a visual representation of how the observations are grouped.

---

## Possible Improvements

The performance of all three models can be improved by:

- Collecting more high-quality data.
- Removing noisy or inconsistent observations.
- Performing better feature selection.
- Tuning hyperparameters such as learning rate, number of epochs, and the number of clusters.
- Trying more advanced machine learning algorithms after establishing these baseline implementations.

---

## Conclusion

The implemented models successfully demonstrate the basic concepts of supervised and unsupervised machine learning. While some prediction and clustering errors remain, the models perform better than the baseline approaches and provide meaningful insights into the AirQualityUCI dataset.