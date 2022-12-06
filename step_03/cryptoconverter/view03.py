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
