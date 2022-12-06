from cryptoconverter.validators import esFloat

def inputFloat(msg):
    valor = input(f"{msg}: ")
    while not esFloat(valor):
        print("Debe introducir un número válido.")
        valor = input(f"{msg}: ")
    return float(valor)    

