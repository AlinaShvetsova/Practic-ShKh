import numpy as np
import math


print("Введите размер матрицы")
n = int(input())
a = np.random.randint(0,10,(n))
b = np.random.randint(0,10,(n))

print(a, '\n', b)

diff = [(a[i] - b[i])**2 for i in range(len(a))]
print(diff)

sumEl = sum(diff)
print(sumEl)

evRast = math.sqrt(sumEl)
print(evRast)