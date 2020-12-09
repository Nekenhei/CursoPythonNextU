import requests

_ENDPOINT =  "https://pro-api.coinmarketcap.com/v1/"

def _url():
    return _ENDPOINT+"cryptocurrency/listings/latest"

def get_names():
    headers = {  'Accepts': 'application/json',  'X-CMC_PRO_API_KEY':  '7b40a66d-023d-4747-80b1-f84ff764dcf1'}
    parametros = {'start': 1, 'limit': 5000, 'convert': 'USD'}
    return requests.get(_url(),headers=headers,params=parametros)

data = get_names().json()
moneda1= data["status.timestamp"]
print(moneda1)









