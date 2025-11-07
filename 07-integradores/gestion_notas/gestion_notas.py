import os


class CalificacionFueraDeRango(Exception):
    pass


class LineaMalFormadaException(Exception):
    pass


class Calificacion:
    def __init__(self, nombre, materia, nota) -> None:
        self.nombre = nombre
        self.materia = materia
        self.nota = nota

    @property
    def calificacion(self) -> int:
        return self.nota

    @calificacion.setter
    def calificacion(self, nueva_nota) -> None:
        if nueva_nota < 0 or nueva_nota > 10:
            raise CalificacionFueraDeRango()
        self.nota = nueva_nota

    def esta_aprobada(self) -> bool:
        return self.nota >= 4

    def esta_promocionada(self) -> bool:
        return self.nota >= 7

    def esta_reprobada(self) -> bool:
        return not self.esta_aprobada()

    def a_final(self) -> bool:
        return self.esta_aprobada() and not self.esta_promocionada()

    def __repr__(self):
        return f"{self.nombre} {self.materia} {self.calificacion}"


class GestionNotas:
    def __init__(self):
        self.calificaciones: list[Calificacion] = []

    def cargar_calificaciones(self, file) -> None:
        # TODO
        with open(file, newline="") as cali:
            for linea in cali:
                try:
                    self.calificaciones.append(self._validar_calificacion(linea))
                except LineaMalFormadaException:
                    print("Linea con formato incorrecto")
                except ValueError:
                    print("Error de formato numerico")
                except CalificacionFueraDeRango:
                    print("Calificacion invalida")

        cali.close()

    def _validar_calificacion(self, linea) -> Calificacion:
        datos = linea.strip().split(",")
        if len(datos) != 3:
            raise LineaMalFormadaException()
        nombre = datos[0]
        materia = datos[1]
        nota = int(datos[2])  # lanza un ValueError si datos[2] no es un entero
        if nota < 1 or nota > 10:
            raise CalificacionFueraDeRango()

        return Calificacion(nombre, materia, nota)

    def notas_por_materia(self) -> dict[str, list[int]]:
        aux: dict[str, list[int]] = {}

        for cu in self.calificaciones:
            # lc = aux.setdefault(cu.materia, [])
            if cu.materia in aux.keys():
                lc = aux[cu.materia]
            else:
                lc = []
            lc.append(cu.nota)
            # aux[cu.materia] = lc
            aux.update({cu.materia: lc})

        return aux

    def materia_mejor_promedio(self) -> tuple[float, list[str]]:
        aux: dict[str, float] = {}
        npm = self.notas_por_materia()
        for k, v in npm.items():
            materia = k
            lista_calificaciones = v
            suma_notas = sum(lista_calificaciones)
            # for nota in lista_calificaciones:
            #     suma_notas += nota
            promedio = float(suma_notas) / len(lista_calificaciones)
            aux[materia] = promedio

        promedio_maximo = max(aux.values())
        # en caso de empates, guarda las materias que tienen
        # el mismo promedio maximo
        lm_pm = []
        for k, v in aux.items():
            if v == promedio_maximo:
                lm_pm.append(k)

        return promedio_maximo, lm_pm

        # return max(aux.items(), key=lambda x: x[1])  # no resuelve empates

    def estadisticas(self):
        npm = self.notas_por_materia()
        with open("estadisticas.txt", "w") as est:
            est.write("Materia\t\t\tReprobados\tA Final \tPromocion\n")
            for materia, lc in npm.items():
                repro = self.cuantos_repro(lc)
                promo = self.cuantos_promo(lc)
                a_final = len(lc) - repro - promo
                est.write(f"{materia:10}\t {repro:10d}\t {a_final:10d}\t {promo:10d}\n")
        est.close()

    def cuantos_repro(self, lc) -> int:
        contador = 0
        for c in lc:
            if c < 4:
                contador += 1
        return contador

    def cuantos_promo(self, lc) -> int:
        contador = 0
        for c in lc:
            if c >= 7:
                contador += 1
        return contador


def main():
    gn = GestionNotas()
    while True:
        try:
            file = input("Ingrese el nombre del archivo de datos: ")
            gn.cargar_calificaciones(file)
            print(gn.calificaciones)
            print(gn.notas_por_materia())
            print(gn.materia_mejor_promedio())
            print(gn.estadisticas())
            break
        except FileNotFoundError:
            print("No se encuentra el archivo, intenete nuevamente...")
            for f in os.listdir("."):  # Lista de archivos y directorios
                print(f)


if __name__ == "__main__":
    main()
