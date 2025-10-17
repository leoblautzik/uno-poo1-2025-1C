"""un mapa en python"""

from typing import TypeVar, Generic

K = TypeVar("K")
V = TypeVar("V")


class Map(Generic[K, V]):

    def __init__(self):
        self.map: dict[K, V] = {}

    def contains_key(self, k: K) -> bool:
        return k in self.map

    def get(self, k: K, d: V) -> V:
        if self.contains_key(k):
            return self.map[k]
        return d

    def put(self, k: K, v: V) -> None:
        self.map.update({k: v})

    def __str__(self) -> str:
        s = ""
        for k, v in self.map.items():
            s += str(k) + ": "
            s += str(v) + "\n"
        return s

    def __repr__(self) -> str:
        s = ""
        for k, v in self.map.items():
            s += str(k) + ": "
            s += str(v) + "\n"
        return s


m = Map[int, str]()
m.put(1, "a")
print(m.get(1, ""))
print(m.get(2, ""))
mapita = Map[int, list[int]]()
mapita.put(1, [3, 5, 7, 9])
print(mapita)
print(mapita.get(1, []))
print(mapita.get(2, []))

m_str = Map[str, list[str]]()
m_str.put("Gago", ["Cavani", "Rojo"])
m_str.put("Gallardo", ["Borja", "Armani"])
print(m_str)
