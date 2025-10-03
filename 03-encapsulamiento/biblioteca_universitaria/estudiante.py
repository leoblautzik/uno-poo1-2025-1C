from cuenta_prestamo import CuentaDePrestamo
from libro import Libro


class Estudiante:
    """La clase Estudiante debe componerse de una
    CuentaDePrestamo, no heredar de ella.
    """

    def __init__(self):
        self.__cuenta_prestamo = CuentaDePrestamo()

    def prestar_libro(self, libro: Libro):
        self.__cuenta_prestamo.prestar(libro)

    def devolver_libro(self, libro: Libro):
        self.__cuenta_prestamo.devolver(libro)

    def __str__(self) -> str:
        return self.__cuenta_prestamo.__str__()


def main():
    l1 = Libro("T1", "A1", 12223, 1)
    l2 = Libro("T2", "A2", 12443, 2)
    l3 = Libro("T3", "A3", 11123, 3)
    l4 = Libro("T4", "A4", 15553, 2)
    pepito = Estudiante()

    print(l1)
    pepito.prestar_libro(l1)
    print(l1)
    pepito.prestar_libro(l2)
    pepito.prestar_libro(l3)
    pepito.prestar_libro(l4)

    print(pepito)

    pepito.devolver_libro(l1)
    pepito.prestar_libro(l4)

    print(pepito)


if __name__ == "__main__":
    main()
