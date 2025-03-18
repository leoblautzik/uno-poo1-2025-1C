"""Escribir una función consonantes que recibe una cadena 
de caracteres y devuelve la cadena que resulta de eliminar 
todas las vocales de la cadena recibida. 
Por ejemplo: consonantes("hola como estas"); 
devuelve "hl cm sts"
"""


def consonantes(cadena):
    """Devuelve un string que es equivalente al pasado por parametro
    pero sin vocales
    """
    vocales = "aeiouüAEIOUáéíóúÁÉÍÓÚäëïö"
    sin_vocales = ""
    for letra in cadena:
        if letra not in vocales:
            sin_vocales += letra

    return sin_vocales


def main():
    """main"""
    print(consonantes("hola como estas"))
    print(consonantes("hola cómo estás"))


if __name__ == "__main__":
    main()
