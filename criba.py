# -----------------------------------------------------------
# Actividad Formativa
# Integrantes:
# Bryan Martínez 23542
# Luis Mendoza 19644
# Daniela Ramírez 23053
# -----------------------------------------------------------

from lib.utils import validateNumber

def criba(n):
    primeNumbers = []
    compoundNumbers = set()
    #ciclo for para recorrer números del 2 hasta n
    for i in range(2, n+1):
        #Si es compuesto pasamos al siguiente número
        if i in compoundNumbers:
            continue
        
        #Recorremos los múltiplos del número de la presente iteración
        #Agregamos todos a "compound numbers"
        for j in range(i*2, n+1, i):
            compoundNumbers.add(j)
        #Si el número no ha sido múltiplo de nadie, se agrega a prime numbers   
        primeNumbers.append(i)
        
    return primeNumbers

#Menú de interacción que verá el usuario al seleccionar la opción de la criba
def get_primes():
    print("---------- Criba de Eratóstenes ----------")
    validNumber = False
    inputNumber = None
    
    while not validNumber:
        inputNumber = input("Ingrese un entero positivo n: ")
        validNumber = validateNumber(inputNumber)
    
    inputNumber = int(inputNumber)
    primeNumbers = criba(inputNumber)
    
    print(f"Los primos menores o iguales a {inputNumber} son {primeNumbers}")  
    print("------------------------------------------")
