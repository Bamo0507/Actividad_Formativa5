from lib.utils import validateNumber
import numpy as np
from criba import criba

def Test_Primalidad(n):
    prime_list = criba(int(np.sqrt(n))) 
    for i in prime_list:
        if n % i == 0:
            return i
    return True

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
