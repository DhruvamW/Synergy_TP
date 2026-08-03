import numpy as np

def regression_baseline(y_train, X_test):
    mean_value = np.mean(y_train)
    predictions = np.full(X_test.shape[0], mean_value)

    return predictions

def classification_baseline(y_train, X_test):
    majority_class = np.argmax(np.bincount(y_train))
    predictions = np.full(X_test.shape[0], majority_class)

    return predictions