# -----------------------------------------------------------
# Actividad Formativa
# Integrantes:
# Bryan Martínez 23542
# Luis Mendoza 19644
# Daniela Ramírez 23053
# -----------------------------------------------------------

from lib.utils import validateNumber
import numpy as np
from criba import criba

def Test_Primalidad(n):
    #Dado un número "n" se evalúa la raíz del número y se toma el entero de esta operación
    prime_list = criba(int(np.sqrt(n))) 
    #Se recorre la lista de números primos que anteceden al número obtenido previamente
    #Se analiza si deviden al número "n" que dio el usuario
    for i in prime_list:
        if n % i == 0:
            return i #Si dividen al número, se devuelve el divisor
    return True #Si no dividen al número, se devuelve True

#Menú a visualizar por el usuario al seleccionar el Test de Primalidad
def is_prime():
    print("---------- Verificación de Primalidad ----------")
    validNumber = False
    inputNumber = None
    
    while not validNumber:
        inputNumber = input("Ingrese un entero positivo n: ")
        validNumber = validateNumber(inputNumber)
    
    inputNumber = int(inputNumber)
    
    testPrimalidad = Test_Primalidad(inputNumber)
    
    if testPrimalidad == True:
        print(f"El número {inputNumber} es primo.")
    else:
        print(f"El número {inputNumber} no es primo, pues lo divide {testPrimalidad}.")
    
    print("-----------------------------------------------")
