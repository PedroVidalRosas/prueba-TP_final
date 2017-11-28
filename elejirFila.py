def menuFila(mapa):
    menu = []

    for x in range(len(mapa)+1):
        menu.append(x)

    return menu
def verificarFila(posicionFila,mapa):
    #si es R retorna True
    if posicionFila == 'r':
        return True
    #si posicionFila no se puede convertir en un entero restorna False
    try:
        posicionFila = int(posicionFila)
    except:
        return False
    menu = menuFila(mapa)
    for x in range(len(menu)):
        if menu[x] == int(posicionFila):
            return True
    return False

def elejirFila(mapa):
    fila = False
    while fila != True:
        posicionFila = input("Ingrese un Numero del 1 al " + str(len(mapa)) +" para FILA o R para reiniciar")
        fila = verificarFila(posicionFila,mapa)

        if fila == False:
            print("ingreso una opcion invalida ingrese una opcion valida")

    return posicionFila

