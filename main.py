from bono import factor
from euclidean import euclidean
from bezout import bezout
from criba import get_primes
from isPrime import is_prime
from lib.utils import validate_positive_integers
import sys

def euclidean_menu():
    print("---------- Algoritmo Euclidiano ----------")
    try:
        a_input = input("Ingrese un entero positivo a: ")
        b_input = input("Ingrese un entero positivo b: ")
        
        a = int(a_input)
        b = int(b_input)
        
        if not validate_positive_integers(a, b):
            print("Error: Ambos números deben ser enteros positivos.")
            return
        
        # Calcular el MCD usando la función euclidean
        mcd = euclidean(a, b)
        print(f"El MCD de {a} y {b} es {mcd}.")
        
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingrese números enteros positivos.")
    print("-----------------------------------------")

def bezout_menu():
    print("---------- Coeficientes de Bézout ----------")
    try:
        a_input = input("Ingrese un entero positivo a: ")
        b_input = input("Ingrese un entero positivo b: ")
        
        a = int(a_input)
        b = int(b_input)
        
        if not validate_positive_integers(a, b):
            print("Error: Ambos números deben ser enteros positivos.")
            return
        
        # Calcular los coeficientes de Bézout usando la función bezout
        x, y = bezout(a, b)
        print(f"Los coeficientes de Bézout de {a} y {b} son {x} y {y}, respectivamente.")
        
    except ValueError as ve:
        print(f"Error: {ve}")
    print("---------------------------------------------")

def criba_menu():
    get_primes()

def is_prime_menu():
    is_prime()

def factor_menu():
    factor()


def main_menu():
    while True:
        print("\n========== Menú de Algoritmos ==========")
        print("1. Criba de Eratóstenes")
        print("2. Verificar si un número es primo")
        print("3. Algoritmo Euclidiano (MCD)")
        print("4. Coeficientes de Bézout")
        print("5. Factorización prima")
        print("6. Salir")
        print("=========================================")
        
        choice = input("Seleccione una opción (1-6): ")
        
        if choice == '1':
            criba_menu()
        elif choice == '2':
            is_prime_menu()
        elif choice == '3':
            euclidean_menu()
        elif choice == '4':
            bezout_menu()
        elif choice == '5':
            factor_menu()
        elif choice == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            sys.exit()
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    main_menu()
