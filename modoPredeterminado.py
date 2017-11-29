import mostrarMapa
import niveles
import modificarMapa
import pasarDeNivel


def juegopredeterminado():
    puntos = 0
    nivel = 1
    while nivel != 6:

        mapa = niveles.niveles((nivel)-1)
        movimientos = (len(mapa))*3
        while movimientos > 0:


            mostrarMapa.interfazGrafica(mapa,nivel,movimientos,puntos)

            mapa = modificarMapa.modificarMapa(mapa)

            movimientos -= 1
            if movimientos == 0:
                puntos -= 300
                break

            #Si mapa es igual a 'R' se reinicia el nivel
            if mapa == 'R':
                puntos -= 300
                break

            #Se verifica el mapa que no tenga ninguna luz prendida para aumemtar NIVEL
            pasarNivel = pasarDeNivel.verificarSiHayLucesPrendidas(mapa)
            if pasarNivel == True:
                nivel += 1
                puntos += 500
                break


            if movimientos < 0:
                break



