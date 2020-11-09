import numpy as np
import math


def EuclideanDistance():
    diff = [(a[i] - b[i])**2 for i in range(len(a))]
    sumEl = sum(diff)
    evRast = math.sqrt(sumEl)
    return evRast
    
print("Введите размер матрицы")
n = int(input())
a = np.random.randint(0,10,(n))
b = np.random.randint(0,10,(n))
print(a, '\n', b)
print(EuclideanDistance())
print('')
