import numpy as np
from kNN import k_nearest
import math

# вычисление евклидова расстояния между двумя точками
def EuclideanDistance(p1, p2):
    result1 = math.sqrt(sum((p1-p2)**2))
    return result1

def CityQuarters(a, b):
    # расстояние городских кварталов
    result = math.fabs(a[0] - b[0]) + math.fabs(a[1] - b[1])
    # в результате получаем сумму модулей разностей координат между двумя точками
    return result


X = np.array([[33, 21, 1],
              [41, 13, 1],
              [18, 22, 1],
              [38, 34, 1],
              [62, 118, 2],
              [59, 137, 2],
              [95, 131, 2],
              [83, 110, 2],
              [185, 155, 3],
              [193, 129, 3],
              [164, 135, 3],
              [205, 131, 3],
              [145, 55, 4],
              [168, 35, 4],
              [135, 47, 4],
              [138, 66, 4]])


height = int(input("Введите рост: "))
weight = int(input("Введите вес: "))
obj = np.array([height, weight])
k = 3
object_class = k_nearest(X[:, 0:-1], X[:,2], k, obj, EuclideanDistance)
# вывод результата классификации
monkeys = {1: 'lemur', 2: 'schimpanze', 3: 'gorilla', 4: 'orangutan'}
print(monkeys[object_class])

