def eleccionDelMenuPrincipal(eleccion):
    menu = "1234"
    for x in range(len(menu)):
        if menu[x] == eleccion:
            return int(eleccion)
    return 10