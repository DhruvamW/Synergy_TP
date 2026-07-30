import pandas as pd

def encode_categorical(x_train, x_val, x_test):
    categorical_columns = x_train.select_dtypes(include=["object"]).columns

    x_train= pd.get_dummies(x_train, columns= categorical_columns, drop_first=True)
    x_val= pd.get_dummies(x_val, columns= categorical_columns, drop_first=True)
    x_test= pd.get_dummies(x_test, columns= categorical_columns, drop_first=True)
    x_train = x_train.reindex(sorted(x_train.columns), axis=1)
    x_val= x_val.reindex(columns=x_train.columns, fill_value=0)
    x_test = x_test.reindex(columns=x_train.columns, fill_value=0)

    return x_train, x_val, x_test

def standardize_features(x_train, x_val, x_test):
    train_mean = x_train.mean()
    train_std = x_train.std()
    train_std = train_std.replace(0, 1)

    scaled_train= (x_train - train_mean) / train_std
    scaled_val= (x_val - train_mean) / train_std
    scaled_test= (x_test - train_mean) / train_std

    return scaled_train, scaled_val, scaled_test, train_mean, train_std
