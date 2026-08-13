from sklearn.model_selection import train_test_split
from config import (
    TEST_SIZE,
    VALIDATION_SIZE,
    TRAIN_SIZE,
    RANDOM_STATE
)


def split_data(X, y):

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        shuffle=True,
        stratify=y
    )

    validation_fraction = (
        VALIDATION_SIZE /
        (TRAIN_SIZE + VALIDATION_SIZE)
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val,
        y_train_val,
        test_size=validation_fraction,
        random_state=RANDOM_STATE,
        shuffle=True,
        stratify=y_train_val
    )

    return (
        X_train,
        X_val,
        X_test,
        y_train,
        y_val,
        y_test
    )