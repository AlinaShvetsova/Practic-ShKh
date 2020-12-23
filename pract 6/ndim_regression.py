#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
from gradient_descent import gradientDescent

if __name__ == '__main__':
    # ЗАДАНИЕ 7
    def normalization(a):
        mean = a.mean(axis = 0)
        std = a.std(axis = 0)
        A = a - mean
        A = A / std
        return mean, std, A
    
    data = np.matrix(np.loadtxt('ex1data2.txt', delimiter=','))
    print('\nМногомерная линейная регрессия по методу градиентного спуска \n')
    x = data[:, :2]
    y = data[:, 2]
    meanX, stdX, X = normalization(x)
    meanY, stdY, Y = normalization(y)
    
    # ЗАДАНИЕ 8
    iteration  = 500
    Area = 3000
    rooms_count = 3
    area = (Area - meanX[0, 0])/stdX[0, 0]
    count = (rooms_count - meanX[0, 1])/stdX[0, 1]
    theta, error = gradientDescent(X, Y, 0.01, 500)
    plt.title('Снижение ошибки при градиентном спуске')
    plt.xlabel('Итерация')
    plt.ylabel('Ошибка')
    plt.xlim(0, iteration)
    plt.plot(error)
    plt.show()
    print("Площадь: ",Area ,"\nКоличество комнат:", rooms_count,"\nПредсказанная цена: ", ((theta[2]*count + theta[1]*area+ theta[0])*stdY + meanY)[0, 0])
    
    def minsquare(x, y):
        m = len(x)
        x=np.c_[np.ones((m, 1)),x]
        theta = np.linalg.pinv(x.transpose()*x)*x.transpose()*y
        return theta
    
    # ЗАДАНИЕ 9
    print('\nМетод наименьших квадратов \n')
    theta = minsquare(x, y)
    theta = theta.view(np.ndarray)
    theta.shape = -1
    print("Площадь: ",Area ,"\nКоличество комнат:", rooms_count,"\nПредсказанная цена: ", (theta[1]*Area + theta[2]*rooms_count+ theta[0]))
    
    # ЗАДАНИЕ 10
    print("\nМетод градиентного спуска:\nФактическая цена: ", (Y[1]*stdY + meanY)[0, 0],"\nПредсказанная цена: ", ((theta[1]*X[1, 0] + theta[2]*X[1, 1]+ theta[0])*stdY + meanY)[0, 0])
    print("\nМетод наименьших квадратов:\nФактическая цена: ", (y[1, 0]),"\nПредсказанная цена: ", (theta[1]*x[1, 0] + theta[2]*x[1, 1]+ theta[0]))