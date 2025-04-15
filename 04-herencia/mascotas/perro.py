from mascota import Mascota


class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.__raza = raza

    def emitir_somido(self):
        return "Guau, guau , guauuuuu"

    def recordar_vacunar(self):
        return "La fecha de la proxima dosis es ......\n"

    def __str__(self):
        return super().__str__() + "\n" + f"Soy de raza {self.__raza}\n"
