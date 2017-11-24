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
        print(mapa[x])

letras = "ABCDEFGHIJ"

mapa = [
    ["0","0",".","0"],
    [".",".","0","."]
]
letralista= []

for x in range(0,len(mapa[0])):
    letralista.append(letras[x])
    letralista.append(' ')

letralista = ''.join(letralista)
mapa = convertirMapaEnUnaListaDeCadenas(mapa)

p = []
for index,item in enumerate(mapa,1):
    o = []
    o.append(index)
    o.append(item)
    p.append(o)
print("    ",letralista)
mostrarmapa(p)