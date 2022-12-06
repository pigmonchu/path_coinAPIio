import requests
from cryptoconverter.model03 import ParCriptos, ErrorConsulta

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
    par = ParCriptos(cripto, criptoA)
    
    print("{} {} son {} {}".format(cantidad, cripto, par.valor(cantidad), criptoA))
except ErrorConsulta as e:
    print(e)
