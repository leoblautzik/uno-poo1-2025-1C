class Libro:
    """
    Cada Libro tiene título, autor, ISBN
    y un número limitado de ejemplares disponibles.
    """

    def __init__(self, titulo, autor, ISBN, ejemplares_disponibles):
        self.__titulo = titulo
        self.__autor = autor
        self.__ISBN = ISBN
        self.__ejemplares_disponibles = ejemplares_disponibles
        self.__ejemplares_prestados = 0

    def prestar(self):
        if self.puedo_prestar():
            self.__ejemplares_prestados += 1

    def devolver(self):
        self.__ejemplares_prestados -= 1

    def puedo_prestar(self):
        return self.__ejemplares_prestados < self.__ejemplares_disponibles

    def __str__(self):
        return f"{self.__titulo}, {self.__autor}, eje. disp:{self.__ejemplares_disponibles - self.__ejemplares_prestados}"


def main():
    pass


if __name__ == "__main__":
    main()
