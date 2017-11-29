

def verificarSiHayLucesPrendidas(mapa):

    for f in range(len(mapa)):
        for c in range(len(mapa[0])):
            if mapa[f][c] != '.':
                return False

    return True
