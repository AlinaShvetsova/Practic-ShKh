import numpy as np;


def SumOfElements():
    if n == m:
        a = np.random.randint(0, 10, (n, m))
        k = 0
        z=[a[i][i] for i in range(n)]
        for i in range(len(z)): 
            k = k + z[i]
        return k
    else: return -1
    
print('Введите размер квадратной матрицы')
n=int(input())
m=int(input())
k = SumOfElements()
if(k == -1): 
    print('Вы ввели размер не квадратной матрицы!')
else: 
    print(k)
print('')
