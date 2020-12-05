criptos = ["BTC","BCC","LTC","ETH","ETC"]

i=0
total=0
while i<3:
    nombre=input("ingrese el nombre de la moneda")
    if nombre in criptos:
        cant = float(input("Ingrese cantidad que posee de la criptomoneda "+str(i+1)+":"))
        cotiza = float(input("Ingrese cotización en USD de la moneda "+str(i+1)+":"))
        total += cant*cotiza
        i+=1
    else:
        print("Moneda no valida")
print("Acumulado de:",total,"USD")
