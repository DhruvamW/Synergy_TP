import pandas as pd

from sklearn.model_selection import train_test_split


def random_split(df, test_size=0.15, validation_size=0.15, random_state=42):
    """
    Stratified random train/validation/test split.
    """

    train_val, test = train_test_split(
        df,
        test_size=test_size,
        stratify=df["crop_disease_status"],
        random_state=random_state
    )

    val_fraction = validation_size / (1 - test_size)

    train, validation = train_test_split(
        train_val,
        test_size=val_fraction,
        stratify=train_val["crop_disease_status"],
        random_state=random_state
    )

    return train, validation, test


def leave_one_region_out(df, test_region, random_state=42):
    """
    Hold out one complete region as the test set.
    The remaining regions are split into training and validation.
    """

    test = df[df["region"] == test_region].copy()

    train_val = df[df["region"] != test_region].copy()

    train, validation = train_test_split(
        train_val,
        test_size=0.1765,
        stratify=train_val["crop_disease_status"],
        random_state=random_state
    )

    return train, validation, test