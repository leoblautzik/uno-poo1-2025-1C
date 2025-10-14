import unittest

from terminal_de_teletipo import TerminalDeTeletipo


class TestColeccionesTerminalDeTeletipo(unittest.TestCase):
    def test_01(self):
        """& al final, debe devolver cadena vacia"""
        self.assertEqual("", TerminalDeTeletipo.procesar("abc&"))

    def test_02(self):
        """cadena vaci, debe devolver cadena vacia"""
        self.assertEqual("", TerminalDeTeletipo.procesar(""))

    def test_03(self):
        """todas ////, debe devolver cadena vacia"""
        self.assertEqual("", TerminalDeTeletipo.procesar("/////////"))


if __name__ == "__main__":
    unittest.main()
