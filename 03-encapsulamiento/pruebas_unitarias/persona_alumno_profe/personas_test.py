import unittest

from personas import Alumno, Persona, Profesor


class TestPersonas(unittest.TestCase):
    def setUp(self):
        # Creamos un alumno y un profesor para todos los tests
        self.alumno = Alumno("Ana", 20, "Matemática")
        self.profesor = Profesor("Luis", 45, "Matemática")
        self.alumno.agregar_nota(8)
        self.alumno.agregar_nota(9)
        self.profesor.agregar_alumno(self.alumno)

    # Tests para la delegación de Persona en Alumno
    def test_alumno_nombre_edad(self):
        self.assertEqual(self.alumno.get_nombre(), "Ana")
        self.assertEqual(self.alumno.get_edad(), 20)

    def test_alumno_presentarse(self):
        self.assertIn("Ana", self.alumno.presentarse())
        self.assertIn("Matemática", self.alumno.presentarse())

    def test_alumno_promedio(self):
        self.assertAlmostEqual(self.alumno.promedio(), 8.5)

    def test_alumno_agregar_nota_invalida(self):
        with self.assertRaises(ValueError):
            self.alumno.agregar_nota(12)

    # Tests para la delegación de Persona en Profesor
    def test_profesor_nombre_edad(self):
        self.assertEqual(self.profesor.get_nombre(), "Luis")
        self.assertEqual(self.profesor.get_edad(), 45)

    def test_profesor_presentarse(self):
        self.assertIn("Luis", self.profesor.presentarse())
        self.assertIn("Matemática", self.profesor.presentarse())

    # Tests de métodos propios de Profesor
    def test_profesor_listar_alumnos(self):
        lista = self.profesor.listar_alumnos()
        self.assertIn("Ana", lista)
        self.assertEqual(len(lista), 1)

    def test_profesor_agregar_alumno_nuevo(self):
        alumno2 = Alumno("Pedro", 22, "Matemática")
        self.profesor.agregar_alumno(alumno2)
        lista = self.profesor.listar_alumnos()
        self.assertIn("Pedro", lista)
        self.assertEqual(len(lista), 2)

    # Test de cambio dinámico de Persona en Alumno
    def test_cambiar_persona_alumno(self):
        nueva_persona = Persona("Pedro", 22)
        self.alumno.set_persona(nueva_persona)
        self.assertEqual(self.alumno.get_nombre(), "Pedro")
        self.assertEqual(self.alumno.get_edad(), 22)
        # Aún conserva atributos propios de Alumno
        self.alumno.agregar_nota(10)
        self.assertAlmostEqual(self.alumno.promedio(), (8 + 9 + 10) / 3)

    # Test de cambio dinámico de Persona en Profesor
    def test_cambiar_persona_profesor(self):
        nueva_persona = Persona("Marta", 40)
        self.profesor.set_persona(nueva_persona)
        self.assertEqual(self.profesor.get_nombre(), "Marta")
        self.assertEqual(self.profesor.get_edad(), 40)
        # Aún conserva atributos propios de Profesor
        self.assertIn("Ana", self.profesor.listar_alumnos())


if __name__ == "__main__":
    unittest.main()
