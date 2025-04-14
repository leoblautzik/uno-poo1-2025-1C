## 🧠 Bonus: Simulación de batalla por turnos (Extensión opcional)

Como extensión del sistema de unidades del juego de estrategia, vas a programar una **simulación simple por turnos** entre dos bandos. El objetivo es mostrar en acción el comportamiento polimórfico de las unidades y resolver conflictos de combate automáticamente.

### 🎯 Objetivo

Implementar una función o clase que reciba dos equipos de unidades y simule una batalla por turnos hasta que uno de los dos bandos quede completamente derrotado.

---

### 🧩 Reglas para la simulación

- La batalla ocurre en una grilla lineal de 10 posiciones (índices del 0 al 9).
- Cada unidad comienza en una posición determinada del campo de batalla.
- En cada turno, una unidad viva de un equipo ataca a una unidad viva del otro equipo si se encuentra en su **rango de ataque permitido**.
- Si no hay enemigos a distancia válida, la unidad **no ataca** en ese turno.
- Las unidades se alternan: primero ataca una unidad del equipo A, luego una del equipo B, y así sucesivamente.
- El juego termina cuando todas las unidades de un bando están muertas.
- Mostrar el resumen de cada turno:
  - Qué unidad atacó
  - A quién atacó
  - Qué daño hizo
  - Qué unidad murió (si corresponde)

---

### 🧪 Sugerencias de implementación

- Crear una clase o función `Batalla` que gestione:
  - Las posiciones iniciales de las unidades
  - El ciclo de turnos
  - Las reglas de ataque por tipo de unidad
- Crear una función `distancia(a, b)` para saber si dos unidades pueden atacarse según su tipo.
- Mostrar por consola la evolución de la batalla.
- Asegurarse de que las reglas de ataque, energía y recursos se respeten.

---

### 💣 Ejemplo de output esperado

