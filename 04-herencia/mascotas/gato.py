from mascota import Mascota


class Gato(Mascota):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.__color = color

    def emitir_somido(self):
        return "Miau, miau, miauuuuuuu"

    def __str__(self):
        return super().__str__() + "\n" + f"Soy de color {self.__color}\n"
