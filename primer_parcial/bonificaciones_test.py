# test_empleados.py
import unittest
from bonificaciones import Empleado, Gerente, Desarrollador, Empresa


class TestEmpleado(unittest.TestCase):
    def test_bonificacion_empleado_base(self):
        e = Empleado("Juan", 1000, "123")
        self.assertEqual(e.calcular_bonificacion(), 50.0)

    def test_salario_total_empleado_base(self):
        e = Empleado("Ana", 2000, "456")
        self.assertEqual(e.calcular_salario(), 2100.0)

    def test_bonificacion_gerente(self):
        g = Gerente("Luis", 3000, "789")
        self.assertEqual(g.calcular_bonificacion(), 300.0)

    def test_salario_total_gerente(self):
        g = Gerente("Luis", 3000, "789")
        self.assertEqual(g.calcular_salario(), 3300.0)

    def test_bonificacion_desarrollador(self):
        d = Desarrollador("Clara", 4000, "111")
        self.assertEqual(d.calcular_bonificacion(), 280.0)

    def test_salario_total_desarrollador(self):
        d = Desarrollador("Clara", 4000, "111")
        self.assertEqual(d.calcular_salario(), 4280.0)

    def test_set_salario_valido(self):
        e = Empleado("María", 1000, "222")
        e.set_salario_base(2500)
        self.assertEqual(e.get_salario_base(), 2500)

    def test_set_salario_invalido(self):
        e = Empleado("Pedro", 1000, "333")
        with self.assertRaises(ValueError):
            e.set_salario_base(-100)

    def test_empresa_agregar_empleado(self):
        emp = Empresa()
        e = Empleado("Rosa", 1200, "444")
        emp.agregar_empleado(e)
        self.assertIn(e, emp.empleados)

    def test_empresa_salarios_mixtos(self):
        emp = Empresa()
        emp.empleados = [
            Empleado("A", 1000, "1"),
            Gerente("B", 2000, "2"),
            Desarrollador("C", 3000, "3"),
        ]

        resultados = emp.imprimir_salarios()
        esperado = [
            ("A", 1050.0),
            ("B", 2200.0),
            ("C", 3210.0),
        ]
        self.assertEqual(resultados, esperado)

        if __name__ == "__main__":
            unittest.main()
