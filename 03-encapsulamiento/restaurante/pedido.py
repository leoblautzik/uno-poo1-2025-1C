from categoria_plato import CategoriaPlato
from plato import Plato


class Pedido:
    def __init__(self) -> None:
        self.__platos: list[Plato] = []

    def agregar_plato(self, pl: Plato) -> None:
        self.__platos.append(pl)

    def total(self) -> float:
        total = 0.00
        for plato in self.__platos:
            total += plato.precio
        return total

    def ticket(self):
        s = ""
        for plato in self.__platos:
            s += plato.__repr__()
            s += "\n"
        s += "Total: " + str(self.total())
        return s


if __name__ == "__main__":
    entrada = Plato("Bruschetta", 1500, CategoriaPlato.ENTRADA)
    principal = Plato("Pasta Alfredo", 3500, CategoriaPlato.PRINCIPAL)
    postre = Plato("Tiramisú", 2000, CategoriaPlato.POSTRE)
    flan = Plato("Flan", 4500.00, CategoriaPlato.POSTRE)

    pedido = Pedido()
    pedido.agregar_plato(entrada)
    pedido.agregar_plato(principal)
    pedido.agregar_plato(postre)

    print(pedido.ticket())
