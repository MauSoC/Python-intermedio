import os

def listar_archivos(path):
    print("Primera parte imprimir todos los archivos de la carpeta descargas:\n")
    lista = os.scandir(path)
    for ls in lista:
        print(ls.name)


def listar_directorios(path):
    print("----------------------------------------------------------------\n")
    print("Segunda parte imprimir todos los archivos que son carpetas:\n")
    lista = os.scandir(path)
    for ls in lista:
        if ls.is_dir():
            print(ls.name)



def listar_tamanio(path):
    print("----------------------------------------------------------------\n")
    print("Tercera parte imprimir todos los archivos que son carpetas y su tamaño:\n")
    lista = os.scandir(path)
    for ls in lista:
        if ls.is_dir():
            print("nombre: ",ls.name,"\tsize:",os.path.getsize(ls.path))



def listar_todo():
    print("----------------------------------------------------------------\n")
    print("Cuarta parte imprimir todos los archivos que son carpetas y su tamaño apartir de la ubicacion actual:\n")
    lista = os.environ['HOME']
    listaOs = os.scandir(lista)
    listaAux=[]
    for ls in listaOs:
        if ls.is_dir:
            print("nombre: ",ls.name,"\tsize:",os.path.getsize(ls.path))


def main():
    path ="/home/carlos/Descargas"
    listar_archivos(path)
    listar_directorios(path)
    listar_tamanio(path)
    listar_todo()



if __name__ == "__main__":
    main()