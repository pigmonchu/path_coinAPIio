import requests
from cryptoconverter import URL


def convierte(deCripto, cantidad, aCripto):
    cabecera = {"X-CoinAPI-Key": "23DBFF71-249C-46BB-BB56-9EBDFA5399F6"}
    respuesta = requests.get(URL.format(deCripto, aCripto), headers=cabecera)

    if respuesta.status_code == 200:
        valor = respuesta.json()["rate"]
        return valor * cantidad
    else:
        print(respuesta.json())
