def eleccionDelMenuPrincipal(eleccion):
    menu = "123"
    for x in range(len(menu)):
        if menu[x] == eleccion:
            return int(eleccion)
    return 3