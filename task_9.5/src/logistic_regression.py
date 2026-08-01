import numpy as np

class LogisticRegression: 
    def __init__(self, learning_rate, epochs):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0
        self.loss_history = []

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def predict_probability(self, x):
        z = x @ self.weights + self.bias
        return self.sigmoid(z)
    
    def predict(self, x):
        probabilities = self.predict_probability(x)
        return (probabilities >= 0.5).astype(int)

    def compute_loss(self, x, y):
        probabilities = self.predict_probability(x)
        probabilities = np.clip(probabilities, 1e-15, 1 - 1e-15)

        binary_cross_entropy= (-1/x.shape[0])*np.sum(y*np.log(probabilities) + (1-y)*np.log(1-probabilities))

        return binary_cross_entropy


    def compute_gradients(self, X, y):
        probabilities = self.predict_probability(X)
        error = probabilities - y

        dw = (1 / X.shape[0]) * (X.T @ error)
        db = (1 / X.shape[0]) * np.sum(error)

        return dw, db

    def fit(self, x, y):
        self.weights = np.zeros(x.shape[1])
        self.bias = 0

        for epoch in range(self.epochs):
            current_loss= self.compute_loss(x,y)
            self.loss_history.append(current_loss)
            dw, db= self.compute_gradients(x,y)
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db