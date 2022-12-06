import requests
from cryptoconverter.model import ParCriptos, ErrorConsulta
from cryptoconverter.view02 import inputFloat

cripto = input("Criptodivisa de: ")
cantidad = inputFloat("Cantidad")
criptoA = input("Criptodivisa a: ")

try:
    par = ParCriptos(cripto, criptoA)
    print("{} {} son {} {}".format(cantidad, cripto, par.valor(cantidad), criptoA))
except ErrorConsulta as e:
    print(e)
