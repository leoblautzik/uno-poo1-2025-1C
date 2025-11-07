def mayusculas(func):
    def wrapper():
        resultado = func()
        return resultado.upper()

    return wrapper


@mayusculas
def saludar():
    return "hola mundo"


def main():
    # nueva_funcion = mayusculas(saludar)
    # print(nueva_funcion())  # → "HOLA MUNDO"
    print(saludar())


if __name__ == "__main__":
    main()
