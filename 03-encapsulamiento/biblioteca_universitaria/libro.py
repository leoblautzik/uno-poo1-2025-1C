class Libro:
    """
    Cada Libro tiene título, autor, ISBN
    y un número limitado de ejemplares disponibles.
    """

    def __init__(self, titulo, autor, ISBN, ejemplares_disponibles):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = ISBN
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
        return (
            f"{self.__titulo}, {self.__autor}, "
            f"ejemp_disp:{self.__ejemplares_disponibles - self.__ejemplares_prestados}"
        )

    def get_isbn(self) -> str:
        return self.__isbn

    def __eq__(self, other):
        if not isinstance(other, Libro):
            return False
        return self.__isbn == other.__isbn

    def __hash__(self):
        return hash(self.__isbn)

    def __repr__(self):
        return f"Libro({self.__titulo}, {self.__autor}, {self.__isbn})"


def main():
    pass


if __name__ == "__main__":
    main()
