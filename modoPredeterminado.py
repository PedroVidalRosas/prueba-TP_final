import mostrarMapa
import niveles
import modificarMapa


def juegopredeterminado():

    nivel = 1
    while nivel != 6:

        mapa = niveles.niveles((nivel)-1)
        movimientos = (len(mapa))*3
        while movimientos > 0:
            print(movimientos)
            mostrarMapa.interfazGrafica(mapa)

            mapa = modificarMapa.modificarMapa(mapa)

            movimientos -= 1

            if mapa == 'R':
                break



