from lib.utils import validateNumber

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
