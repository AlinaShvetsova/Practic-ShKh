import numpy as np

def Task3(a):
    b = np.zeros(len(a))
    b[:len(a[x:])] = a[x:]
    b[len(a[x:]):] = a[:x]
    return b

a = [1, 2, 3, 4, 5]  
print (a) # вывод Массива
print('Введите  число, на которое сместить массив: \t')
x = int(input())
print(Task3(a))