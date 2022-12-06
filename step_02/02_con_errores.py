import requests
from cryptoconverter.model02 import convierte, ErrorConsulta

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
try:
    resultado = convierte (cripto, cantidad, criptoA)
    print("{} {} son {} {}".format(cantidad, cripto, resultado, criptoA))
except ErrorConsulta as e:
    print(e)
