def ConversionCriptomoneda(cantBTC,cantXRP):
    BTCUSD = 7422.50
    XRPUSD = 0.660982

    totalBTC = BTCUSD * cantBTC
    totalXRP = cantXRP * XRPUSD
    total = totalBTC + totalXRP
    return total


cantBTCvar = float(input("Ingrese la cantidad de Bitcoins que tiene: "))
cantXRPvar = float(input("Ingrese la cantidad de Ripple que tiene "))

print("Total acumulado de Bitcoin + Ripple es de:",ConversionCriptomoneda(cantBTCvar, cantXRPvar))
    