## 🕹️ Práctica de Herencia: Entidades en un Videojuego

### 🎯 Consigna

Vas a modelar entidades dentro de un videojuego utilizando clases y **herencia**. Tu objetivo es construir una jerarquía de clases que represente distintos tipos de personajes y enemigos, cada uno con su comportamiento específico.

### 🧱 Clases requeridas

#### `Entidad` (superclase)
- Atributos:
  - `nombre`: String
  - `salud`: int
- Métodos:
  - `recibirDanio(int cantidad)`
  - `toString()` para describir la entidad

#### `Jugador` (subclase de `Entidad`)
- Atributos:
  - `inventario`: arreglo o lista de Strings
- Métodos:
  - `curarse(int cantidad)`
  - Puede sobreescribir `toString()` si lo deseas

#### `Enemigo` (subclase de `Entidad`)
- Atributos:
  - `poderAtaque`: int
- Métodos:
  - `atacar(Entidad objetivo)`

#### `JefeFinal` (subclase de `Enemigo`)
- Atributos:
  - `fase`: int (representa la fase actual del combate)
- Métodos:
  - `cambiarFase()`: incrementa la fase
  - Sobreescribe `toString()` para incluir información de la fase

---

### 💡 Requisitos mínimos

- Usar `super` en los constructores para reutilizar el de la clase base.
- Instanciar al menos un `Jugador`, un `Enemigo` y un `JefeFinal`.
- Mostrar interacciones entre objetos (ataques, curaciones, cambio de fase).
- Probar todo en una clase `main`.

---

### ⭐ Bonus (opcional)

- Mostrar el uso de polimorfismo: declarar una lista de tipo `Entidad` que contenga instancias de `Jugador`, `Enemigo` y `JefeFinal`, y recorrerla usando los métodos comunes.
- Agregar nuevos tipos de enemigos (por ejemplo: `EnemigoVolador`, `EnemigoMágico`).
- Implementar un sistema simple de combate por turnos.

---
