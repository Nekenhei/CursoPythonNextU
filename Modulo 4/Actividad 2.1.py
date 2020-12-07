nombre = []
cantidades = []
cotizaciones = []
i = 0

while i<5:
    nombre.append(input("ingrese el nombre de la moneda #"+str(i+1)+":"))
    cantidades.append(float(input("Ingrese la cantidad que posee de la criptomoneda #"+str(i+1)+":")))
    cotizaciones.append(float(input("Ingrese el valor de USD actual de la moneda #"+str(i+1)+":")))
    i += 1

i=0
while i<5:
    print("Moneda:",nombre[i],"cantidad:",str(cantidades[i]),"Cotización:",str(cotizaciones[i]))
    i += 1



