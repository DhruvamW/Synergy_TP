import numpy as np

def mae(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))


def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def rmse(y_true, y_pred):
    return np.sqrt(mse(y_true, y_pred))


def r2_score(y_true, y_pred):

    ss_res = np.sum((y_true - y_pred) ** 2)

    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)

    return 1 - (ss_res / ss_tot)


def accuracy(y_true, y_pred):

    return np.mean(y_true == y_pred)


def confusion_matrix(y_true, y_pred):

    tp = np.sum((y_true == 1) & (y_pred == 1))

    tn = np.sum((y_true == 0) & (y_pred == 0))

    fp = np.sum((y_true == 0) & (y_pred == 1))

    fn = np.sum((y_true == 1) & (y_pred == 0))

    return np.array([[tn, fp], [fn, tp]])


def precision(y_true, y_pred):

    cm = confusion_matrix(y_true, y_pred)

    tp = cm[1][1]

    fp = cm[0][1]

    if tp + fp == 0:
        return 0

    return tp / (tp + fp)


def recall(y_true, y_pred):

    cm = confusion_matrix(y_true, y_pred)

    tp = cm[1][1]

    fn = cm[1][0]

    if tp + fn == 0:
        return 0

    return tp / (tp + fn)


def f1_score(y_true, y_pred):

    p = precision(y_true, y_pred)

    r = recall(y_true, y_pred)

    if p + r == 0:
        return 0

    return (2 * p * r) / (p + r)


def inertia(X, labels, centroids):

    total = 0

    for i in range(len(X)):
        cluster = labels[i]
        total += np.sum((X[i] - centroids[cluster]) ** 2)

    return total


def cluster_counts(labels):

    unique, counts = np.unique(labels, return_counts=True)

    cluster_dict = {}

    for i in range(len(unique)):
        cluster_dict[int(unique[i])] = int(counts[i])

    return cluster_dict


def silhouette_score(X, labels):

    return 0