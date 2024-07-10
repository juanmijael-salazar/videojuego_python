# Videojuego desarrollado con Python
## Code header & Configuration
_pip3 install opencv-python_
```
pip install pygame
```
# Sumary

![](https://github.com/juanmijael-salazar/videojuego_python/blob/main/screenshots/shooter2.png)

El videojuego consiste principalmente en destruir o esquivar los meteoros que se van generando
aleatoriamente con una velocidad también aleatoria en el escenario del juego.

Objetos creados:
* La nave (Player)
* Meteoros (10 tamaños)
* Esferas verdes (curación)
* Proyectil de disparo

Adicionales visuales y/o audiovisuales
* Fondo (entorno visual)
* Barra de vida
* Sonidos (colisión, curación, disparo, música de fondo, estallido de meteoro)

Acciones:
* Mover nave: tecla de direccionales (izquierda, derecha, arriba, abajo) Perspectiva 2D centrado.
* Disparar proyectil: tecla (espacio)

El comportamiento de las esferas verdes es la misma que los meteoros pero su objetivo principal
es que cuando la nave hace una colisión con esta esfera, la nave restaura su salud en 25 y si la
destruye con un proyectil se resta los puntos en -3.
El jugador (nave) puede moverse tanto en eje x y eje y, si hay colisión entre la nave y un
meteoro, la vida de la nave se resta en -25, considerando que la vida máxima de la nave es 100,
en el escenario de juego aparece la puntuación que se va sumando o restando conforme vaya
sucediendo dichos eventos y también está una barra verde que representa la vida de la nave.

![](https://github.com/juanmijael-salazar/videojuego_python/blob/main/screenshots/shooter3.png)
![](https://github.com/juanmijael-salazar/videojuego_python/blob/main/screenshots/shooter1.png)

`
Sprites: https://www.klipartz.com/es/sticker-png-fofyg
https://www.gameart2d.com/freebies.html
`
`
Efectos de sonido:
https://www.zapsplat.com/?s=explosion&post_type=music&sound-effect-category-id=
`



[Copyright](https://github.com/juanmijael-salazar/videojuego_python).
