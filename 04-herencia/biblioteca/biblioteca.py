# -----------------------------
# Ejercicio: Sistema de Biblioteca Virtual
# -----------------------------
from __future__ import annotations
from abc import ABC


# Clase base
class Material(ABC):
    def __init__(self, titulo: str, autor: str, anio: int):
        # Atributos privados
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__prestado = False

    # Getters
    def get_titulo(self) -> str:
        return self.__titulo

    def get_autor(self) -> str:
        return self.__autor

    def get_anio(self) -> int:
        return self.__anio

    def esta_prestado(self) -> bool:
        return self.__prestado

    def prestar(self):
        self.__prestado = True

    def devolver(self):
        self.__prestado = False

    def __str__(self) -> str:
        # representación genérica de un material
        return (
            f"{type(self).__name__} -> "
            f"Titulo: {self.get_titulo()}, "
            f"Autor: {self.get_autor()}, "
            f"Año: {self.get_anio()}"
        )


# -----------------------------
# Subclases (Herencia)
# -----------------------------
class Libro(Material):
    def __init__(self, titulo: str, autor: str, anio: int, genero: str):
        # inicializar atributos de Material + atributo propio genero
        super().__init__(titulo, autor, anio)

        self.__genero = genero

    def __str__(self) -> str:
        # devolver cadena representando un libro
        return f"{super().__str__()}, Genero: {self.__genero}"


class Revista(Material):
    def __init__(self, titulo: str, autor: str, anio: int, numero_edicion: int):
        # inicializar atributos de Material + atributo propio numero_edicion
        super().__init__(titulo, autor, anio)

        self.__numero_edicion = numero_edicion

    def __str__(self) -> str:
        # devolver cadena representando una revista
        return f"{super().__str__()}, Num Edición: {self.__numero_edicion}"


class DVD(Material):
    def __init__(self, titulo: str, autor: str, anio: int, duracion: int):
        super().__init__(titulo, autor, anio)

        self.__duracion = duracion

    def __str__(self) -> str:
        # devolver cadena representando una revista
        return f"{super().__str__()}, Duración: {self.__duracion}"


# -----------------------------
# Clase Usuario (Composición)
# -----------------------------
class Usuario:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        # lista de objetos Material
        self.__materiales_prestados: list[Material] = []

    def prestar(self, material: Material):
        # agregar material a la lista de prestados
        self.__materiales_prestados.append(material)

    def devolver(self, material: Material):
        # quitar material de la lista de prestados
        self.__materiales_prestados.remove(material)

    def listar_materiales(self):
        # mostrar todos los materiales prestados por este usuario
        print("Materiales en poder de" + self.__nombre)
        for m in self.__materiales_prestados:
            print(m)


# -----------------------------
# class Biblioteca
# -----------------------------
class Biblioteca:
    def __init__(self):
        self.materiales: list[Material] = []
        self.usuarios: list[Usuario] = []

    def mostrar_informacion(self, material: Material):
        # imprimir el objeto (usará __str__ polimórfico)
        print(material.__str__())

    def prestar(self, material: Material, usuario: Usuario):
        if material in self.materiales and not material.esta_prestado():
            material.prestar()
            usuario.prestar(material)

    def devolver(self, material: Material, usuario: Usuario):
        material.devolver()
        usuario.devolver(material)


# -----------------------------
# Programa principal
# -----------------------------


def main():
    # crear algunos libros, revistas y DVDs
    # crear usuarios
    # prestar materiales
    # listar materiales de cada usuario
    uno_biblio = Biblioteca()
    libro = Libro("Base de Datos", "Dejean", 1998, "Ciencia de Datos")
    revista = Revista("Pata ti", "Atlantida", 1990, 123)
    dvd = DVD("La Felicidad", "Palito Ortega", 1970, 60)
    uno_biblio.mostrar_informacion(dvd)

    uno_biblio.materiales = [libro, revista, dvd]

    juancito = Usuario("Juancito")

    uno_biblio.prestar(dvd, juancito)
    uno_biblio.prestar(libro, juancito)
    uno_biblio.prestar(revista, juancito)

    juancito.listar_materiales()

    juancito.devolver(revista)

    juancito.listar_materiales()


if __name__ == "__main__":
    main()
