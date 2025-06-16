class LineaMalFormadaError(Exception):
    pass


# Clase para representar un libro
class Libro:
    def __init__(self, titulo, autor, genero, cantidad_disponible):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cantidad_disponible = cantidad_disponible

    def __repr__(self):
        return f"{self.titulo}, {self.autor}, {self.genero}, {self.cantidad_disponible}"


# Clase para gestionar la biblioteca
class GestionBiblioteca:
    def __init__(self):
        self.libros = []

    def cargar_libros(self, archivo_csv):
        try:
            with open(archivo_csv, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    datos = linea.split(",")
                    try:
                        if len(datos) != 4:
                            raise LineaMalFormadaError
                        titulo = datos[0]
                        autor = datos[1]
                        genero = datos[2]
                        cantidad = datos[3]
                        try:
                            cantidad = int(cantidad.strip())
                            libro = Libro(
                                titulo.strip(), autor.strip(), genero.strip(), cantidad
                            )
                            self.libros.append(libro)
                        except ValueError:
                            print(f"Cantidad inválida para libro: {linea}")
                    except LineaMalFormadaError:
                        print("Linea mal formada", linea)
        except FileNotFoundError:
            print(f"No se encontró el archivo: {archivo_csv}")
        except IOError as e:
            print(f"Error al leer el archivo: {e}")

    def libros_por_genero(self):
        dicc_generos = {}
        for libro in self.libros:
            dicc_generos.setdefault(libro.genero, []).append(libro)
        return dicc_generos

    def autor_mas_libros_disponibles(self):
        conteo = {}
        for libro in self.libros:
            cd = conteo.get(libro.autor, 0) + libro.cantidad_disponible
            conteo[libro.autor] = cd
        if conteo:
            max_cant = max(conteo.values())
            for autor, cantidad in conteo.items():
                if cantidad == max_cant:
                    return autor, max_cant
        return None, 0


def main():
    gestion = GestionBiblioteca()
    gestion.cargar_libros("libros.csv")

    print("\n2.b: Diccionario por género:")
    libros_por_genero = gestion.libros_por_genero()
    for genero, libros in libros_por_genero.items():
        print(f"{genero}: {libros}")

    print("\n2.c: Autor con más libros disponibles:")
    autor, cantidad = gestion.autor_mas_libros_disponibles()
    if autor:
        print(f"{autor}: {cantidad} libros disponibles.")
    else:
        print("No hay datos de libros.")


if __name__ == "__main__":
    main()
