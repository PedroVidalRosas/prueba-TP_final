import indexDeLetra

def verificarColumna(posicionColumna,mapa):
    """
    Verifica si la opcion que se ingreso este dentro del index de columna, si esta
    devuelve True, si no esta devuelve False
    """
    if posicionColumna == 'R':
        return True
    menu = indexDeLetra.indexLetras(mapa)
    for x in range(len(menu)):
        if menu[x] == posicionColumna:
            return True
    return False

def devolverPosicionDeLetraDelIndex(posicionColumna,mapa):
    """
    devuelve la posicion, en numero, de la letra que se elijio
    """
    menu = indexDeLetra.indexLetras(mapa)
    for x in range(len(menu)):
        if menu[x] == posicionColumna:
            return x

def elejirColumna(mapa):
    menu = indexDeLetra.indexLetras(mapa)
    columna = False
    while columna != True:
        posicionColumna = input("Ingrese una LETRA de "+ menu + " para columna o R para reiciniar").upper()
        if posicionColumna == 'R':
            return posicionColumna
        columna = verificarColumna(posicionColumna,mapa)

        if columna == False:
            print("opcion invalida ingrese de nuevo")
    posicionColumna = devolverPosicionDeLetraDelIndex(posicionColumna,mapa)
    return posicionColumna
