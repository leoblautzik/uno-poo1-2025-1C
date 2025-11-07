from typing import Optional, TypeVar, Generic


class NoHayElementosException(Exception):
    pass


T = TypeVar("T")


class Pila:
    """Pila NO GENERICA"""

    def __init__(self) -> None:
        self.items = []

    def push(self, item) -> None:
        """apilar"""
        self.items.append(item)

    def pop(self):
        """desapilar"""
        if self.is_empty():
            raise NoHayElementosException
        return self.items.pop()

    def peek(self):
        """desapilar"""
        if self.is_empty():
            raise NoHayElementosException
        return self.items[len(self.items) - 1]

    def is_empty(self) -> bool:
        """pila vacia"""
        return len(self.items) == 0


class Stack(Generic[T]):
    """Pila Generica"""

    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        """apila un elemento de tipo T"""
        self.items.append(item)

    def pop(self) -> T:
        """desapila el tope de la pila y devuelve un elemento de tipo T"""
        if self.is_empty():
            raise NoHayElementosException
        return self.items.pop()

    def peek(self) -> T:
        """devuelve el tope de la pila de tipo T, sin desapilarlo"""
        if self.is_empty():
            raise NoHayElementosException
        return self.items[len(self.items) - 1]

    def is_empty(self) -> bool:
        """pila vacia"""
        return len(self.items) == 0


class Cola2Pilas(Generic[T]):
    """Cree una clase Cola que utilice dos pilas para contener los datos de la siguiente manera:
    cada vez que se encola un elemento se lo guarda en la pila A, y cada vez que se desencola
    un elemento se lo extrae del tope de la pila B, si la pila B está vacía entonces se desapilan
    todos los elementos de la pila A y se los apila en B.
    """

    def __init__(self) -> None:
        self.__pa = Stack[T]()
        self.__pb = Stack[T]()

    def is_empty(self) -> bool:
        """cola vacia"""
        return self.__pa.is_empty() and self.__pb.is_empty()

    def enqueue(self, item: T) -> None:
        """encolar"""
        self.__pa.push(item)

    def dequeue(self) -> T:
        """desencolar, si está vacia lanza una excepcion"""
        if self.is_empty():
            raise NoHayElementosException
        if self.__pb.is_empty():
            while not self.__pa.is_empty():
                self.__pb.push(self.__pa.pop())
        return self.__pb.pop()

    def peek(self) -> T:
        """desencolar, si está vacia lanza una excepcion"""
        if self.is_empty():
            raise NoHayElementosException
        if self.__pb.is_empty():
            while not self.__pa.is_empty():
                self.__pb.push(self.__pa.pop())
        return self.__pb.peek()


class Node(Generic[T]):
    """class Node"""

    def __init__(self, dato: T, siguiente: Optional["Node[T]"] = None) -> None:
        self.dato = dato
        self.siguiente = siguiente


class LinkedStack(Generic[T]):
    """Una Pila con nodos simplemente enlazados"""

    def __init__(self, primero: Optional["Node[T]"] = None) -> None:
        self.__len = 0
        self.__primero = primero

    def push(self, dato: T) -> None:
        """el nuevo nodo se agrega al principio"""
        nuevo = Node[T](dato)
        if self.__len > 0:
            nuevo.siguiente = self.__primero
        self.__primero = nuevo
        self.__len += 1

    def is_empty(self) -> bool:
        """esta vacía"""
        return self.__len == 0

    def pop(self) -> T:
        """devuelve el dato del primer nodo y lo remueve"""
        if self.__primero is None:
            raise NoHayElementosException
        dato = self.__primero.dato
        if self.__len == 1:
            self.__primero = None
        else:
            if self.__primero is not None:
                self.__primero = self.__primero.siguiente
        self.__len -= 1
        return dato

    def peek(self) -> T:
        """devuelve el primer dato de la pila"""
        if self.__primero is None:
            raise NoHayElementosException
        dato = self.__primero.dato
        return dato

    def __str__(self) -> str:
        """str para ver la pila"""
        if self.__primero is None:
            raise NoHayElementosException
        s = "[ "
        nodo = self.__primero
        while nodo is not None:
            s += str(nodo.dato) + " "
            nodo = nodo.siguiente
        s += "]"
        return s


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


def main() -> None:
    # """main"""
    # pila = Pila()
    # pila.push(2)  # OK
    # pila.push("x")  # OK pero tendremos una pila con elementos de diferentes tipos
    # print(pila.pop())
    # print(pila.pop())
    #
    # stack = Stack[int]()
    # stack.push(2)  # OK
    # print(stack.pop())  # OK
    # # stack.push("x")  # error, solo se permmite apilar elementos de tipo int

    cola = Cola2Pilas[int]()
    cola.enqueue(11)
    cola.enqueue(12)
    cola.enqueue(13)
    cola.enqueue(14)
    print("peek", cola.peek())
    print("desencola", cola.dequeue())

    for _ in range(10):
        try:
            print(cola.dequeue())

        except NoHayElementosException:
            print("Cola vacia")

        finally:
            print("Hola Mundo")

    # print("peek", cola.peek())

    # ls = LinkedStack[str]()
    # ls.push("Ana")
    # ls.push("Laura")
    # ls.push("Lorena")
    # print(str(ls))
    # print(ls.peek())
    # while not ls.is_empty():
    #     print(ls.pop())
    #
    # print("------LinkedList--------")
    # ll = LinkedList[int]()
    # ll.add_first(11)
    # ll.add_last(12)
    # ll.add_first(10)
    # ll.add_last(13)
    # print(ll)
    # while not ll.is_empty():
    #     print(ll.remove_first())
    #     print(ll)
    #
    # ll.add_first(11)
    # ll.add_last(12)
    # ll.add_first(10)
    # ll.add_last(13)
    #
    # print(ll)
    # while not ll.is_empty():
    #     print(ll.remove_last())
    #     print(ll)


if __name__ == "__main__":
    main()
