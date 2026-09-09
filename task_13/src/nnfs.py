import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

file_path = r"Synergy_TP\task_13\data\train.csv"
data = pd.read_csv(file_path)
#print(data.info())
#print(data.head())

data = np.array(data)
m, n=data.shape
np.random.shuffle(data) 
#print(m,n)

"""Test and Validation split along with Transpose"""
train_data = data[0:int(0.8*m), :]
val_data = data[int(0.8*m) : , :]
X_train = train_data[:, 1 : ].T
Y_train = train_data[:, 0]
X_val = val_data[:, 1:].T
Y_val = val_data[:, 0]
#print(X_train.shape)
#print(Y_train.shape)
#print(X_val.shape)
#rint(Y_val.shape)

"""Feature Scaling"""
X_train = X_train / 255.0
X_val = X_val / 255.0

#intialise random weights and biases
def intialize_parameters():
    W1= np.random.rand(10,784) - 0.5
    B1 = np.random.rand(10,1) - 0.5
    W2 = np.random.rand(10,10) - 0.5
    B2 = np.random.rand(10,1) - 0.5

    return (W1, B1, W2, B2)

def ReLU(Z):
    return np.maximum(Z,0)

def softmax(Z):
     exp_Z = np.exp(Z - np.max(Z, axis=0, keepdims=True))
     return exp_Z / np.sum(exp_Z, axis=0, keepdims=True)

def forward_propagation(W1, B1, W2, B2, X_train):
    Z1 = W1.dot(X_train) + B1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + B2
    A2 = softmax(Z2)

    return (Z1, A1, Z2, A2)

def one_hot_encoder(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1

    return one_hot_Y.T


def backward_propagation(W1, B1, W2, B2, Z1, A1, Z2, A2, X, Y, m ):
    one_hot_Y = one_hot_encoder(Y)
    dZ2 = A2 - one_hot_Y
    dW2 = 1/m * dZ2.dot(A1.T)
    dB2 = 1/m * np.sum(dZ2)
    dZ1 = (W2.T).dot(dZ2) * (Z1 > 0)
    dW1 = 1/m * dZ1.dot(X.T)
    dB1 = 1/m * np.sum(dZ1)

    return (dW2, dB2, dW1, dB1)

def update_parameters(W1, B1, W2, B2, dW1, dW2, dB1, dB2, learning_rate):
    W1 -= learning_rate * dW1
    B1 -= learning_rate * dB1
    W2 -= learning_rate * dW2
    B2 -= learning_rate * dB2

    return (W1, B1, W2, B2)

def get_predictions(A2):
    return np.argmax(A2 , 0)

def get_accuracy(predictions, Y):
    return np.sum(predictions == Y) / Y.size

def gradient_descent(X, Y, alpha, iterations):
    W1, B1, W2, B2 = intialize_parameters()

    for i in range(iterations):
        Z1, A1, Z2, A2 = forward_propagation(W1, B1, W2, B2, X_train)
        dW2, dB2, dW1, dB1 = backward_propagation(W1, B1, W2, B2, Z1, A1, Z2, A2, X, Y, m )
        W1, B1, W2, B2 = update_parameters(W1, B1, W2, B2, dW1, dW2, dB1, dB2, alpha)
        if (i%20 == 0):
            print("Iteration Number: ", i)
            print("Accuracy: ", get_accuracy(get_predictions(A2),Y))

    return W1, B1, W2, B2

W1, B1, W2, B2 = gradient_descent(X_train, Y_train, 0.1, 500)

val_index = 0
Z1vval, A1val, Z2val, A2val = forward_propagation(W1, B1, W2, B2, X_val[:,val_index, None])
print("Predicted Label: ",get_predictions(A2val))
print("Actual Label: ", Y_val[val_index])

image_array = X_val[:, 0].reshape(28,28)
plt.imshow(image_array, cmap='gray')
plt.show()

Z1val, A1val, Z2val, A2val = forward_propagation(W1, B1, W2, B2, X_val)
val_acc = get_accuracy(get_predictions(A2val), Y_val)
print("Validation accuracy = ", val_acc)