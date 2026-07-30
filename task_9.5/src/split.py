import pandas as pd
import numpy as np

def train_val_test_split(x, y, train_size=0.7, val_size=0.15, test_size=0.15, random_state=42):
    if not np.isclose(train_size + val_size + test_size, 1.0):
        raise ValueError("Train, validation and test sizes must sum to 1.")
        return
    
    n_samples= x.shape[0]
    indices = np.arange(n_samples)
    np.random.seed(random_state)
    np.random.shuffle(indices)

    x = x.iloc[indices].reset_index(drop=True)
    y = y.iloc[indices].reset_index(drop=True)

    train_end = int(n_samples * train_size)
    val_end = train_end + int(n_samples * val_size)

    x_train = x.iloc[:train_end]
    x_val= x.iloc[train_end:val_end]
    x_test= x.iloc[val_end:]
    y_train = y.iloc[:train_end]
    y_val = y.iloc[train_end:val_end]
    y_test= y.iloc[val_end:]

    return x_train, x_val, x_test, y_train, y_val, y_test