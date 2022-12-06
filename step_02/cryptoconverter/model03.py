import requests
from cryptoconverter import URL

class ErrorConsulta(Exception):
    pass

class ParCriptos:
    def __init__(self, de, a):
        self.de = de
        self.a = a

    def valor(self, cantidad = 1):
        cabecera = {"X-CoinAPI-Key": "23DBFF71-249C-46BB-BB56-9EBDFA5399F6"}
        respuesta = requests.get(URL.format(self.de, self.a), headers=cabecera)

        if respuesta.status_code == 200:
            valor = respuesta.json()["rate"]
            return valor * cantidad
        else:
            error = respuesta.json().get('error', "Sin error definido")
            raise ErrorConsulta(error)

    