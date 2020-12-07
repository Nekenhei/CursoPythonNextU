import requests

_ENDPOINT = "https://api.binance.com"

def _url(api):
    return _ENDPOINT+api

def get_price(cripto):
    return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))

def esMoneda(cripto):
    criptomonedas = ["BTC","BCC","LTC","ETH","ETC","XRP"]
    return cripto in criptomonedas

def esNumero(numero):
    return numero.replace('.',"",1).isdigit()

monedas = []
cantidades = []
cotizaciones = []
i=0

while i<3:
    moneda=input("ingrese el nombre de la moneda #"+str(i+1))
    while not esMoneda(moneda):
        print("Moneda invalida.")
        moneda=input("ingrese el nombre de la moneda #"+str(i+1))
    else:
        monedas.append(moneda)
        data = get_price(moneda+"USDT").json()
        cotizaciones.append(float(data["price"]))
        cantidad = input("Indique la cantidad de "+moneda+":")
        while not esNumero(cantidad):
            cantidad = input("Indique la cantidad de "+moneda+":")
        else:
            cantidades.append(float(cantidad))
    i += 1

i=0
total = 0

while i<3:
    total += cantidades[i]*cotizaciones[i]
    print("Moneda: ",monedas[i],
        ", cantidad: ",cantidades[i],
        ", Cotizacion: ",cotizaciones[i],
        ", Cantidad de USDT: ",cantidades[i]*cotizaciones[i])
    i += 1
    

