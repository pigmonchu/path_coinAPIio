def esFloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def inputFloat(msg):
    valor = input(f"{msg}: ")
    while not esFloat(valor):
        print("Debe introducir un número válido.")
        valor = input(f"{msg}: ")
    return float(valor)    

