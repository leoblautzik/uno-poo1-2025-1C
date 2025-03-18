"""Se ingresa un valor numérico por consola, determinar e 
informar si se trata de un número primo o no"""

# def es_primo(n) -> bool:
#     """Devuelve true si el n es primo"""
#     ep = True
#     i = 2
#     while i < n and ep:
#         if n % i == 0:
#             ep = False
#         i += 1
#
#     return ep


def es_primo(n):
    """Devuelve true si el n es primo"""
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


def main():
    """main"""
    n = int(input("Ingrese un numero: "))

    if es_primo(n):
        print("es primo")
    else:
        print("no es primo")


if __name__ == "__main__":
    main()
