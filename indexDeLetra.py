
def indexLetras(mapa):
    """
    Recibe un mapa o nivel y devuelve una lista, en letras en orden alfabetico desde la A hasta la J,
    segun del LEN(MAPA) del mapa
    """

    letras = "ABCDEFGHIJ"
    letralista= []

    if len(mapa[0]) <= len(letras):

        for x in range(0,len(mapa[0])):
            letralista.append(letras[x])
        letralista = ''.join(letralista)

    else:
        return []
    return letralista  
