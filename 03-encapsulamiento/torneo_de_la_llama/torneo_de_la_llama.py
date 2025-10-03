from enum import Enum

# -------------------------
# ENUM de Items
# -------------------------


class Item(Enum):
    ESPADA = 10
    VARITA = 7
    ARCO = 8
    POCION = 3
    CAPA = 5
    # 👆 Se pueden agregar más ítems mágicos


# -------------------------
# Clase Héroe
# -------------------------
class Heroe:
    def __init__(self, nombre: str) -> None:
        self._nombre = nombre
        self._items: list[Item] = []  # lista privada de ítems

    @property
    def nombre(self):
        return self._nombre

    def agregar_item(self, item: Item):
        """Agrega un ítem al héroe"""
        self._items.append(item)

    def consumir_item(self, item: Item):
        """Elimina un ítem si lo tiene"""
        self._items.remove(item)

    def poder_de_fuego(self) -> int:
        """Devuelve la suma de poderes de todos sus ítems"""
        pdf = 0
        for item in self._items:
            pdf += item.value
        return pdf

    def vaciar_items(self):
        """El héroe pierde todos sus ítems"""
        self._items = []

    def quitar_poder_de_fuego(self, pdf_a_quitar):
        if self.poder_de_fuego() <= pdf_a_quitar:
            self.vaciar_items()

        else:
            # self._items = sorted(self._items, key=Item.value)
            quitado = 0
            while len(self._items) > 0 and quitado < pdf_a_quitar:
                quitado += self._items[0].value
                self._items.pop(0)

    def mostrar_items(self) -> str:
        """Devuelve un string con los ítems actuales"""
        s = ""
        for item in self._items:
            s += item.name
            s += ", "
        return s

    def __str__(self):
        return f"{self._nombre} (Poder: {self.poder_de_fuego()})"

    def __lt__(self, other):
        return self.poder_de_fuego() < other.poder_de_fuego()

    def __eq__(self, other):
        if isinstance(other, Heroe):
            return (
                self.nombre == other.nombre
                and self._items == other._items
            )
        return False


# -------------------------
# Clase Torneo
# -------------------------


class Torneo:
    def __init__(self):
        self.participantes = []

    def agregar_heroe(self, heroe: Heroe):
        """Agrega un héroe al torneo"""
        self.participantes.append(heroe)

    def mostrar_participantes(self):
        self.participantes.sort()
        for p in self.participantes:
            print(p)

    def enfrentar(self, h1: Heroe, h2: Heroe):
        """
        Enfrenta a dos héroes:
        - Gana el de mayor poder de fuego
        - El perdedor pierde todos sus ítems
        - El ganador descarta ítems hasta quedar con poder >= al que tenía su rival
        - Empate: ambos pierden todos sus ítems
        """
        if h1.poder_de_fuego() == h2.poder_de_fuego():
            h1.vaciar_items()
            h2.vaciar_items()
            return

        if h1.poder_de_fuego() > h2.poder_de_fuego():
            ganador = h1
            perdedor = h2
        else:
            ganador = h2
            perdedor = h1

        ganador.quitar_poder_de_fuego(perdedor.poder_de_fuego())
        perdedor.vaciar_items()

    def iniciar(self):
        """
        (Opcional) Simula rondas del torneo hasta que quede un ganador.
        """
        # TODO: implementar si se quiere
        pass


# -------------------------
# Ejemplo de uso (para pruebas)
# -------------------------
if __name__ == "__main__":
    # Crear héroes
    h1 = Heroe("Arthas")
    h2 = Heroe("Jaina")
    h3 = Heroe("Sylvanas")

    # Dar algunos ítems iniciales
    h1.agregar_item(Item.ESPADA)
    h1.agregar_item(Item.POCION)

    h2.agregar_item(Item.VARITA)
    h2.agregar_item(Item.ARCO)

    h3.agregar_item(Item.ARCO)
    h3.agregar_item(Item.POCION)

    print(h1.nombre, h1.mostrar_items(), h1.poder_de_fuego())
    print(h2.nombre, h2.mostrar_items(), h2.poder_de_fuego())
    print(h3.nombre, h3.mostrar_items(), h3.poder_de_fuego())

    # # Crear torneo
    torneo = Torneo()
    torneo.agregar_heroe(h1)
    torneo.agregar_heroe(h2)
    torneo.agregar_heroe(h3)
    print("Muestro ordenado")
    torneo.mostrar_participantes()

    #
    # # Enfrentamientos de ejemplo
    # torneo.enfrentar(h1, h2)
    # torneo.enfrentar(h1, h3)
    #
    # # Mostrar estados finales
    # print(h1.nombre, h1.mostrar_items(), h1.poder_de_fuego())
    # print(h2.nombre, h2.mostrar_items(), h2.poder_de_fuego())
    # print(h3.nombre, h3.mostrar_items(), h3.poder_de_fuego())
