import  elejirColumna
import elejirFila
import modificarMapaSegunPosicionDeColumnaFila



def modificarMapa(mapa):

    posicionColumna = elejirColumna.elejirColumna(mapa)
    if posicionColumna == 'R':
        return 'R'
    posicionFila = elejirFila.elejirFila(mapa)
    if posicionFila == 'r':
        return "R"
    posicionFila = int(posicionFila) - 1

    mapa = modificarMapaSegunPosicionDeColumnaFila.prenderOApagarLuz(mapa,posicionColumna,posicionFila)

    return mapa


