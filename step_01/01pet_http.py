import requests

def esFloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


cripto = input("Criptodivisa: ")
cantidad = input("Cantidad: ")
while not esFloat(cantidad):
    print("Debe introducir una cantidad.")
    cantidad = input("Cantidad: ")

cantidad = float(cantidad)

cabecera = {"X-CoinAPI-Key": "23DBFF71-249C-46BB-BB56-9EBDFA5399F6"}
respuesta = requests.get("https://rest.coinapi.io/v1/exchangerate/{}/EUR".format(cripto), headers=cabecera)

if respuesta.status_code == 200:
    valor = respuesta.json()["rate"]
    print(valor * cantidad, "€")
else:
    print(respuesta.json())
