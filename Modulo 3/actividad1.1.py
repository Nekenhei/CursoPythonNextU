moneda1 = input("Digite nombre de la moneda 1:")
valor1 = float(input("Digite valor de la moneda 1: "))
moneda2 = input("Digite nombre de la moneda 2:")
valor2 = float(input("Digite valor de la moneda 2: "))
moneda3 = input("Digite nombre de la moneda 3:")
valor3 = float(input("Digite valor de la moneda 3: "))

if valor1 > valor2 and valor2 > valor3:
    print(moneda1,"cotiza a",valor1)
    if valor2 > valor3:
        print(moneda2,"cotiza a",valor2)
        print(moneda3,"cotiza a",valor3)
    else:
        print(moneda3,"cotiza a",valor3)
        print(moneda2,"cotiza a",valor2)
elif valor2 > valor1 and valor2 > valor3:
    print(moneda2,"cotiza a",valor2)
    if valor2 > valor3:
        print(moneda2,"cotiza a",valor2)
        print(moneda3,"cotiza a",valor3)
    else:
        print(moneda3,"cotiza a",valor3)
        print(moneda2,"cotiza a",valor2)
else:
    print(moneda3,"cotiza a",valor3)
    if valor1 > valor2:
        print(moneda1,"cotiza a",valor1)
        print(moneda2,"cotiza a",valor2)
    else:
        print(moneda2,"cotiza a",valor2)
        print(moneda1,"cotiza a",valor1)