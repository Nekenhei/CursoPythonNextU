BTCCop = 3200
DASHCop = 5000
LTCCop = 1000


moneda = input("Ingrese la moneda a utlizar (BTC, DASH, LTC):")


if moneda == "BTC" or moneda == "DASH" or moneda == "LTC":
    cant = float(input("Ingrese la cantidad de dicha moneda a recargar:"))
    if moneda == "BTC":
        total = BTCCop * cant
    elif moneda == "DASH":
        total = DASHCop * cant
    else:
        total = LTCCop * cant
    print("El valor cargado fue de $",total,"COP")
else:
    "Moneda no aceptada, use una de la lista"
