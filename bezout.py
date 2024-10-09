from lib.utils import validate_positive_integers
import numpy as np

def bezout(a, b):
    if not validate_positive_integers(a, b):
        raise ValueError("Ambos números deben ser enteros positivos.")
    
    X = np.array([[1, 0],
                  [0, 1]])
    
    while b != 0:
        q = a // b
        
        # Matriz de transformación
        T = np.array([[0, 1],
                      [1, -q]])
        
        X = np.dot(X, T)
        a, b = b, a % b
    
    # La primera columna de X son los coeficientes de Bézout
    x, y = X[0, 0], X[1, 0]
    
    return (x, y)
