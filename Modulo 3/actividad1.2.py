conteo = 1
total = 0
cant = 0
valor = 0


while conteo <= 5:
    cant = float(input("Ingrese cantidad de la moneda "+str(conteo)+":"))
    valor = float(input("ingrese valor cotización de la moneda "+str(conteo)+":"))
    total += (cant * valor)
    conteo += 1
    cant = 0
    valor = 0
print("El valor acumulado es de $USD",total)
