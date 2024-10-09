from lib.utils import validate_positive_integers

def euclidean(a, b):
    if not validate_positive_integers(a, b):
        raise ValueError("Ambos números deben ser enteros positivos.")
    
    while b != 0:
        a, b = b, a % b
    return a