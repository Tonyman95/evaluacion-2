
numeros = []
print("Bienvenido, ingrese 3 numeros para determinar cual es el numero mayor")
while True:
    try:
        numero_1 = int(input("ingrese numero 1: "))
        numero_2 = int(input("ingrese numero 2: "))
        numero_3 = int(input("ingrese numero 3: "))

        numeros.append(numero_1)
        numeros.append(numero_2)
        numeros.append(numero_3)
        break
    except ValueError:
        print("*******Por Favor ingrese numeros*********")

print("El numero mayor es: ", max(numeros))

