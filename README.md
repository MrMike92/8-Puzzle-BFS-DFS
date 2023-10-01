# Solución del juego 8 por medio de búsqueda BFS y DFS

El juego del 8, también conocido como el rompecabezas de 8 piezas, es un desafío en el que se debe reorganizar fichas numeradas en un tablero 3x3 para alcanzar una disposición objetivo y resolverlo implica el uso de algoritmos de búsqueda, como DFS (Búsqueda en Profundidad) y BFS (Búsqueda en Amplitud).

En este repositorio se encuentra 4 archivos los cuales los que tienen `-Definida` en el nombre sus tableros de inicio ya se encuentran definidas dentro del código (ver `Imagen 2`), los demás sus tableros de inicio no se encuentran definidas si no que son aleatorias cada vez que se inicie el programa.

## Instrucciones de uso.

- Clona este repositorio en tu máquina local.
- Asegure que el respositorio se haya descargado correctamente.
- Abre el programa que deseas ejecutar en tu entorno de desarrollo que soporte Python 3.11.2 64-bit.

## Funcionamiento.

El juego de 8 es un rompecabezas clásico que implica mover piezas numeradas en un tablero de 3x3 para alcanzar el objetivo de encontrar una secuencia de movimientos que resuelva el rompecabezas desde una configuración inicial dada hasta el objetivo, el objetivo más común para este juego es la de ordenar de manera ascendente empezando desde la parte superior izquierda del tablero como se muestra en la `Imagen 1`.

<img src="/img/imagen1.png" alt="objetivoComunJuego8" title="Objetivo común en el juego del 8"/>

> _**Imagen 1.- Objetivo común en el juego del 8**_

<br/>

Los programas usan el orden de la `Imagen 2` como el tablero objetivo y el orden para mover las fichas será en el siguiente orden: Izquierda, arriba, derecha y abajo. Solo se pueden realizar movimientos válidos, es decir, mover una ficha adyacente al espacio vacío y siguiendo el orden de prioridad de movimientos ya mencionada y no se pueden realizar movimientos diagonales ni fuera de los límites del tablero.

<img src="/img/imagen2.png" alt="ordenTableroObjetivo" title="Orden para el tablero objetivo" width="250px"/>

> _**Imagen 2.- Orden para el tablero objetivo que se usó**_

Primero se define el tablero inicial que va a resolver, esta puede ser de manera aleatoria cada vez que se inicie el programa o ya definir una, se define cuáles son los estados del problema, donde cada uno de los estados del problema pueda ser esquematizado gráficamente y representado en forma simbólica que a su vez, cada estado debe ser capaz de realizar una transición de estado, es decir, que pueda ser capaz de cambiar a otro estado y de esta manera se define un espacio de estados (o búsqueda) de un problema dado, esto representa un grafo, o alguna estructura de datos similar, cuyos nodos representan las configuraciones que puedan ser alcanzadas (los estados válidos) y las conexiones son las movidas posibles que pueda tener cada estado (transición de estado). De esta manera un estado en el juego pueda ser presentado como en la `Imagen 1`, puesto que una transición de estado es la transformación de un estado a otro estado, como se muestra en la `Figura 1`, y un espacio de estados son todas las posibles transiciones que puedan realizarse de un estado a otros, la `Figura 2` muestra, con una estructura de árbol, un conjunto de estados.

<img src="/img/figura1.png" alt="transicionEstado" title="Transición de un estado" width="300px"/>

> _**Figura 1.- Transición de un estado**_

<img src="/img/figura2.jpg" alt="arbolAlgunosPosiblesEstados" title="Árbol de algunos posibles estados" width="600px"/>

> _**Figura 2.- Árbol de algunos posibles estados**_

Como el DFS es un algoritmo de búsqueda caracterizado por realizar una búsqueda a un árbol o grafo de búsqueda, que empieza por la raíz (o punto inicial) del árbol y explora los más lejano posible cada una de las ramas antes de volver hacia atrás y verificar todos los nodos pendientes, la `Figura 3` muestra un árbol de búsqueda para la generación de los estados y la manera en que son accesados.

<img src="/img/figura3.jpg" alt="comportamientoArbolDFS" title="Comportamiento de un árbol DFS" width="600px"/>

> _**Figura 3.- Comportamiento de un árbol DFS**_

Como el BFS es un algoritmo caracterizado por realizar una búsqueda a un árbol o grafo de búsqueda empezando por la raíz (o punto inicial) del árbol y explora a cada uno de los nodos vecinos en el nivel actual, dando prioridad a recorrer a todo el nivel antes de moverse a los nodos de un siguiente nivel, como muestra la `Figura 4` la cual es un árbol de búsqueda para la generación de los estados y la manera en que estos son accesados.

<img src="/img/figura4.png" alt="comportamientoArbolBFS" title="Comportamiento de un árbol BFS" width="600px"/>

> _**Figura 4.- Comportamiento de un árbol BFS**_

Cabe mencionar que el BFS puede ser más lento que el DFS en algunos casos debido a la cantidad de estados que debe explorar, mientras que el DFS puede encontrar soluciones más rápido en situaciones en las que el número de movimientos requeridos sea muy grande, pero esto no garantiza que encuentre la solución más corta.

Si deseas contribuir a este proyecto, puedes enviar solicitudes de extracción (pull requests) con mejoras o características adicionales y si tienes alguna pregunta o problema, puedes contactarme a través de mi perfil de GitHub MrMike92. :turtle:
