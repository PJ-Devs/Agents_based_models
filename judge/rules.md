# Reglas de la simulación de jurados

## 1. Definiciones

- **Temperatura Social**: Medida del nivel de tensión o presión social en la sala de jurados. Valor entre 0 y 1. Aumenta con la reducción del tiempo disponible y la divergencia entre opiniones. Una TS alta indica un ambiente propenso al conformismo o cambios impulsivos de opinión.

- **Tiempo Restante**: Tiempo en minutos que queda para alcanzar un veredicto. A menor tiempo, mayor presión sobre los jurados.

- **Presencia de Evidencia**: Valor probabilístico (0 a 1) que indica si existe evidencia disponible y clara que favorece una de las posturas (culpabilidad o inocencia).

- **Nivel de Convicción Individual (CI)**: Nivel de certeza (0 a 1) que tiene cada jurado respecto a su posición actual. A menor CI, mayor probabilidad de cambiar su voto.

## 2. Jurados (Agentes)

Cada jurado tiene los siguientes atributos:

- **Opinión Inicial (OI)**: Valor entre 0 (inocente) y 1 (culpable).
- **Convicción Individual (CI)**: Qué tan firme es su postura (0 a 1).

## 3. Ambiente

El ambiente de la sala está definido por:

- **Temperatura Social (TS)**: Calculada como:

  ```
  TS(t) = 1 - (TR(t) / TR_0) + α · D(t)
  ```

  Donde:

  - `TR_0`: Tiempo total inicial.
  - `D(t)`: Dispersión de opiniones en el tiempo `t`.
  - `α`: Peso del desacuerdo en el aumento de la TS.

- **Evidencia (E)**: Dos valores, cada uno en el rango de 0 a 1, los cuales representan la evidencia a favor y en contra del caso. Aquí, se tiene en cuenta que la que la evidencia a favor reslpada la inocencia, mientras que la evidencia en contra la refuta.

## 4. Reglas de Cambio de Opinión

Las decisiones de los jurados pueden cambiar por:

### a. Presión Social

Si la TS es alta, hay gran desacuerdo y poco tiempo, aumenta la probabilidad de alinearse con la mayoría.

### b. Evidencia

Si existe evidencia fuerte que contradice su postura es más probable que cambie hacia la consenso del caso.

### c. Tiempo

A medida que se reduce el TR, jurados con baja CI y alta ST tienden a cambiar su postura más rápidamente.

## 5. Decisión Final

El juicio termina cuando:

- Se alcanza un consenso (todas las opiniones están dentro de un umbral de diferencia, por ejemplo 0.1).
- Se acaba el tiempo (TR = 0) y se realiza una votación (mayoría simple o calificada).
