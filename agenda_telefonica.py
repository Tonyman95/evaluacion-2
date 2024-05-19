from funciones_agenda_telefonica import *

while True:
    while True:
        print("**************Agenda Telefonica****************")
        print("1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Encontrar Contacto")
        print("4. Mostar todos los contactos")
        print("5. Salir")
        try:
            opcion = int(input("ingrese la opcion que desea realizar: "))
        except ValueError:
            print("Por favor ingrese una opcion correcta")

        if opcion > 0 and opcion < 6:
            break
        else:
            print("ingrese una opcion correcta")
    
    if opcion == 1:
        agregar_contacto(agenda,contacto,telefono)
    if opcion == 2:
        eliminar_contacto(agenda)
    if opcion == 3:
        encontrar_contacto(agenda)
    if opcion == 4:
        mostrar_todos(agenda)
    if opcion == 5:
        break