import unittest
from nave import Caza, Bombardero, Crucero


class TestCombateNaves(unittest.TestCase):
    def test_caza_ataca_a_caza(self):
        c1 = Caza("X-Wing")
        c2 = Caza("TIE Fighter")
        c1.atacar(c2)
        self.assertEqual(c2.salud, 85)  # 100 - 15

    def test_caza_destruye_a_otro(self):
        atacante = Caza("X-Wing")
        victima = Caza("TIE Fighter")
        for _ in range(7):  # 7 ataques de 15 = 105
            atacante.atacar(victima)
        self.assertTrue(victima.esta_destruida())
        self.assertEqual(victima.salud, 0)

    def test_bombardero_ataca_y_se_autodaña(self):
        b = Bombardero("TIE Bomber")
        c = Caza("X-Wing")
        b.atacar(c)
        self.assertEqual(c.salud, 75)  # 100 - 25
        self.assertEqual(b.salud, 145)  # 150 - 5

    def test_bombardero_se_autodestruye_con_muchos_ataques(self):
        b = Bombardero("TIE Bomber")
        c = Caza("X-Wing")
        for _ in range(30):  # suficiente para bajar su propia salud a 0
            b.atacar(c)
        self.assertTrue(b.esta_destruida())
        self.assertEqual(b.salud, 0)

    def test_crucero_ataca_con_salud_alta(self):
        cr = Crucero("Destructor Estelar")
        c = Caza("X-Wing")
        cr.atacar(c)
        self.assertEqual(c.salud, 60)  # 100 - 40

    def test_crucero_no_ataca_con_salud_baja(self):
        cr = Crucero("Destructor Estelar")
        c = Caza("X-Wing")
        cr.salud = 50  # baja la salud manualmente
        cr.atacar(c)
        self.assertEqual(c.salud, 100)  # no recibió daño

    def test_estado_muestra_nombre_y_salud(self):
        c = Caza("X-Wing")
        esperado = "Nave: X-Wing -> salud: 100"
        self.assertEqual(c.estado(), esperado)

    def test_encadenamiento_de_ataques(self):
        c = Caza("X-Wing")
        b = Bombardero("TIE Bomber")
        cr = Crucero("Destructor Estelar")

        c.atacar(b)  # b: 150 -> 135
        b.atacar(cr)  # cr: 300 -> 275, b: 135 -> 130
        cr.atacar(c)  # c: 100 -> 60

        self.assertEqual(b.salud, 130)
        self.assertEqual(cr.salud, 275)
        self.assertEqual(c.salud, 60)

    def test_destruccion_por_crucero(self):
        cr = Crucero("Destructor Estelar")
        c = Caza("X-Wing")
        for _ in range(3):  # 3 ataques de 40 = 120
            cr.atacar(c)
        self.assertTrue(c.esta_destruida())
        self.assertEqual(c.salud, 0)


if __name__ == "__main__":
    unittest.main()
