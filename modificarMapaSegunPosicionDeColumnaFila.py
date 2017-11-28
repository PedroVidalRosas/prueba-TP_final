def movimientoDerecha(mapa,columna,fila):
    if columna + 1 <= (len(mapa)-1):
        if mapa[fila][columna + 1] == '0':
            mapa[fila][columna + 1] = '.'
        elif mapa[fila][columna + 1] == '.':
            mapa[fila][columna + 1] = '0'
    return mapa

def movimientoIzquierdo(mapa,columna,fila):
    if columna - 1 >= 0:
        if mapa[fila][columna - 1] == '0':
            mapa[fila][columna - 1] = '.'
        elif mapa[fila][columna - 1] == '.':
            mapa[fila][columna - 1] = '0'
    return mapa

def movientoAbajo(mapa,columna,fila):

    if fila + 1 <= (len(mapa) - 1):
        if mapa[fila + 1][columna] == '0':
            mapa[fila + 1][columna] = '.'
        elif mapa[fila + 1][columna] == '.':
            mapa[fila + 1][columna] = '0'

    return mapa

def movientoArriba(mapa,columna,fila):

    if fila - 1 >= 0:
        if mapa[fila - 1][columna] == '0':
            mapa[fila - 1][columna] = '.'
        elif mapa[fila - 1][columna] == '.':
            mapa[fila - 1][columna] = '0'

    return mapa


def prenderOApagarLuz(mapa,columna,fila):

    # modico donde esta la posicion de columna y fila
    if mapa[fila][columna] == '0':
        mapa[fila][columna] = '.'
    elif mapa[fila][columna] == '.':
        mapa[fila][columna] = '0'

    # modifico donde esta la pocicion a la derecha de la posicion de columna y fila
    mapa = movimientoDerecha(mapa,columna,fila)

    # modifo donde esta la posicion a la izquierda de la posicion de columna y fila
    mapa = movimientoIzquierdo(mapa,columna,fila)

    # modificar donde esta la pocicion hacia abajo de la posicion de columna y fila
    mapa = movientoAbajo(mapa,columna,fila)

    # modifico donde esta la posicion hacia arriba de la posicion de columna y fila
    mapa = movientoArriba(mapa,columna,fila)

    return mapa