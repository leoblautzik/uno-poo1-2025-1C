from mascota import Mascota


class Conejo(Mascota):
    def __init__(self, nombre, edad, pelaje):
        super().__init__(nombre, edad)
        self.__pelaje = pelaje

    def emitir_somido(self):
        return "........ "

    def __str__(self):
        return super().__str__() + "\n" + f"Soy de pelaje {self.__pelaje}\n"
