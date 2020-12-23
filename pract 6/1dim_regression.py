import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from compute_cost import compute_cost
from gradient_descent import gradientDescent

if __name__ == '__main__':
    #ЗАДАНИЕ 1
    data = np.matrix(np.loadtxt('ex1data1.txt', delimiter=','))
    
    #ЗАДАНИЕ 2
    font = {'family': 'Verdana', 'weight' : 'normal'}
    rc('font', **font)
    x = data[: , 0]
    y = data[: , 1]
    plt.plot(x, y, 'b.')
    plt.xlabel('Численность')
    plt.ylabel('Прибыльность')
    plt.title('Зависимость прибыльности от численности')
    plt.grid()
    plt.xlim(0, 25)
    plt.ylim(-5, 25)
    plt.show()
    theta = np.matrix('[1; 2]')
     
    print("\nКвадратичная ошибка:", compute_cost(x, y, theta)[0, 0])
        
    alpha = 0.02
    iteration  = 500
    theta, error = gradientDescent(x, y, alpha, iteration)
    plt.title('Снижение ошибки при градиентном спуске')
    plt.xlabel('Итерация')
    plt.ylabel('Ошибка')
    plt.xlim(0, iteration)
    plt.plot(error)
    plt.show()
    print(theta)
    population  = 50
    print("Численность в 10 тыс. человек:",population ,"\nПрибыльность в 10.000 кратном размере: " ,theta[1]*population + theta[0] )
        
    # ЗАДАНИЕ 6
    plt.plot(x, theta[1]*x + theta[0], 'g--')
    plt.plot(x, y, 'b.')
    plt.xlabel('Численность')
    plt.ylabel('Прибыльность')
    plt.title('График линейной зависимости')
    plt.xlim(0, 25)
    plt.ylim(-5, 25)
    plt.grid()
    plt.show()
    print("Фактическая цена: ", y[9],"\nПредсказанная цена: ",theta[1]*x[9] + theta[0]) 