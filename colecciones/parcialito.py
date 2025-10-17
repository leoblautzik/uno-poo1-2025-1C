class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Parcialito:
    def __init__(self):
        self.mapa = {}

    def agrupar_personas(self, lista_personas):
        for p in lista_personas:
            lista_personas_misma_edad = self.mapa.setdefault(p.edad, [])
            lista_personas_misma_edad.append(p.nombre)
            self.mapa[p.edad] = lista_personas_misma_edad

        return self.mapa

    def __str__(self):
        ordenado = dict(sorted(self.mapa.items()))
        return str(ordenado)


def main():
    personas = [
        Persona("Ana", 30),
        Persona("Luis", 25),
        Persona("Marta", 30),
        Persona("Juan", 25),
        Persona("Pedro", 40),
    ]
    p = Parcialito()
    p.agrupar_personas(personas)
    print(p)


if __name__ == "__main__":
    main()
