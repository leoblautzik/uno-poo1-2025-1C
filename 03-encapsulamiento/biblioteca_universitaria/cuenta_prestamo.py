from libro import Libro


class CuentaDePrestamo:
    """Los préstamos deben gestionarse a través de una
    clase CuentaDePrestamo, que lleva un registro interno
    de los libros prestados y fechas de devolución.
    La CuentaDePrestamo es responsable de manejar la lógica
    de cuántos libros tiene un estudiante y si puede tomar más.
    No se puede superar el límite de 3 préstamos por estudiante.
    """

    def __init__(self):
        self.__libros_prestados: list[Libro] = []

    def get_libros_prestados(self) -> list[Libro]:
        return self.__libros_prestados

    def prestar(self, libro: Libro):
        if libro.puedo_prestar() and len(self.__libros_prestados) < 3:
            libro.prestar()
            self.__libros_prestados.append(libro)

    def devolver(self, libro: Libro):
        libro.devolver()
        self.__libros_prestados.remove(libro)

    def __str__(self):
        s: str = ""
        for libro in self.__libros_prestados:
            s += libro.__str__()
            s += "\n"

        return s


def main():
    pass


if __name__ == "__main__":
    main()
