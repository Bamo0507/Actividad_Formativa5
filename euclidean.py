# -----------------------------------------------------------
# Actividad Formativa
# Integrantes:
# Bryan Martínez 23542
# Luis Mendoza 19644
# Daniela Ramírez 23053
# -----------------------------------------------------------

from lib.utils import validate_positive_integers

def euclidean(a, b):
    if not validate_positive_integers(a, b):
        raise ValueError("Ambos números deben ser enteros positivos.")
    #Vamos reemplazando a y b 
    #Igualamos "a" a "b", y "b" es igual al residuo que se obtiene al hacer a%b
    #Cuando el residuo es 0, se devuelve a, el MCD entre ambos números
    while b != 0:
        a, b = b, a % b
    return a
