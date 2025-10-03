"""Biblioteca Universitaria"""

from typing import Dict, List
from estudiante import Estudiante
from libro import Libro


class Biblioteca:
    def __init__(self):
        # Lista de libros y estudiantes registrados
        self.__libros: list[Libro] = []
        self.__estudiantes: list[Estudiante] = []

    def registrar_libro(self, libro: Libro) -> None:
        self.__libros.append(libro)

    def registrar_estudiante(self, estudiante: Estudiante) -> None:
        self.__estudiantes.append(estudiante)

    def prestar_libro(self, libro, usuario):
        self.__estudiantes[self.__estudiantes.index(usuario)].prestar_libro(libro)

    def devolver_libro(self, libro, usuario):
        self.__estudiantes[self.__estudiantes.index(usuario)].devolver_libro(libro)

    def prestamos_actuales(self) -> str:
        """
        Usa un diccionario con clave libro y
        value lista de estudiantes para juntar los datos.
        """
        prestamos: Dict[Libro, List[Estudiante]] = {}
        s = "Prestamos actuales\n"
        for estu in self.__estudiantes:
            for libro in estu.libros_prestados():
                prestamos.setdefault(libro, []).append(estu)

        for libro in prestamos.keys():
            s += libro.__repr__()
            s += " ->"
            for estu in prestamos[libro]:
                s += estu.get_nombre()
                s += " "

            s += "\n"

        return s


def main():
    el_ateneo = Biblioteca()

    l1 = Libro("T1", "A1", 12223, 10)
    l2 = Libro("T2", "A2", 12443, 20)
    l3 = Libro("T3", "A3", 11123, 30)
    l4 = Libro("T4", "A4", 15553, 40)
    el_ateneo.registrar_libro(l1)
    el_ateneo.registrar_libro(l2)
    el_ateneo.registrar_libro(l3)
    el_ateneo.registrar_libro(l4)

    print(l1)
    print(l2)
    pepito = Estudiante("Pepito")
    juancito = Estudiante("Juancito")
    luisito = Estudiante("Luisito")
    el_ateneo.registrar_estudiante(pepito)
    el_ateneo.registrar_estudiante(juancito)
    el_ateneo.registrar_estudiante(luisito)

    el_ateneo.prestar_libro(l1, pepito)
    el_ateneo.prestar_libro(l2, juancito)
    el_ateneo.prestar_libro(l1, luisito)

    print(el_ateneo.prestamos_actuales())


if __name__ == "__main__":
    main()
