def main():
    """Leer dos valores numéricos enteros e indicar
    cual es el mayor y cual es el menor.
    Considerar que ambos valores son diferentes.
    """

    a = int(input("Ingrese un entero: "))
    b = int(input("Ingrese otro entero: "))

    mayor = a
    menor = b
    if a < b:
        mayor = b
        menor = a
    # Le agregamos a la consigna que puedan ser iguales
    if mayor == menor:
        print("Son iguales")
    else:
        print("Mayor: ", mayor)
        print("Menor: ", menor)


if __name__ == "__main__":
    main()
