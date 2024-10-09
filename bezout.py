from lib.utils import validate_positive_integers
import numpy as np

def bezout(a, b):
    if not validate_positive_integers(a, b):
        raise ValueError("Ambos números deben ser enteros positivos.")
    
    # Inicializar la matriz identidad 2x2
    X = np.array([[1, 0],
                  [0, 1]])
    
    while b != 0:
        q = a // b
        
        # Matriz de transformación
        T = np.array([[0, 1],
                      [1, -q]])
        
        # Actualizar la matriz X
        X = np.dot(X, T)
        
        # Actualizar a y b
        a, b = b, a % b
    
    # Los coeficientes de Bézout son los elementos de la primera columna de X
    x, y = X[0, 0], X[1, 0]
    
    return (x, y)