def leerMoneda(conteo):
    nombre = input("Ingrese nombre de la moneda "+str(conteo)+":")
    criptos = ["BTC","BCC","LTC","ETH","ETC"]
    while nombre not in criptos:
        nombre = input("La moneda "+nombre+" no existe. Ingrese el nombre de la moneda: ")
    else:
        print("Moneda Válida")
    cant = float(input("Ingrese cantidad que posee de la criptomoneda "+str(conteo)+":"))
    cotiza = float(input("Ingrese cotización en USD de la moneda "+str(conteo)+":"))
    return nombre, cant, cotiza

nombre1, cant1, cotiza1 = leerMoneda(1)
nombre2, cant2, cotiza2 = leerMoneda(2)
nombre3, cant3, cotiza3 = leerMoneda (3)
total = (cant1*cotiza1)+(cant2*cotiza2)+(cant3*cotiza3)

print("Tiene un total acumulado entre las 3 criptomonedas de:",total"USD")

