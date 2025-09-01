import unittest

from producto import Producto


class TestProducto(unittest.TestCase):
    def test_aumentar_stock_invalido(self):
        obj = Producto("Perchas", 100.35)
        with self.assertRaises(ValueError):
            obj.aumentar_stock(0)

        with self.assertRaises(ValueError):
            obj.aumentar_stock(-3)


if __name__ == "__main__":
    unittest.main()
