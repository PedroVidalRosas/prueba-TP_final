import indexDeLetra

def convertirMapaEnUnaListaDeCadenas(life):
    # convierto el mapa de lista de lista en una lista de cadenas['  '.'  ']
    mapaListaDeCadenas = []
    for x1 in range(len(life)):
        lenn = list(life[x1])
        listaAux = []
        for x2 in range(len(lenn)):
            listaAux.append(life[x1][x2])
            listaAux.append(' ')
        mapaListaDeCadenas.append(''.join(listaAux))
    return mapaListaDeCadenas

def mostrarIndexLetra(letras):
    listaAux= []
    for x in range(len(letras)):

        listaAux.append(letras[x])
        listaAux.append(' ')
    listaAux = ''.join(listaAux)
    print("   ",listaAux)


def mostrarmapa(mapa):
    for x in range(len(mapa)):
        print(x+1,'|', mapa[x])

def interfazGrafica(mapa,nivel,movimientos,puntos):
    print("     Nivel: " + str(nivel))
    print("movimientos: " + str(movimientos) + " puntos: " + str(puntos))

    #letraLista va a ser el indice "ABCDE" que se muestra arriba del mapa
    letralista = indexDeLetra.indexLetras(mapa)

    mapa = convertirMapaEnUnaListaDeCadenas(mapa)

    mostrarIndexLetra(letralista)

    mostrarmapa(mapa)

