import requests
from cryptoconverter.model import ParCriptos, ErrorConsulta
from cryptoconverter.view03 import inputFloat, inputNotEmpty

cripto = inputNotEmpty("Criptodivisa de")
cantidad = inputFloat("Cantidad")
criptoA = inputNotEmpty("Criptodivisa a: ")

try:
    par = ParCriptos(cripto, criptoA)
    print("{} {} son {} {}".format(cantidad, cripto, par.valor(cantidad), criptoA))
except ErrorConsulta as e:
    print(e)
