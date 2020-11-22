import numpy as np

def k_nearest(X, y, k, obj, CityQuarters):
   
    # нормализация каждого столбца (кроме последнего)
    mx=np.max(X, axis=0)
    norm_X = X/mx
    
    # нормализация объекта obj 
    m = X.shape[0]
    norm_obj = obj/mx
    
    distance = np.zeros((m, X.shape[1]))
    for i in range(m):
        distance[i] = CityQuarters(norm_X[i], norm_obj)
   
    # получение с помощью функции np.argsort индексы соседей по мере их удаления от obj.
    sort = np.argsort(distance, axis=0)
    
    # выборка в отдельный вектор классы k ближайших соседей
    nearest_classes = np.zeros((k))
    for i in range(k):
        index = sort[i,0]
        nearest_classes[i] = y[index] 

    # наиболее часто встречающийся класс в этом векторе
    unique, counts = np.unique(nearest_classes, return_counts=True)
    object_class = unique[np.argmax(counts)]
    return object_class
