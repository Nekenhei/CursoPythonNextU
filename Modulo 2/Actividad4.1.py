from datetime import datetime

nombreCripto = input("ingrese el nombre de la criptomoneda: ")
cantidadCripto = float(input("Ingrese la cantidad que posee de la criptomoneda:"))
valorCripto = float(input("Ingrese la cotización por unidad de moneda en USD: "))

fecha = datetime.now()
cotizaCripto = valorCripto * cantidadCripto

print("A la fecha de consulta :",fecha.strftime("%A %d/%B/%Y %I:%M:%S%p"),"la criptomoneda",nombreCripto,"tiene un valor de:",cotizaCripto)

