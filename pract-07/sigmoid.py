import math

# ЗАДАНИЕ 4    
def sigmoid(z):
    g_z = 1 / (1 + math.e ** -z)  
    return g_z
