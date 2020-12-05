def leerMoneda(conteo):
    nombre = input("Ingrese nombre de la moneda "+str(conteo)+":")
    cant = float(input("Ingrese cotización en USD de la moneda "+str(conteo)+":"))
    return nombre, cant

nombre1, cant1 = leerMoneda(1)
nombre2, cant2 = leerMoneda(2)
nombre3, cant3 = leerMoneda (3)

if cant1 > cant2 and cant2 > cant3:
    print(nombre1)
    if cant2 > cant3:
        print(nombre2)
        print(nombre3)
    else:
        print(nombre3)
        print(nombre2)
elif cant2 > cant1 and cant1 > cant3:
    print(nombre2)
    if cant1 > cant3:
        print(nombre1)
        print(nombre2)
else:
    print(nombre3)
    if cant1 > cant2:
        print(nombre1)
        print(nombre2)
    else:
        print(nombre2)
        print(nombre1)



    

