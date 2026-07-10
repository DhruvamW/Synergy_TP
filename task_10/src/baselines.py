import numpy as np

def regression_baseline(y_train, X_test):
    mean_value = np.mean(y_train)

    predictions = np.full(len(X_test), mean_value)

    return predictions


def classification_baseline(y_train, X_test):
    values, counts = np.unique(y_train, return_counts=True)

    majority_class = values[np.argmax(counts)]

    predictions = np.full(len(X_test), majority_class)

    return predictions


def clustering_baseline(kmeans_model, X):
    labels = kmeans_model.fit_predict(X)

    return labels