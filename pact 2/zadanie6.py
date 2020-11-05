import numpy as np;


def func(n):
    
    print('Введите размер квадратной матрицы')
    n=int(input())
    if n % 2 == 0:
        a = np.random.randint(0, 10, (n, n))
        z=[a[i][i] for i in range(n)]
        print('Полученная матрица')
        print(a)
        print('Массив элементов на главной диагонали')
        print(z)
        print('Результат')
        print(sum(z))
    else:
        print('Вы ввели размер не квадратной матрицы!')
func('n')