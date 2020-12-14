import os
import time

def escribirMoneda(nombreMoneda, cantidadMoneda):
    if os.path.isfile("monedas/"+"%s.txt" % nombreMoneda):
        archivo = open("monedas/"+"%s.txt" % nombreMoneda, "rt")
        cantidad = int(archivo.read())
        archivo.close()
        cantidad += cantidadMoneda
        print(cantidad)
        archivo = open("monedas/"+"%s.txt" % nombreMoneda, "wt")
        archivo.write(str(cantidad))
        archivo.close()
        print("Se ha actualizado la informacion para la moneda:",nombreMoneda)
        time.sleep(5.5)
    else:
        archivo = open("monedas/"+"%s.txt" % nombreMoneda, "wt")
        archivo.write(str(cantidadMoneda))
        archivo.close()
        print("Se ha creado la moneda:",nombreMoneda)
        time.sleep(5.5)

nombre= input("nombre: ")
cantidad = int(input("cantidad: "))

escribirMoneda(nombre,cantidad)