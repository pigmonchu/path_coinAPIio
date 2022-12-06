# Objetivos

Evolucionar ese programita del step_01 a algo más parecido a una aplicación.

## Requisitos

- Hacer invisible la API KEY. Ponerla en un fichero fuera del repo (config.py)
- Presentar la noción de arquitectura en capas. Empezar por MVC de forma muy laxa. 
    - Capa de presentación (Vista)
    - Capa de negocio (Controlador)
    - Capa de datos (Modelo)

- Control de errores
    - Moneda inexistente
    - Errores de HTTP (url equivocada, o apikey incorrecta)

## Como

Ampliar la funcionalidad para cambiar no sólo a euros sino a cualquier cripto

Transformo step_02 en módulo de python

### Pasos - SOLO CAPA MODEL
- Creo un módulo python llamado cryptoconverter (carpeta + __init__.py)
    Extraigo la llamada a la api a un fichero llamado model.py
    Evoluciono el modelo hasta llegar a una clase par que obtiene el valor de intercambio cada vez que se necesita

