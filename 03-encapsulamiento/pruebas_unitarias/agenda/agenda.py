class Contacto:
    def __init__(self, nombre: str, telefono: str):
        self.__nombre = nombre
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre

    def get_telefono(self):
        return self.__telefono

    def __str__(self):
        return f"{self.__nombre}: {self.__telefono}"


class Agenda:
    def __init__(self):
        self.__contactos = []  # lista privada de objetos Contacto

    def agregar_contacto(self, nombre: str, telefono: str):
        contacto = Contacto(nombre, telefono)
        self.__contactos.append(contacto)

    def buscar_contacto(self, nombre: str):
        for contacto in self.__contactos:
            if contacto.get_nombre() == nombre:
                return contacto
        return None

    def listar_contactos(self):
        return [str(contacto) for contacto in self.__contactos]


def main():
    pass


if __name__ == "__main__":
    main()
