import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from config import *

def load_data(filepath):
    df = pd.read_csv(filepath)

    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    return X , y

def split_data(X, y):

    X_train_val, X_test, y_train_val, y_test = train_test_split(
    X,
    y,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE,
    shuffle=True)

    validation_fraction = VALIDATION_SIZE / (TRAIN_SIZE + VALIDATION_SIZE)

    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val,
        y_train_val,
        test_size= validation_fraction,
        random_state= RANDOM_STATE,
        shuffle= True
    )

    return (X_train, X_val, X_test, y_train, y_val, y_test)



    