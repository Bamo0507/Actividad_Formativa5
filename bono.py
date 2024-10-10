# -----------------------------------------------------------
# Actividad Formativa
# Integrantes:
# Bryan Martínez 23542
# Luis Mendoza 19644
# Daniela Ramírez 23053
# -----------------------------------------------------------

from lib.utils import validateNumber

def factorizacion(n):
    r = ""  # Para almacenar el resultado de la factorización prima 
    i = 2  # Inicializamos el divisor en 2

    while n > 1:  # Seguir factorizando mientras n sea mayor a 1
        contador = 0
        while n % i == 0:  # Mientras n sea divisible por i, se realiza el proceso y aumenta el contador
            contador += 1
            n = n // i
        if contador > 0:  # Si i es un factor primo de n, se agrega al resultado
            if contador > 1:
                r += f"{i}^{contador}"  # Exponente de i cuando es mayor a 1
            else:
                r += f"{i}"  # Cuando exponente = 1
            if n > 1:
                r += "x"  # Separar factores
        i += 1
    return r

def factor():
    num = input("Ingrese un número que sea mayor a 1: ")
    
    if validateNumber(num):
        num = int(num) 
        r = factorizacion(num)
        print("Los factores primos de", f"{num}", "son:", r)
    else:
        print("El número ingresado es inválido.")

if __name__ == "__main__":
    factor()