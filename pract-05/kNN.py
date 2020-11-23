import numpy as np

def k_nearest(X, y, k, obj, dist_function):
    # нормализация каждого столбца (кроме последнего)
    mx=np.max(X, axis=0)
    norm_X = X/mx
    
    # нормализация объекта obj 
    norm_obj = obj/mx
    
    distance = [dist_function(norm_item, norm_obj) for norm_item in norm_X]
   
    # получение с помощью функции np.argsort индексы соседей по мере их удаления от obj.
    sort = np.argsort(distance, axis=0)
    
    # выборка в отдельный вектор классы k ближайших соседей
    nearest_classes = y[sort[:k]]

    # наиболее часто встречающийся класс в этом векторе
    unique, counts = np.unique(nearest_classes, return_counts=True)
    object_class = unique[np.argmax(counts)]
    return object_class
