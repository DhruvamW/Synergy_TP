import numpy as np

def predict(X, weights, bias):
    return np.dot(X, weights) + bias


def train_linear_regression(X, y, learning_rate=0.01, epochs=1000):
    X = np.array(X)
    y = np.array(y)

    rows, cols = X.shape

    weights = np.zeros(cols)
    bias = 0

    losses = []

    for i in range(epochs):

        y_pred = predict(X, weights, bias)

        error = y_pred - y

        # Mean Squared Error Loss
        loss = np.mean(error ** 2)
        losses.append(loss)

        # Calculate gradients
        dw = (2 / rows) * np.dot(X.T, error)
        db = (2 / rows) * np.sum(error)

        # Update parameters
        weights = weights - learning_rate * dw
        bias = bias - learning_rate * db

    return weights, bias, losses


def test_linear_regression(X, weights, bias):
    X = np.array(X)

    return predict(X, weights, bias)