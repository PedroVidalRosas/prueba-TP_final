import json

def devolverListaGanadores():

    with open('ganadores.json', 'r') as file:
        lista = json.load(file)

    return lista['jugadores']

def ordenarDeMayorAMenorGanadores():

    listaGanadores = devolverListaGanadores()

    listaFinal = []

    for l in range(len(listaGanadores)):
        lista = []
        puntos = 0
        for c in range(1,len(listaGanadores[l])):
            puntos = puntos + listaGanadores[l][c]
        lista.append(puntos)
        lista.append(listaGanadores[l][0])
        listaFinal.append(lista)
    listaFinal.sort()

    return listaFinal

def mostrarGanadores():

    listaDeGanadores = ordenarDeMayorAMenorGanadores()
    listaDeGanadores.reverse()

    for x in range(len(listaDeGanadores)):
        print(listaDeGanadores[x][1],listaDeGanadores[x][0])
