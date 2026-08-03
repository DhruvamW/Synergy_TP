import numpy as np

# Regression
def mean_squared_error(y_true, y_pred):
    error = y_pred - y_true
    error_squared = error **2
    mse = np.mean(error_squared)

    return mse

def root_mean_squared_error(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

def mean_absolute_error(y_true, y_pred):
    error = y_pred - y_true
    mae = np.mean(np.abs(error))

    return mae

def r2_score(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)

    if ss_tot == 0:
        return 0.0

    return 1 - (ss_res / ss_tot)


# Classification
def confusion_matrix(y_true, y_pred):
   
   tp = np.sum((y_true == 1) & (y_pred == 1))
   fn = np.sum((y_true == 1) & (y_pred == 0))
   fp = np.sum((y_true == 0) & (y_pred == 1))
   tn = np.sum((y_true == 0) & (y_pred == 0))

   matrix = {"tn": tn,
            "fp": fp,
            "fn": fn,
            "tp": tp }
   
   return matrix
   

def accuracy(y_true, y_pred):
    matrix = confusion_matrix(y_true, y_pred)
    tp = matrix["tp"]
    fp = matrix["fp"]
    fn = matrix["fn"]
    tn = matrix["tn"]

    if tp + tn + fn + fp == 0:
        return 0.0
    accuracy = (tp + tn) / (tp + tn + fn + fp)

    return accuracy

def precision(y_true, y_pred):
    matrix = confusion_matrix(y_true, y_pred)
    tp = matrix["tp"]
    fp = matrix["fp"]
    fn = matrix["fn"]
    tn = matrix["tn"]

    if tp + fp == 0:
        return 0.0
    precision = tp / (tp + fp)

    return precision

def recall(y_true, y_pred):
    matrix = confusion_matrix(y_true, y_pred)
    tp = matrix["tp"]
    fp = matrix["fp"]
    fn = matrix["fn"]
    tn = matrix["tn"]
    
    if tp + fn == 0:
        return 0.0
    recall = tp / (tp + fn)

    return recall


def f1_score(y_true, y_pred):
    precision_val = precision(y_true,y_pred)
    recall_val = recall(y_true,y_pred)

    if precision_val + recall_val == 0:
        return 0.0
    f1 = 2 * ((precision_val * recall_val)/(precision_val + recall_val))

    return f1