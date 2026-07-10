import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def predict_probability(X, weights, bias):
    linear = np.dot(X, weights) + bias

    return sigmoid(linear)


def train_logistic_regression(X, y, learning_rate=0.01, epochs=1000):
    X = np.array(X)
    y = np.array(y)

    rows, cols = X.shape

    weights = np.zeros(cols)
    bias = 0

    losses = []

    for i in range(epochs):

        y_pred = predict_probability(X, weights, bias)

        # Binary Cross Entropy Loss
        loss = -np.mean( y * np.log(y_pred + 1e-9) + (1 - y) * np.log(1 - y_pred + 1e-9))

        losses.append(loss)

        error = y_pred - y

        dw = (1 / rows) * np.dot(X.T, error)

        db = (1 / rows) * np.sum(error)

        weights = weights - learning_rate * dw

        bias = bias - learning_rate * db

    return weights, bias, losses


def test_logistic_regression(X, weights, bias):
    X = np.array(X)

    probabilities = predict_probability(X, weights, bias)

    predictions = []

    for p in probabilities:
        if p >= 0.5:
            predictions.append(1)
        else:
            predictions.append(0)

    return np.array(predictions)