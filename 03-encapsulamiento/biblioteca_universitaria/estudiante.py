from cuenta_prestamo import CuentaDePrestamo
from libro import Libro


class Estudiante:
    """La clase Estudiante debe componerse de una
    CuentaDePrestamo, no heredar de ella.
    """

    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__cuenta_prestamo = CuentaDePrestamo()

    def get_nombre(self):
        return self.__nombre

    def prestar_libro(self, libro: Libro):
        self.__cuenta_prestamo.prestar(libro)

    def devolver_libro(self, libro: Libro):
        self.__cuenta_prestamo.devolver(libro)

    def __str__(self) -> str:
        return self.__nombre + self.__cuenta_prestamo.__str__()

    def __repr__(self) -> str:
        return self.__nombre + self.__cuenta_prestamo.__str__()

    def libros_prestados(self) -> list[Libro]:
        return self.__cuenta_prestamo.get_libros_prestados()


def main():
    pass


if __name__ == "__main__":
    main()
