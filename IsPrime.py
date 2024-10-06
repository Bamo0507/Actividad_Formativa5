"""
---------- Actividad Formativa 5 ----------
---------- Inciso 2 ----------
---------- Is Prime ----------
"""

#IMPORTS UTILIZADOS
import numpy as np

#FUNCIONES
##########################################
def criba(n):
    primeNumbers = []
    compoundNumbers = set()
    
    #ciclo for para recorrer números del 2 hasta n
    for i in range(2, n+1):
        if i in compoundNumbers:
            continue
        
        for j in range(i*2, n+1, i):
            compoundNumbers.add(j)
            
        primeNumbers.append(i)
        
    return primeNumbers
##########################################
def validateNumber(n):
    try:
        number = int(n)
        if number <= 0 or number == 1:
            print("El número seleccionado es inválido, no puede ser negativo, ni igual a 1 o 0.")
            return False
        else:
            return True
    except ValueError:
        print("El input no es un número entero.\nPor favor, vuelva a intentarlo.\n")
        return False
##########################################

def Test_Primalidad(n):
  prime_list = criba(int(np.sqrt(n))) 
  for i in prime_list:
    if n % i == 0:
      return i
  return True


#PROGRAMA PRINCIPAL
print("-------------------------------------------------")
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

print("--------------------------------------------------")