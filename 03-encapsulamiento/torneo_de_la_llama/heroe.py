
# -------------------------
# Clase Héroe
# -------------------------
class Heroe:
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
        self.__items: list[Item] = []  # lista privada de ítems

    @property
    def nombre(self):
        return self._nombre

    def agregar_item(self, item: Item):
        """Agrega un ítem al héroe"""
        self.__items.append(item)

    def consumir_item(self, item: Item):
        """Elimina un ítem si lo tiene"""
        self.__items.remove(item)

    def poder_de_fuego(self) -> int:
        """Devuelve la suma de poderes de todos sus ítems"""
        pdf = 0
        for item in self.__items:
            pdf += item.value
        return pdf

    def vaciar_items(self):
        """El héroe pierde todos sus ítems"""
        self.__items = []

    def quitar_poder_de_fuego(self, pdf_a_quitar):
        if self.poder_de_fuego() <= pdf_a_quitar:
            self.vaciar_items()

        else:
            # self._items = sorted(self._items, key=Item.value)
            quitado = 0
            while len(self.__items) > 0 and quitado < pdf_a_quitar:
                quitado += self.__items[0].value
                self.__items.pop(0)

    def mostrar_items(self) -> str:
        """Devuelve un string con los ítems actuales"""
        s = ""
        for item in self.__items:
            s += item.name
            s += ", "
        return s

    def __str__(self):
        return f"{self.__nombre} (Poder: {self.poder_de_fuego()})"

    def __lt__(self, other):
        return self.poder_de_fuego() < other.poder_de_fuego()

    def __eq__(self, other):
        return self.nombre == other.nombre and self.__items == other.__items
