import json

def guardarDatos(listaPuntos,validacion):

    #leo el archivo json y lo declaro en una variable
    if validacion == True:
        with open('ganadores.json', 'r') as file:
            lista = json.load(file)

    #agrego un nombre y la lista de puntos al archivo json
    listaPuntos.insert(0,input("ingrese su nombre"))
    lista['jugadores'].append(listaPuntos)

    #escribo con la nueva lista el archivo json
    with open('ganadores.json', 'w') as file:
        json.dump(lista, file)
