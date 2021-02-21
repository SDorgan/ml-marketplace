Ejercicio de desarrollo propuesto por Mercado Libre

Enunciado: 

Nos piden dar una solución al siguiente problema usando los motores/lenguajes/arquitecturas conocidas:

Estamos desarrollando un marketplace y queremos diseñar un backend para nuestros Ítems, que debe soportar también la búsqueda.

De Ítems sabemos que:
* La cantidad total es del orden de los 100.000.000+,
* El tráfico va a ser muy elevado (~1.000.000 reqs/sec.)
* La distribución del tráfico es 90% lecturas y 10% escritura.
* Y se esperan incrementos puntuales de tráfico en casos como eventos Día de Niño, Hot-sale y similares.


La arquitectura no está definida, entonces te damos total libertad para diseñar lo que creas conveniente.

1) Diseñar la arquitectura de la solución de forma que soporte:
  + Todas las operaciones que se pueden hacer con un Ítem.
  + El tráfico propuesto, dando varias opciones donde sea aplicable e indicando los pros/contras de cada una.

2) Definir los endpoints de la API de Ítems.
3) Incluir un diagrama explicando cómo estaría diseñado/estructurado el código de la API. (incluir un esqueleto del código es un plus)



Datos de Arquitectura:

    -Servidor en Amazon con el objetivo de poder aumentar el tamaño fácilmente previo a eventos como Día del Niño o Hot Sale.
    -Base de Datos en MongoDB para soporte de grandes cantidades de datos y de la cantidad de llamados de lectura (Document Based NoSQL)
    -Desarrollo en Python con uso de Flask App pra generado fácil de API
    -La API de la aplicación se puede encontrar en el archivo api.yaml



Puerto del server: 5000

Instalar:

    - npm
    - docker
    - docker-compose
    
Para correr local:
    
    - docker-compose up --build
