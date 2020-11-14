import numpy as np
import matplotlib.pyplot as plt
import scipy.io

# ЗАДАНИЕ №1 
a=10
print('a =' ,a)

arr = np.array([1, 2, 3])
print('Матрица с заданными значениями 1\n', arr)

arr1 = [[1], [1, 2], [1, 2, 3]]
print('Матрица  \n', arr1)

arr2 = np.zeros((3, 2))
print('Матрица с нулевыми значениями 2 \n', arr2)

arr3 = np.ones((2, 3))
print('Матрица с единичными значениями \n', arr3)

arr4 = np.random.randint(2, 6, (3, 3))
print('Матрица с случайными целочисленными значениями \n',arr4)

# ЗАДАНИЕ №2
data = np.loadtxt(r'text.txt', dtype=np.int32)
print('Переменные из текстового файла \n')
print(data)

# ЗАДАНИЕ №3
data1 = scipy.io.loadmat(r'var3.mat')
dataA = data1['n']
maxx = np.max(dataA) # максимальная 
print('Рассчет максимального = ', maxx)

minn = np.min(dataA) # минимальная 
print('Рассчет минимального = ', minn)

med = np.median(dataA) # медиана
print('Рассчет медианы = ', med)

mato = np.mean(dataA) # мат. ожидание
print('Рассчет математического ожидания = ', mato)

dis = np.var(dataA) # дисперсия
print('Рассчет дисперсии = ',dis)

srotk = np.std(dataA) # среднеквадратическое отклонение 
print('Рассчет среднеквадратического отклонения = ', srotk)

# ЗАДАНИЕ №4
plt.plot(dataA)
plt.show()
mean = np.mean(dataA) * np.ones(len(dataA))
var = np.var(dataA) * np.ones(len(dataA))
plt.plot(dataA, 'b-', mean, 'r-', mean-var, 'g--', mean+var, 'g--')
plt.grid()
plt.show()
plt.hist(dataA, bins=20)
plt.grid()
plt.show()

# ЗАДАНИЕ №5
def autocorrelate(a):
 n = len(a)
 cor = []
 
 for i in range(n//2, n//2+n):
  a1 = a[:i+1]   if i< n else a[i-n+1:]
  a2 = a[n-i-1:] if i< n else a[:2*n-i-1]
  cor.append(np.corrcoef(a1, a2)[0, 1])
 return np.array(cor)

dataA = np.ravel(dataA)
cor = autocorrelate(dataA)
plt.plot(cor)
plt.show()

# ЗАДАНИЕ №6
data2 = scipy.io.loadmat(r'var2.mat')
dataB = data2['mn']

# ЗАДАНИЕ №7
n = dataB.shape[1]
corr_matrix = np.zeros((n, n))
for i in range(0, n):
  for j in range(0, n):
    col = dataB[:, i] # выбор i-го столбца 
    col2 = dataB[:, j] # выбор j-го столбца 
    corr_matrix[i,j] = np.corrcoef(col, col2)[0, 1]
np.set_printoptions(precision=2)
print(corr_matrix)

plt.plot(dataB[:, 2], dataB[:, 5], 'b.')
plt.grid()
plt.show()
