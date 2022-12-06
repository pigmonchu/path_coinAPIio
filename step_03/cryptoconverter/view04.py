from cryptoconverter import MONEDAS
from cryptoconverter.validators import esFloat

def inputFloat(msg):
    valor = input(f"{msg}: ")
    while not esFloat(valor):
        print("Debe introducir un número válido.")
        valor = input(f"{msg}: ")
    return float(valor)      

def inputNotEmpty(msg):
    valor = input(f"{msg}: ").strip()
    while not valor:
        print("Introduzca algún valor.")
        valor = input(f"{msg}: ").strip()
    return valor

def inputInOptions(msg, options):
    valor = input(f"{msg}: ").strip().upper()
    while valor not in options:
        print("Introduce un valor de entre los siguientes: " + ", ".join(options))
        valor = input(f"{msg}: ").strip().upper()
    return valor

class CriptoVista:
    def __init__(self):
        self.criptoDe = ""
        self.criptoA = ""
        self.cantidad = 0

    def intro(self):
        self.criptoDe = inputInOptions("Cripto de", MONEDAS)
        self.criptoA = inputInOptions("Cripto a", MONEDAS)
        self.cantidad = inputFloat("Cantidad De")

    def mostrar(self, tasa):
        print("{} {} son {} {}".format(self.cantidad, self.criptoDe, tasa, self.criptoA))

    def error(self, err):
        print(err)