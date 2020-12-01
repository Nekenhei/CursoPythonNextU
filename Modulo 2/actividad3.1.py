cripto = input("indique el nombre de la moneda: ")
cant = float(input("Indique la cantidad de la moneda que posee: "))
dias = int(input("Ingrese la cantidad de dias a cotizar: "))
ganancia = float(input("Indique el porcentaje de ganancia por día: "))

ganancia_total = cant * (ganancia/100) * dias
cant_total = cant + ganancia_total

print("La ganancia final de ",cripto," durante los ",dias," dias, es de: ",ganancia_total)
print("El total final de ",cripto," es de: ",cant_total)