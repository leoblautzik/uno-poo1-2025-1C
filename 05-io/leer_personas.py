from dataclasses import dataclass
from io import open


@dataclass
class Persona:
    def __init__(self, dni, apellido, edad, provincia):
        self.dni = dni
        self.apellido = apellido
        self.edad = edad
        self.provincia = provincia

    def __str__(self):
        return f"Apellido: {self.apellido}, Edad: {self.edad}"

    def __lt__(self, other):
        return self.apellido < other.apellido


def main():
    personas = []
    personas_por_provincia = {}
    cuantas_por_provincia = {}
    with open("personas.csv", "r", encoding="UTF-8") as file:
        for linea in file:
            datos = linea.split(",")
            persona = Persona(int(datos[0]), datos[1], int(datos[2]), datos[3])
            personas.append(persona)

    # Si pensamos la logica para actualizar el map
    # for persona in personas:
    #     key = persona.provincia
    #     if key in personas_por_provincia.keys():
    #         lista_p = personas_por_provincia[key]
    #     else:
    #         lista_p = []
    #
    #     lista_p.append(persona)
    #     personas_por_provincia[key]=lista_p

    # Si uamos setdefault
    for persona in personas:
        lista_p = personas_por_provincia.setdefault(persona.provincia, [])
        lista_p.append(persona)
        personas_por_provincia[persona.provincia] = lista_p

    for persona in personas:
        contador = cuantas_por_provincia.setdefault(persona.provincia, 0)
        contador += 1
        cuantas_por_provincia[persona.provincia] = contador

    with open("personas_por_rovincia.txt", "w", encoding="UTF-8") as archivo:
        for provincia, l_p in personas_por_provincia.items():
            archivo.write(f"Provincia: {provincia}")
            # sorted(l_p)
            list.sort(l_p)
            for p in l_p:
                archivo.write(str(p))
                archivo.write("\n")

            archivo.write("\n")

    print(cuantas_por_provincia)


if __name__ == "__main__":
    main()
