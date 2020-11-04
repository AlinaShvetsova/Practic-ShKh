import numpy as np;

print('Введите размер квадратной матрицы')
n=int(input())
a = np.random.randint(0, 10, (n, n))
z=[a[i][i] for i in range(n)]
print('Полученная матрица')
print(a)
print('Массив элементов на главной диагонали')
print(z)
print('Результат')
print(sum(z))