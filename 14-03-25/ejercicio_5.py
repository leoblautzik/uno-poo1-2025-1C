"""Leer dos valores numéricos enteros e indicar cual es el 
mayor y cual es el menor. 
Considerar que ambos valores son diferentes
"""


def mayor(a, b):
    """Devuelve el mayor de dos numeros"""
    if a > b:
        return a
    return b


def menor(a, b):
    """Devuelve el menor de dos numeros"""
    if a < b:
        return a
    return b


def main():
    """main"""
    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))

    print("El mayor es ", mayor(a, b))
    print("El menor es ", menor(a, b))


if __name__ == "__main__":
    main()
