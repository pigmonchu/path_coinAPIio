import requests
from cryptoconverter.model01 import convierte

def esFloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


cripto = input("Criptodivisa de: ")
cantidad = input("Cantidad: ")

while not esFloat(cantidad):
    print("Debe introducir una cantidad.")
    cantidad = input("Cantidad: ")
cantidad = float(cantidad)    

criptoA = input("Criptodivisa a: ")
resultado = convierte (cripto, cantidad, criptoA)
print("{} {} son {} {}".format(cantidad, cripto, resultado, criptoA))