## 🐾 Consigna: Clínica Veterinaria

Una clínica veterinaria necesita llevar un registro de los animales que atiende. Para ello, se requiere modelar las distintas **mascotas**.

### Requisitos:

Crear una **clase abstracta o base** llamada `Mascota` con los siguientes atributos y métodos:

- `nombre` (String)
- `edad` (int)
- `emitir_sonido()` → método abstracto (cada animal lo implementará de forma diferente)
- `__str__()` o `toString()` para mostrar información de la mascota

### Crear las siguientes subclases:

#### 🐶 Perro

- Atributo extra: `raza` (String)
- El sonido es "Guau guau"

#### 🐱 Gato

- Atributo extra: `color` (String)
- El sonido es "Miau"

#### 🐰 Conejo

- Atributo extra: `pelaje` (String)
- El sonido es "..."

### Objetivo

- Crear una lista de varias `Mascota` (de diferentes tipos) y mostrar su información.
- Llamar al método `emitir_sonido()` de forma **polimórfica**: sin importar el tipo real, todas deben responder correctamente.

---

### 💡 Bonus para quienes avanzan más:

- Agregar un método `vacunar()` en `Mascota` que cada subclase implemente con un mensaje diferente.
- Mostrar cómo se pueden usar `isinstance()` o `type()` (en Python) o `instanceof` (en Java) si necesitás hacer un comportamiento especial para una subclase.

---
