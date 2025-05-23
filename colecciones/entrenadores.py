"""
“Bielsa”:[“Juan”, “Alberto”],
Alvarez”:[“Tom”, “Alberto”, “Vero”],
"""


class Entrenadores:
    def __init__(self):
        pass

    def procesar(self, entrada):
        salida = {}
        # lista_entrenadores = []
        for entrenador, lista_socios in entrada.items():
            for socio in lista_socios:
                lista_entrenadores = salida.setdefault(socio, [])
                # if socio in salida.keys():
                #     lista_entrenadores = salida[socio]
                # else:
                #     lista_entrenadores = []

                lista_entrenadores.append(entrenador)
                salida[socio] = lista_entrenadores

        return salida


def main():
    entrada = {
        "Bielsa": ["Juan", "Alberto"],
        "Alvarez": ["Tom", "Alberto", "Vero"],
        "Gago": ["Alberto", "Vero", "Juan"],
    }
    print(entrada)

    entre = Entrenadores()
    print(entre.procesar(entrada))


if __name__ == "__main__":
    main()
