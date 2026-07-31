import numpy as np

class LinearRegression:
    def __init__(self, learning_rate, epochs):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0
        self.loss_history = []

    def predict(self, x):
        y = x @ self.weights + self.bias
        return y

    def compute_cost(self, x, y):
        prediction = self.predict(x)
        error = prediction - y
        error_squared = error ** 2
        mse = np.mean(error_squared)

        return mse

    def compute_gradients(self, x, y):
        prediction = self.predict(x)
        error = prediction - y
        dw = (1/x.shape[0])*(x.T)@(error)
        db= (1/x.shape[0])*np.sum(error)

        return dw , db


    def fit(self, x, y):
        self.weights = np.zeros(X.shape[1])
        self.bias = 0

        for epoch in range(self.epochs):
            current_loss= self.compute_cost(x,y)
            dw, db= self.compute_gradients(x,y)
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db