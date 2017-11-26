import indexDeLetra
import niveles

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

def mostrarmapa(mapa):
    for x in range(len(mapa)):
        print(x+1,'|', mapa[x])

def interfazGrafica(mapa):

    #letraLista va a ser el index "ABCDE" que se muestra arriba del mapa
    letralista = indexDeLetra.indexLetras(mapa)

    mapa = convertirMapaEnUnaListaDeCadenas(mapa)

    print("   ",letralista)
    mostrarmapa(mapa)

mapa = niveles.nivel3D(2)
interfazGrafica(mapa)