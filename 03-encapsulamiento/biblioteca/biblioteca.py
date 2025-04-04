"""Class Biblioteca"""

from libro import Libro


class Biblioteca:
    def __init__(self):
        self.__libros: list[Libro] = []

    def cuantos_libros(self):
        """Devuelve la cantidad de libros en la biblioteca"""
        return len(self.__libros)

    def agregar_libro(self, titulo, autor, genero, paginas):
        """Agrega un Libro a la biblioteca"""
        self.__libros.append(Libro(titulo, autor, genero, paginas))

    def libro_en_la_posicion(self, posicion):
        """Devuelve el título de un libro a partir de la posición."""
        return self.__libros[posicion - 1].obtener_titulo()

    def libro_con_mas_paginas(self) -> Libro:
        """Devuelva el libro con más cantidad de páginas."""
        pos_max = 0
        max_pag = self.__libros[0].obtener_paginas()
        for i in range(1, len(self.__libros)):
            if self.__libros[i].obtener_paginas() > max_pag:
                pos_max = i
                max_pag = self.__libros[i].obtener_paginas()
        return self.__libros[pos_max]


def main():
    pass


if __name__ == "__main__":
    main()
