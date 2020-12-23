import numpy as np

#ЗАДАНИЕ 3
def compute_cost(x, y ,theta):
    m = x.shape[0] #количество элементов в X(количество городов)
    x_ones = np.c_[np.ones((m, 1)), x] #добавляем единичный столбец к Х
    h_x = x_ones * theta #вычисление гипотезы для вех городов сразу
    return sum(np.power(h_x - y, 2))/(2*x.shape[0])
