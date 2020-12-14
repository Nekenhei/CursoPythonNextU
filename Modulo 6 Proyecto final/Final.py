import requests
import datetime
from datetime import date
import os.path
import time
#-------------------------------
#Creacion de variables y listas a usar
#-------------------------------

opcion =  0
codigoNuestro = 951111
diccionario_monedas = dict()
lista_monedas = []

#-------------------------------
#Creacion de funciones y llamadas a API
#-------------------------------

#Funcion que revisa que el codigo no sea el propio
def validarCodigo(codigoEnvio, codigoPropio):
    if codigoEnvio == codigoPropio:
        flag = True
        return flag
    else:
        flag = False
        return flag


#Llamada a API
COINMARKET_API_KEY = "7b40a66d-023d-4747-80b1-f84ff764dcf1"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}
parametros = {
    'start': 1,
    'limit': 5000,
    'convert': 'USD'
}

data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers,params=parametros).json()

#metodo que buscará la moneda del usuario
#dentro de las monedas obtenidas por la API
def esMoneda(cripto):
    return cripto in lista_monedas


#se popula el diccionario con simbolo y nombre de las criptomonedas
for moneda in data["data"]:
    diccionario_monedas[moneda["symbol"]]=[moneda["name"],moneda["quote"]["USD"]["price"]]

lista_monedas = diccionario_monedas.keys()

def solicitaMoneda():
    monedaUsuario=input("ingrese el nombre de la moneda a verificar: ")
    while not esMoneda(monedaUsuario):
        print("Moneda invalida.")
        monedaUsuario=input("ingrese el nombre de la moneda: ")
    else:
        monedaConsulta = diccionario_monedas.get(monedaUsuario)
        print("La moneda con simbolo:",monedaUsuario,"nombre:",monedaConsulta[0],"y valor:",monedaConsulta[1],"es valida porque existe en coimnmarketcap.com")
        return monedaUsuario

def leerMoneda(nombreMoneda):
    if os.path.isfile("monedas/"+"%s.txt" % nombreMoneda):
        archivo = open("monedas/"+"%s.txt" % nombreMoneda, "rt")
        cantidad = int(archivo.read())
        monedaArchivo = diccionario_monedas.get(nombreMoneda)
        cantidad = cantidad * monedaArchivo[1]
        print("")
        print("La moneda",monedaArchivo[0],"tiene un balance a hoy",date.today().strftime("%B %d, %Y"),"de:",cantidad)
        print("Cotizacion en USD:",monedaArchivo[1])
        print("")
        archivo.close()
    else:
        print('''
        La moneda no cuenta con informacion en el monedero
        ''')
    
def leerMonedas(nombreMoneda):
    archivo = open("monedas/"+"%s.txt" % nombreMoneda, "rt")
    cantidad = int(archivo.read())
    monedaArchivo = diccionario_monedas.get(nombreMoneda)
    cantidad = cantidad * monedaArchivo[1]
    print("")
    print("La moneda",monedaArchivo[0],"tiene un balance a hoy",date.today().strftime("%B %d, %Y"),"de:",cantidad)
    print("Cotizacion en USD:",monedaArchivo[1])
    print("")
    archivo.close()
    return cantidad


def escribirMoneda(nombreMoneda, cantidadMoneda):
    if os.path.isfile("monedas/"+"%s.txt" % nombreMoneda):
        archivo = open("monedas/"+"%s.txt" % nombreMoneda, "rt")
        cantidad = int(archivo.read())
        archivo.close()
        if (cantidad + cantidadMoneda) >= 0:
            cantidad += cantidadMoneda
            archivo = open("monedas/"+"%s.txt" % nombreMoneda, "wt")
            archivo.write(str(cantidad))
            archivo.close()
            print("Se ha actualizado la informacion para la moneda:",nombreMoneda)
            flag = True
        else:
            print("no tiene fondos suficientes en la moneda",nombreMoneda)
            flag = False
    else:
        archivo = open("monedas/"+"%s.txt" % nombreMoneda, "wt")
        archivo.write(str(cantidadMoneda))
        archivo.close()
        print("Se ha creado la moneda:",nombreMoneda)
        flag = True
    return flag

def leerTransacciones():
    print('''A continuación, las transacciones en orden cronologico: 
        ''')
    archivo = open("transacciones.txt", "rt")
    for x in archivo:
        print(x)
    archivo.close()
    print("Fin del archivo")

def escribirTransaccion(transaccionTexto):
    archivo = open("transacciones.txt", "at")
    archivo.write(transaccionTexto+"\n")
    archivo.close()
    

#def leerBalance():
    


#-------------------------------
#Menu de operacion
#-------------------------------
while opcion != 6:
    print('''Menu Princial:
    1: Recibir Cantidad.
    2: Enviar Cantidad.
    3: Mostrar Saldo de una moneda especifica.
    4: Mostrar balance del monedero virtual.
    5: Mostrar historico de transacciones.
    6: Salir
    ''')
    opcion = int(input("Ingrese una opcion: "))
    
    #seccion para recibir dinero
    if opcion == 1:
        codigo = int(input("Ingrese el codigo de su cuenta: "))
        #Revision de codigo cuenta propia
        while not validarCodigo(codigo, codigoNuestro):
            print("Codigo erroneo")
            codigo = int(input("Ingrese el codigo de su cuenta: "))
        else:
            print("Ok")            

        #solicitador de moneda
        monedaIngresada = solicitaMoneda()
        montoRecibir = int(input("Ingrese la cantidad de "+monedaIngresada+" a recibir: "))
        
        #limpia variable opcion
        
        bandera = escribirMoneda(monedaIngresada,montoRecibir)
        if bandera == True :
            texto = str(datetime.datetime.now()) + ", se ingreso la cantidad de "+str(montoRecibir)+" para la moneda "+monedaIngresada
            print(texto)
            escribirTransaccion(texto)
        else:
            print("Transaccion fallida")
        opcion = 0
    
    #seccion para enviar dinero
    elif opcion == 2:
        codigo = int(input("Ingrese el codigo de la cuenta destinataria: "))
        #Revision de codigo cuenta propia
        while validarCodigo(codigo, codigoNuestro):
            print("Codigo erroneo, no puede ser su propia cuenta")
            codigo = int(input("Ingrese el codigo de la cuenta a enviar: "))
        else:
            print("Ok") 

        #solicitador de moneda
        monedaIngresada = solicitaMoneda()
        montoEnvio = int(input("Ingrese la cantidad de "+monedaIngresada+" a enviar: "))      
        texto = str(datetime.datetime.now()) + ", se retiro la cantidad de "+str(montoEnvio)+" para la moneda "+monedaIngresada+" Enviada a la cuenta: "+str(codigo)
        
        montoEnvio = montoEnvio*-1
        bandera = escribirMoneda(monedaIngresada,montoEnvio)

        if bandera == True:
            print(texto)
            escribirTransaccion(texto)
        else:
            print("Transaccion fallida")

        #limpia variable opcion
        opcion = 0          
    
    #Seccion para consultar moneda
    elif opcion == 3:
        #solicitador de moneda
        monedaIngresada = solicitaMoneda()
        leerMoneda(monedaIngresada)

    #Seccion para consultar balance
    elif opcion == 4:

        acumulado = 0
        for filename in os.listdir("monedas/"):
            nombreFile = str(os.path.splitext(filename)[0])
            acumulado += leerMonedas(nombreFile)
        
        print("Su acumulado en USD a la fecha es de:",acumulado)

    #Seccion para consultar transacciones
    elif opcion == 5:
        leerTransacciones()

    #salida del menu
    pass

print("Hasta Pronto")






