from typing import Optional, TypeVar, Generic


class NoHayElementosException(Exception):
    pass


T = TypeVar("T")


class Node(Generic[T]):
    """class Node"""

    def __init__(self, dato: T, siguiente: Optional["Node[T]"] = None) -> None:
        self.dato = dato
        self.siguiente = siguiente


class LinkedList(Generic[T]):
    def __init__(
        self, primero: Optional["Node[T]"] = None, ultimo: Optional["Node[T]"] = None
    ) -> None:
        self.__len = 0
        self.__primero = primero
        self.__ultimo = ultimo

    def add_first(self, dato: T) -> None:
        """el nuevo nodo se agrega al principio"""
        nuevo = Node[T](dato)
        if self.__primero is None:
            self.__ultimo = nuevo
        else:
            nuevo.siguiente = self.__primero
        self.__primero = nuevo
        self.__len += 1

    def add_last(self, dato: T) -> None:
        """el nuevo nodo se agrega al final"""
        nuevo = Node[T](dato)
        if self.__ultimo is None:
            self.__primero = nuevo
        else:
            self.__ultimo.siguiente = nuevo

        self.__ultimo = nuevo
        self.__len += 1

    def remove_first(self) -> T:
        if self.__primero is None:
            raise NoHayElementosException
        dato: T = self.__primero.dato
        if self.size() == 1:
            self.__primero = None
            self.__ultimo = None
        else:
            self.__primero = self.__primero.siguiente
        self.__len -= 1

        return dato

    def remove_last(self) -> T:
        if self.__ultimo is None:
            raise NoHayElementosException
        dato: T = self.__ultimo.dato
        if self.size() == 1:
            self.__primero = None
            self.__ultimo = None
        elif self.__primero is not None and self.__primero.siguiente is not None:
            anterior: Node[T] = self.__primero
            current: Node[T] = self.__primero.siguiente
            while current.siguiente is not None:
                anterior = current
                current = current.siguiente

            self.__ultimo = anterior
            self.__ultimo.siguiente = None

        self.__len -= 1

        return dato

    def size(self) -> int:

        return self.__len

    def is_empty(self) -> bool:

        return self.__primero is None

    def __repr__(self) -> str:
        """str para ver la lista"""
        if self.__primero is None:
            s = "[ ]"
        else:
            s = "[ "
            nodo = self.__primero
            while nodo is not None:
                s += str(nodo.dato) + " "
                nodo = nodo.siguiente
            s += "]"

        return s
