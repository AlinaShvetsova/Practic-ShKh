import numpy as np
from sigmoid import sigmoid

# ЗАДАНИЕ 5
def predict(Theta1, Theta2, X):
    m = X.shape[0]
    ones = np.ones((m))
    a1 = np.c_[ones, X]
    z2 = np.dot(a1, Theta1.T)
    a2 = sigmoid(z2)
    a3 = np.c_[np.ones(a2.shape[0]), a2]
    z3 = np.dot(a3, Theta2.T)
    h_x = sigmoid(z3)
    p = np.argmax(h_x, axis=1)+1  
    return p
