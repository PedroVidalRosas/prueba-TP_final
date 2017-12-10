

def puntosPorCadaNivel(puntosNiveles,puntos):

    sumaDePuntos = 0
    if len(puntosNiveles) == 0:
        puntosNiveles.append(puntos)
        return puntosNiveles
    if len(puntosNiveles) > 0:
        for x in range(len(puntosNiveles)):
            sumaDePuntos = sumaDePuntos + puntosNiveles[x]
        puntosNiveles.append(puntos - sumaDePuntos)
    return puntosNiveles

