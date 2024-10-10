def factorizacion(n):
    r = "" #Para almacenar el resultado de la fatorización prima 
    i = 2 #Inicializamos el divisor en 2

    while n > 1: #Seguir factorizando mientras n sea mayor a 1
        contador = 0
        while n % i == 0: #mientras n sea divisible por i, se realiza el proceso y aumenta el contador
            contador += 1
            n = n // i
        if contador > 0: #Si i es un factor primo de n, se agrega al resultado
            if contador > 1:
                r += f"{i}^{contador}" #Exponente de i cuando es mayor a 1
            else:
                r += f"{i}" #Cuando exponente = 1
            if n > 1:
                r += "x" #Separar factores
        i += 1
    return r

def main():
    num = int(input("Ingrese un número que sea mayor a 1: "))
    if num <= 1:
        print("El número debe ser mayor a 1")
        return
    
    r = factorizacion(num)
    print("Los factores primos de", f"{num}", "son:", r)

if __name__ == "__main__":
    main()