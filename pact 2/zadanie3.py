import numpy as np

def СyclicShift(a):
    b = a[x:]+a[:x]
    return b

a = [1, 2, 3, 4, 5]  
print (a) # вывод Массива
print('Введите  число, на которое сместить массив: \t')
x = int(input())
print(СyclicShift(a))
print('')
