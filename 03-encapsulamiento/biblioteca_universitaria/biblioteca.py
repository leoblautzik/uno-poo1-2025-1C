from estudiante import Estudiante
from libro import Libro


class Biblioteca:
    def __init__(self):
        # Lista de libros y estudiantes registrados
        self.__libros = []
        self.__estudiantes = []

    def registrar_libro(self, libro: Libro) -> None:
        pass

    def registrar_estudiante(self, estudiante: Estudiante) -> None:
        pass

    def prestamos_actuales(self):
        """Devuelve un mapeo de estudiante -> libros prestados."""
        pass


def main():
    pass


if __name__ == "__main__":
    main()
