import unittest
from list import LinkedList


class TestListaEnlazadaGenerica(unittest.TestCase):
    """Pruebas unitarias para la lista enlazada generica"""

    def test_1(self):
        """Agrego siempre al final y quito del principio"""
        ll = LinkedList[int]()
        ll.add_last(11)
        ll.add_last(12)
        ll.add_last(10)
        ll.add_last(13)
        self.assertEqual(11, ll.remove_first())
        self.assertEqual(12, ll.remove_first())
        self.assertEqual(10, ll.remove_first())
        self.assertEqual(13, ll.remove_first())

    def test_2(self):
        """Agrego siempre al final y quito del final"""
        ll = LinkedList[int]()
        ll.add_last(11)
        ll.add_last(12)
        ll.add_last(10)
        ll.add_last(13)
        self.assertEqual(13, ll.remove_last())
        self.assertEqual(10, ll.remove_last())
        self.assertEqual(12, ll.remove_last())
        self.assertEqual(11, ll.remove_last())

    def test_3(self):
        """Con una lista de strings agrego siempre al final y quito del final"""
        ll = LinkedList[str]()
        ll.add_last("A")
        ll.add_last("B")
        ll.add_last("C")
        ll.add_last("D")
        self.assertEqual("D", ll.remove_last())
        self.assertEqual("C", ll.remove_last())
        self.assertEqual("B", ll.remove_last())
        self.assertEqual("A", ll.remove_last())


if __name__ == "__main__":
    unittest.main()
