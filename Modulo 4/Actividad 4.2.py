import requests

def esMoneda(cripto):
    return cripto in monedas_list

monedas_list = ()
monedas_dict = {}


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

for moneda in data["data"]:
    #monedas_dict[data["data"][id]["symbol"]]=data["data"][id]["quotes"]["USD"]["price"]
    monedas_dict[moneda["symbol"]]=moneda["quote"]["USD"]["price"]

monedas_list=monedas_dict.keys()

monedaUsuario=input("ingrese el nombre de la moneda a verificar")
while not esMoneda(monedaUsuario):
    print("Moneda invalida.")
    monedaUsuario=input("ingrese el nombre de la moneda")
else:
    print("La moneda con simbolo:",monedaUsuario,
    "tiene un precio de:",monedas_dict.get(monedaUsuario),"USD según coimnmarketcap.com")
