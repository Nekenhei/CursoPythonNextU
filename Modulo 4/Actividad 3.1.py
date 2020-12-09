import requests
#Creo endpoint y lista
_ENDPOINT =  "https://pro-api.coinmarketcap.com/v1/"
lista_monedas = []


#Metodo que devuelve URL de api
def _url():
    return _ENDPOINT+"cryptocurrency/listings/latest"

#metodo que buscará la moneda del usuario
#dentro de las monedas obtenidas por la API
def esMoneda(cripto):
    return cripto in monedas

#metodo que llama a la api dados parametros de la documentacion y devuelve respuesta
def get_names():
    headers = {  'Accepts': 'application/json',  'X-CMC_PRO_API_KEY':  '7b40a66d-023d-4747-80b1-f84ff764dcf1'}
    parametros = {'start': 1, 'limit': 5000, 'convert': 'USD'}
    return requests.get(_url(),headers=headers,params=parametros)

#llamo a metodo de api y convierto respuesta en JSON
data = get_names().json()


#recorro la respuesta en su espacio "data" (también existe response)
#y por cada objeto JSON devuelto, extraigo su nombre symbol
#se guarda nombre en lista_monedas
for moneda in data["data"]:
    lista_monedas.append(moneda["symbol"])

#creo tupla a partir de lista
monedas = tuple(lista_monedas)

monedaUsuario=input("ingrese el nombre de la moneda a verificar")
while not esMoneda(monedaUsuario):
    print("Moneda invalida.")
    monedaUsuario=input("ingrese el nombre de la moneda")
else:
    print("La moneda,",monedaUsuario,"es valida porque existe en coimnmarketcap.com")







#criptoTotal= data["data"]
#criptoNames = criptoTotal[2]
#criptosymbol = criptoNames["symbol"]
#print(criptosymbol)









