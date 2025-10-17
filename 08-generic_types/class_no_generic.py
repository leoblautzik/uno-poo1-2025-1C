class Contenedor:

    def __init__(self, contenido):
        self.contenido = contenido

    def get_contenido(self):
        return self.contenido

    def set_contenido(self, nuevo_contenido) -> None:
        self.contenido = nuevo_contenido


def main() -> None:
    c_int = Contenedor(10)
    c_str = Contenedor("Oi")
    a = c_int.get_contenido() + 1
    print(a)
    b = c_str.get_contenido() + "3"
    print(b)
    print(c_int.get_contenido())  # 10
    print(c_str.get_contenido())  # 'Oi'
    c_int.set_contenido("ocho")
    c_str.set_contenido(23)


if __name__ == "__main__":
    main()
