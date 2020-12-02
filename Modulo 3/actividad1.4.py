def leerMoneda(conteo):
    cant = float(input("Ingrese valor de la moneda "+str(conteo)+":"))
    valor = float(input("Ingrse cotización en USD de la moneda "+str(conteo)+":"))
    total = cant * valor
    return total

conteoVar = 1
totalmoneda = 0

while conteoVar <=5:
    totalmoneda += leerMoneda(conteoVar)
    conteoVar += 1


print(totalmoneda)