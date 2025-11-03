class Mascota:
    def __init__(self, id, nombre, especie, edad, adoptado) -> None:
        self.id: int = id
        self.nombre: str = nombre
        self.especie: str = especie
        self.edad: int = edad
        self.adoptado: bool = adoptado

    def marcar_adoptado(self):
        # cambia el estado a adoptado.
        if not self.adoptado:
            self.adoptado = True

    def __str__(self) -> str:
        # devuelve una representación legible del animal.
        return f"{self.nombre}, {self.especie}, {self.edad}, {self.adoptado}"


class Refugio:
    def __init__(self):
        self.__mascotas: list[Mascota] = []

    def cargar_desde_archivo(self, ruta: str):
        try:
            with open(ruta, "r") as f:
                f.readline()
                for linea in f:
                    try:
                        datos = linea.strip().split(",")
                        id = int(datos[0])
                        nombre = datos[1]
                        especie = datos[2]
                        edad = int(datos[3])
                        adoptado = bool(datos[4])
                        self.__mascotas.append(
                            Mascota(id, nombre, especie, edad, adoptado)
                        )
                    except ValueError:
                        print("Error de formato")
        except FileNotFoundError:
            print("Archivo no encontrado")
        finally:
            f.close()

    def contar_por_especie(self) -> dict[str, int]:
        especies: dict[str, int] = {}
        for m in self.__mascotas:
            cantidad_actual = especies.setdefault(m.especie, 0)
            cantidad_actual += 1
            especies[m.especie] = cantidad_actual

        return especies


def main():
    patitas = Refugio()
    patitas.cargar_desde_archivo("mascotas.csv")
    print(patitas.contar_por_especie())


if __name__ == "__main__":
    main()
