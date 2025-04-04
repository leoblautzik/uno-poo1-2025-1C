"""Class Libro"""

from genero import Genero


class Libro:
    def __init__(self, titulo: str, autor: str, genero: Genero, paginas: int):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__paginas = paginas

    def obtener_titulo(self):
        return self.__titulo

    def obtener_paginas(self):
        return self.__paginas

    def obtener_autor(self):
        return self.__autor

    def obtener_genero(self):
        return self.__genero

    def __eq__(self, other):
        return (
            self.__titulo == other.obtener_titulo()
            and self.__autor == other.obtener_autor()
            and self.__genero == other.obtener_genero()
            and self.__paginas == other.obtener_paginas()
        )
