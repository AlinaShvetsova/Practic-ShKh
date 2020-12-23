import numpy as np

#ЗАДАНИЕ 4
def gradientDescent(x, y, alpha, iterations):
    m=x.shape[0]
    error = []
    x = np.array(x)
    y = y.view(np.ndarray)
    y.shape = -1
    x=np.c_[np.ones((m, 1)),x]
    n = x.shape[1]
    xTrans = x.T
    theta=np.ones(n)
    for i in range(0, iterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        cost = np.sum(loss ** 2) / (2 * m)
        error.append(cost)
        gradient = np.dot(xTrans, loss) / m
        theta = theta - alpha * gradient
    return theta, error

