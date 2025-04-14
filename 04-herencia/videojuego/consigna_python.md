## 🐍 Práctica de Herencia en Python: Entidades en un Videojuego

### 🎯 Consigna

Vas a modelar entidades dentro de un videojuego utilizando clases y **herencia**. El objetivo es construir una jerarquía de clases que represente distintos tipos de personajes y enemigos, cada uno con su comportamiento específico.

---

### 🧱 Clases requeridas

#### `Entidad` (superclase)
- Atributos:
  - `nombre`: `str`
  - `salud`: `int`
- Métodos:
  - `recibir_danio(self, cantidad: int) -> None`
  - `__str__(self) -> str`: devuelve una representación legible

#### `Jugador` (subclase de `Entidad`)
- Atributos:
  - `inventario`: `list[str]`
- Métodos:
  - `curarse(self, cantidad: int) -> None`
  - Puede sobrescribir `__str__()`

#### `Enemigo` (subclase de `Entidad`)
- Atributos:
  - `poder_ataque`: `int`
- Métodos:
  - `atacar(self, objetivo: Entidad) -> None`

#### `JefeFinal` (subclase de `Enemigo`)
- Atributos:
  - `fase`: `int` (representa la fase actual del combate)
- Métodos:
  - `cambiar_fase(self) -> None`
  - Sobrescribe `__str__()` para mostrar información de la fase

---

### 💡 Requisitos mínimos

- Usar `super()` para reutilizar código de clases base.
- Crear al menos un `Jugador`, un `Enemigo` y un `JefeFinal`.
- Mostrar interacciones entre ellos (`atacar`, `curarse`, `cambiar_fase`).
- Probar todo dentro de un `if __name__ == "__main__":`.

---

### ⭐ Bonus (opcional)

- Demostrar **polimorfismo** usando una lista de tipo `Entidad` con instancias de diferentes subclases.
- Agregar nuevos enemigos como `EnemigoVolador` o `EnemigoMagico` con comportamiento especial.
- Implementar un sistema simple de combate por turnos con texto en consola.

---

¿Querés que te prepare también el esqueleto del código en Python para que lo veas más claro o lo uses como base en clase?
