"""
Claves de esta versión:
Alumno y Profesor pueden cambiar dinámicamente la persona interna con set_persona().
Los métodos delegados (get_nombre, presentarse) reflejan inmediatamente la nueva persona.
Los atributos propios (notas, curso, alumnos, asignatura) no se ven afectados, demostrando la flexibilidad de composición vs herencia.
Los tests confirman que la delegación sigue funcionando después del cambio dinámico.
"""


class Persona:
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def presentarse(self):
        return f"Hola, me llamo {self.__nombre} y tengo {self.__edad} años."

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad


class Alumno:
    def __init__(self, nombre: str, edad: int, curso: str):
        self.__persona = Persona(nombre, edad)  # composición
        self.__curso = curso
        self.__notas: list[int] = []

    # Delegación
    def get_nombre(self):
        return self.__persona.get_nombre()

    def get_edad(self):
        return self.__persona.get_edad()

    def presentarse(self):
        return self.__persona.presentarse() + f" Soy alumno del curso {self.__curso}."

    # Métodos propios
    def agregar_nota(self, nota: int):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0 y 10")

    def promedio(self):
        if not self.__notas:
            return 0
        return sum(self.__notas) / len(self.__notas)

    # Permite cambiar la persona contenida
    def set_persona(self, persona: Persona):
        self.__persona = persona


class Profesor:
    def __init__(self, nombre: str, edad: int, asignatura: str):
        self.__persona = Persona(nombre, edad)  # composición
        self.__asignatura = asignatura
        self.__alumnos: list[Alumno] = []

    # Delegación
    def get_nombre(self):
        return self.__persona.get_nombre()

    def get_edad(self):
        return self.__persona.get_edad()

    def presentarse(self):
        return self.__persona.presentarse() + f" Soy profesor de {self.__asignatura}."

    # Métodos propios
    def agregar_alumno(self, alumno: Alumno):
        self.__alumnos.append(alumno)

    def listar_alumnos(self):
        return [alumno.get_nombre() for alumno in self.__alumnos]

    # Permite cambiar la persona contenida
    def set_persona(self, persona: Persona):
        self.__persona = persona
