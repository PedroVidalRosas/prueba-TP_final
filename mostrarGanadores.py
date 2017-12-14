import json

def leerJson():

    with open('ganadores.json', 'r') as file:
        lista = json.load(file)

    return lista['jugadores']



def mostrarGanadores():

    listaGanadores = leerJson()







