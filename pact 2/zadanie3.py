import numpy as np


print('Введите  размер матрицы: \t')
n = int(input())
print('Введите  матрицу: \t')
a = np.random.randint(0,10,(n))
b = np.zeros(n)
c = np.zeros(n)
print (a) # вывод Массива
print('Введите  число, на которое сместить массив: \t')
x = int(input())

t = x

while t <= n - x:
    b[t] = a[t-x]
    t=t+1

t = 0
while t < x:
    c[t] = a[n-x+t]
    t=t+1

print(' ', a ,'\n' , b, '\n' ,'\n', c, '\n', b+c)

