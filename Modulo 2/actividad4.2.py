from datetime import datetime

nombreCripto = input("ingrese el nombre de la criptomoneda: ")
cantidadCripto = float(input("Ingrese la cantidad que posee de la criptomoneda:"))
valorCripto = float(input("Ingrese la cotización por unidad de moneda en USD: "))

fecha = datetime.now()
cotizaCripto = valorCripto * cantidadCripto

print("A la fecha de consulta :",fecha.strftime("%A %d/%B/%Y %I:%M:%S%p"),"la criptomoneda",nombreCripto,"tiene un valor de:",cotizaCripto)
valor1 = cantidadCripto*1.05
valor2 = valor1*1.05
valor3 = valor2*1.05
valor4 = valor3*1.05
valor5 = valor4*1.05
valor6 = valor5*1.05
valor7 = valor6*1.05


print("su ganancia pasada una semana es de",valor7)