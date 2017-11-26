
def indexLetras(mapa):
    letras = "ABCDEFGHIJ"
    letralista= []

    for x in range(0,len(mapa[0])):
        letralista.append(letras[x])
        letralista.append(' ')

    letralista = ''.join(letralista)
    return letralista
