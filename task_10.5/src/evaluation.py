from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np
import pandas as pd


def evaluate_model(model, X, y):
    y_pred = model.predict(X)

    mae = mean_absolute_error(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    r2= r2_score(y, y_pred)
    rmse = np.sqrt(mse)

    return {"MAE": mae,
            "MSE" : mse,
            "R2" : r2,
            "RMSE" : rmse}


def largest_errors(model, X, y, n=10):

    y_pred = model.predict(X)

    errors = np.abs(y - y_pred)

    error_df = pd.DataFrame({
        "Actual": y,
        "Predicted": y_pred,
        "Absolute Error": errors
    })

    return error_df.sort_values(by="Absolute Error", ascending=False).head(n)