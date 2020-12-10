import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

#ЗАДАНИЕ 1
data = np.matrix(np.loadtxt('ex1data1.txt', delimiter=','))

#ЗАДАНИЕ 2
x = []
y = []
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

#ЗАДАНИЕ 3
def compute_cost(x, y ,theta):
    m = x.shape[0] #количество элементов в X(количество городов)
    x_ones = np.c_[np.ones((m, 1)), x] #добавляем единичный столбец к Х
    h_x = x_ones * theta #вычисление гипотезы для вех городов сразу
    return sum(np.power(h_x - y, 2))/(2*x.shape[0])
print("\nКвадратичная ошибка:", compute_cost(x, y, theta)[0, 0])

#ЗАДАНИЕ 4
def gradientDescent(x, y, alpha, iterations):
    m=x.shape[0]
    mass1 = []
    mass2 = []
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
        mass1.append(i)
        mass2.append(cost)
        gradient = np.dot(xTrans, loss) / m
        theta = theta - alpha * gradient
    return theta, mass1, mass2
alpha = 0.02
iteration  = 500
theta, mass1, mass2 = gradientDescent(x, y, alpha, iteration)
plt.title('Снижение ошибки при градиентном спуске')
plt.xlabel('Итерация')
plt.ylabel('Ошибка')
plt.xlim(0, iteration)
plt.plot(mass1, mass2)
plt.show()
print(theta)
population  = 50
print("Численность в 10 тыс. человек:",population ,"\nПрибыльность в 10.000 кратном размере: " ,theta[1]*population + theta[0] )
X_1 = np.arange(min(x), max(x))

def minsquare(x , y):
    m = len(x)
    x=np.c_[np.ones((m, 1)),x]
    theta = np.linalg.pinv(x.transpose()*x)*x.transpose()*y
    return theta


# ЗАДАНИЕ 6
plt.plot(X_1, theta[1]*X_1 + theta[0], 'g--')
plt.plot(x, y, 'b.')
plt.xlabel('Численность')
plt.ylabel('Прибыльность')
plt.title('График линейной зависимости')
plt.xlim(0, 25)
plt.ylim(-5, 25)
plt.grid()
plt.show()
print("Фактическая цена: ", y[9],"\nПредсказанная цена: ",theta[1]*x[9] + theta[0])

# ЗАДАНИЕ 7
def normalization(a):
    mean = a.mean(axis = 0)
    std = a.std(axis = 0)
    A = a - mean
    A = A / std
    return mean, std, A

data2 = np.matrix(np.loadtxt('ex1data2.txt', delimiter=','))
print('\nМногомерная линейная регрессия по методу градиентного спуска \n')
x2 = data2[:, :2]
y2 = data2[:, 2]
meanX, stdX, X = normalization(x2)
meanY, stdY, Y = normalization(y2)

# ЗАДАНИЕ 8
Area = 3000
Count = 3
area = (Area - meanX[0, 0])/stdX[0, 0]
count = (Count - meanX[0, 1])/stdX[0, 1]
theta, mass1, mass2 = gradientDescent(X, Y, 0.01, 500)
plt.title('Снижение ошибки при градиентном спуске')
plt.xlabel('Итерация')
plt.ylabel('Ошибка')
plt.xlim(0, iteration)
plt.plot(mass1, mass2)
plt.show()
print("Площадь: ",Area ,"\nКоличество комнат:", Count,"\nПредсказанная цена: ", ((theta[2]*count + theta[1]*area+ theta[0])*stdY + meanY)[0, 0])

# ЗАДАНИЕ 9
print('\nМетод наименьших квадратов \n')
theta_2 = minsquare(x2, y2)
theta_2 = theta_2.view(np.ndarray)
theta_2.shape = -1
print("Площадь: ",Area ,"\nКоличество комнат:", Count,"\nПредсказанная цена: ", (theta_2[1]*Area + theta_2[2]*Count+ theta_2[0]))

# ЗАДАНИЕ 10
print("\nМетод градиентного спуска:\nФактическая цена: ", (Y[1]*stdY + meanY)[0, 0],"\nПредсказанная цена: ", ((theta[1]*X[1, 0] + theta[2]*X[1, 1]+ theta[0])*stdY + meanY)[0, 0])
print("\nМетод наименьших квадратов:\nФактическая цена: ", (y2[1, 0]),"\nПредсказанная цена: ", (theta_2[1]*x2[1, 0] + theta_2[2]*x2[1, 1]+ theta_2[0]))
