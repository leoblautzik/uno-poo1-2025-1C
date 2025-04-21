from abc import ABCMeta, abstractmethod


class Profesional(metaclass=ABCMeta):
    __honorario_basico = 1500000

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @abstractmethod
    def calcular_honorario(self):
        pass

    @classmethod
    def set_honorario_basico(cls, nuevo_valor):
        cls.__honorario_basico = nuevo_valor

    @classmethod
    def get_honorario_basico(cls):
        return cls.__honorario_basico

    # Comparación basada en honorarios
    def __lt__(self, other):
        return self.calcular_honorario() < other.calcular_honorario()

    def __eq__(self, other):
        return self.calcular_honorario() == other.calcular_honorario()

    def __str__(self):
        return f"({type(self).__name__}) {self.nombre} {self.apellido} - Honorario: ${self.calcular_honorario():,.2f}"


class Medico(Profesional):
    def calcular_honorario(self):
        return self.get_honorario_basico()


class Cirujano(Medico):
    def calcular_honorario(self):
        return super().calcular_honorario() * 1.25


class CirujanoCardiovascular(Cirujano):
    def calcular_honorario(self):
        return super().calcular_honorario() * 1.25


class Dentista(Profesional):
    def calcular_honorario(self):
        return self.get_honorario_basico()


class Endodoncista(Dentista):
    def calcular_honorario(self):
        return super().calcular_honorario() * 1.25


def main():
    profesionales = [
        Medico("Ana", "Martínez"),
        Dentista("Luis", "Gómez"),
        Endodoncista("Manuel", "Molar"),
        Cirujano("Pedro", "Sánchez"),
        CirujanoCardiovascular("Laura", "Pérez"),
    ]

    total = sum(p.calcular_honorario() for p in profesionales)
    print(f"\nTotal a abonar: ${total:,.2f}\n")

    print("Listado de profesionales (ordenado por honorarios descendente):")
    for profesional in sorted(profesionales, reverse=True):
        print(profesional)


if __name__ == "__main__":
    main()
