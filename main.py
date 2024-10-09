from euclidean import euclidean
from bezout import bezout
from lib.utils import validate_positive_integers

def main():
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
        print(f"El mcd de {a} y {b} es {mcd}.")
        
        # Calcular los coeficientes de Bézout usando la función bezout
        x, y = bezout(a, b)
        print(f"Los coeficientes de Bézout de {a} y {b} son {x} y {y}, respectivamente.")
        
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingrese números enteros positivos.")

if __name__ == "__main__":
    main()