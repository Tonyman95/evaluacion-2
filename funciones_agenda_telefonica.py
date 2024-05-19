agenda = {}
contacto = ""
telefono = 0

def agregar_contacto(agenda,contacto,telefono):

    try:

        contacto = input("ingrese nombre del contacto: ")
        telefono = int(input("ingrese el numero de telefono: "))
        agenda[contacto] = telefono
        print("********Contacto ingresado**********")

    except ValueError:
        print("Por favor, ingrese datos correctos")

def eliminar_contacto(agenda):
    eliminar = input("Ingrese el contacto que desea eliminar: ")
    if eliminar in agenda:
        del agenda[eliminar]
        print("*********Contacto Eliminado************")
    else:
        print("Contacto no encontrado")

def encontrar_contacto(agenda):
    encontrar_cont = input("Ingrese el contacto que desea mostrar: ")
    for i,j in agenda.items():
        if encontrar_cont == i:
            print(i, ":", j)
    if encontrar_cont not in agenda:
        print("Contacto no encontrado")

def mostrar_todos(agenda):
    for i,j in agenda.items():
        print(i, ":", j)




    
