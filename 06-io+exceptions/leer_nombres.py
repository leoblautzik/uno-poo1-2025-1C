from io import open


class LeerNombres:
    def __init__(self) -> None:
        self.nombres = []

    def leer_nombres(self, mi_archivo: str):
        with open(mi_archivo, "r") as archinom:
            for nombre in archinom:
                self.nombres.append(nombre.strip())
        archinom.close()

    def contar_nombres(self):
        return len(self.nombres)

    def nombres_largos(self) -> tuple[list[str], int]:
        nombres_largos = []
        nl = self.nombres[0]
        lmax = len(nl)

        for nombre in self.nombres:
            if len(nombre) > lmax:
                lmax = len(nombre)

        for nombre in self.nombres:
            if len(nombre) == lmax:
                nombres_largos.append(nombre)

        return nombres_largos, lmax

    def nombres_largos_max(self) -> tuple[list[str], int]:
        # 1. Obtener la longitud máxima
        max_len = len(max(self.nombres, key=len))

        # 2. Filtrar todos los nombres que tengan esa longitud
        nombres_largos = [nombre for nombre in self.nombres if len(nombre) == max_len]
        return nombres_largos, max_len

    def ordenar(self):
        self.nombres.sort(key=len)

    def escribir_ordenados(self):
        with open("nombres_ordenados.txt", "w") as ao:
            self.ordenar()
            for nombre in self.nombres:
                ao.write(nombre + "\n")


def main():
    ln = LeerNombres()
    ln.leer_nombres("nombres.txt")
    print(ln.nombres)
    print(ln.nombres_largos())
    ln.escribir_ordenados()


if __name__ == "__main__":
    main()
