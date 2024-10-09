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

def validate_positive_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return False

    if a <= 0 or b <= 0:
        return False

    return True
