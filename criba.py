"""
---------- Actividad Formativa 5 ----------
---------- Inciso 1 ----------
---------- Criba ----------
"""

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
"""
-------------- Lógica del Programa -------------------
"""
print("-------------------------------------------------")
validNumber = False
inputNumber = None

while not validNumber:
    inputNumber = input("Ingrese un entero positivo n: ")
    validNumber = validateNumber(inputNumber)

inputNumber = int(inputNumber)
primeNumbers = criba(inputNumber)

print(f"Los primos menores o iguales a {inputNumber} son {primeNumbers}")  
print("-------------------------------------------------")

            