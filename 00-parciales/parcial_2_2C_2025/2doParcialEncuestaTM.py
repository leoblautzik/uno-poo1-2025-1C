class RespuestaEncuesta:
    def __init__(self, nombre, edad, ciudad, satisfaccion) -> None:
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        self.satisfaccion = satisfaccion


class LineaMalFormadaException(Exception):
    pass


class SatisfaccionInvalidaException(Exception):
    pass


class Encuesta:
    def __init__(self) -> None:
        self.respuestas = []

    def cargar_respuestas(self, archivo):
        try:
            with open(archivo, "r") as fr:
                for lr in fr:
                    try:
                        datos = lr.strip().split(",")
                        if len(datos) != 4:
                            raise LineaMalFormadaException()
                        nombre = datos[0]
                        edad = int(datos[1])
                        ciudad = datos[2]
                        satisfaccion = int(datos[3])
                        if not 1 <= satisfaccion <= 10:
                            raise SatisfaccionInvalidaException()
                        self.respuestas.append(
                            RespuestaEncuesta(nombre, edad, ciudad, satisfaccion)
                        )
                    except LineaMalFormadaException:
                        print("Linea mal formada")
                    except ValueError:
                        print("Valor no numérico")
                    except SatisfaccionInvalidaException:
                        print("Error en valor de satisfaccion")

        except FileNotFoundError:
            print("Archivo no encontrado")

    def agrupar_por_ciudad(self) -> dict[str, list[RespuestaEncuesta]]:
        dicci = {}
        for r in self.respuestas:
            lr = dicci.setdefault(r.ciudad, [])
            lr.append(r)
            dicci[r.ciudad] = lr

        return dicci

    def promedio_satisfaccion_por_ciudad(self) -> dict[str, float]:
        promedios = {}
        agrupados = self.agrupar_por_ciudad()
        for k, v in agrupados.items():
            suma = 0
            for r in v:
                suma += r.satisfaccion
            prom = float(suma) / len(v)
            promedios[k] = prom

        return promedios

    def guardar_resultados(self, salida):
        with open(salida, "w") as out:
            out.write(" Ciudad \t Satisfaccion\n")
            for k, v in self.promedio_satisfaccion_por_ciudad().items():
                out.write(f"{k},\t {v}\n")


def main():
    e = Encuesta()
    e.cargar_respuestas("encuestas.csv")
    print(e.promedio_satisfaccion_por_ciudad())
    e.guardar_resultados("ciudad_satisfaccion.txt")


if __name__ == "__main__":
    main()
