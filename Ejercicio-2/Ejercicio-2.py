import os

def llenado():
    nombre = input("Ingrese un nombre para el usuario: ")
    telefono = input("Ingrese el numero: ")
    return nombre,telefono

def buscar(dic):
    name = input("ingrese el nombre que desea buscar: ")
    for i,j in dic.items():
        if name in i:
            print(i,j)
def menu():
    ban = True
    opcion = 0
    dic={}
    
    while ban:
        print("""
        Elija una opcion:
        1.- Agregar Contacto
        2.- Buscar contacto
        3.- salir
        """)
        opcion = int(input())

        if opcion == 1:
            nombre,telefono = llenado()
            dic[nombre]=telefono
            os.system ("clear") 

        elif opcion == 2:
            buscar(dic)
            
        else:
            ban=False


def main():
    menu()


if __name__ == "__main__":
    main()