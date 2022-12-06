# Objetivos

Evolucionar ese programita del step_01 a algo más parecido a una aplicación.

## Requisitos

- Hacer invisible la API KEY. Ponerla en un fichero fuera del repo (config.py)
- Presentar la noción de arquitectura en capas. Empezar por MVC de forma muy laxa. 
    - Capa de presentación (Vista)
    - Capa de negocio (Controlador)
    - ~~Capa de datos (Modelo)~~

- Control de errores
    - Moneda inexistente
    - Errores de HTTP (url equivocada, o apikey incorrecta)

## Como

Ampliar la funcionalidad para cambiar no sólo a euros sino a cualquier cripto

Transformo step_02 en módulo de python

### Pasos - MODEL heredado y CAPA VISTA
- Creo un módulo python llamado cryptoconverter (carpeta + __init__.py)
    Añado la capa vista en un fichero llamado view.py y juego con funciones, clases y Excepciones
- Para simular la vista llegamos a una clase y a limitar el número de monedas con las que trabajar (04_con_clases.py)
