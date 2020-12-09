import requests
#Creo endpoint y lista

diccionario_monedas = dict()
lista_monedas = []

#Llamada a API
COINMARKET_API_KEY = "7b40a66d-023d-4747-80b1-f84ff764dcf1"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}
parametros = {
    'start': 1,
    'limit': 5000,
    'convert': 'USD'
}

data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers,params=parametros).json()


#metodo que buscará la moneda del usuario
#dentro de las monedas obtenidas por la API
def esMoneda(cripto):
    return cripto in lista_monedas


#se popula el diccionario con simbolo y nombre de las criptomonedas
for moneda in data["data"]:
    diccionario_monedas[moneda["symbol"]]=moneda["name"]

lista_monedas = diccionario_monedas.keys()

monedaUsuario=input("ingrese el nombre de la moneda a verificar")
while not esMoneda(monedaUsuario):
    print("Moneda invalida.")
    monedaUsuario=input("ingrese el nombre de la moneda")
else:
    print("La moneda con simbolo:",monedaUsuario,"y nombre:",diccionario_monedas.get(monedaUsuario),"es valida porque existe en coimnmarketcap.com")










