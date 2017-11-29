def resetearMapa(mapa):
    puntos = 0
    for f in range(len(mapa)):
        for c in range(len(mapa[0])):
            if  mapa[f][c] == '0':
                puntos += 50
    return puntos