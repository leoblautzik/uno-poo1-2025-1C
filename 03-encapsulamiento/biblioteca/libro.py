"""Class Libro"""

from genero import Genero


class Libro:
    def __init__(self, titulo: str, autor: str, genero: Genero, paginas: int):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__paginas = paginas

    @property
    def titulo(self):
        return self.__titulo

    @property
    def paginas(self):
        return self.__paginas

    @property
    def autor(self):
        return self.__autor

    @property
    def genero(self):
        return self.__genero

    def __eq__(self, other):
        return (
            self.__titulo == other.titulo
            and self.__autor == other.autor
            and self.__genero == other.genero
            and self.__paginas == other.paginas
        )
