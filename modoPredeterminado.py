import mostrarMapa
import niveles
import modificarMapa
import pasarDeNivel
import resetear
import puntosPorCadaNivel


def juegopredeterminado():

    puntosNivel = []
    puntos = 0
    nivel = 1
    while nivel != 6:

        mapa = niveles.niveles((nivel)-1)
        movimientos = (len(mapa))*3
        while movimientos > 0:

            if puntos < 0:
                print("game over")
                puntos = 0
                nivel = 1
                break


            puntosPorRsetear = resetear.resetearMapa(mapa)

            mostrarMapa.interfazGrafica(mapa,nivel,movimientos,puntos)

            mapa = modificarMapa.modificarMapa(mapa)


            #si los movimientos es igual a cero se reinicia el nivel
            movimientos -= 1
            if movimientos == 0:
                puntos -= 300
                break


            #Si mapa es igual a 'R' se reinicia el nivel
            if mapa == 'R':
                print("Perdio "+ str(puntosPorRsetear)+" puntos por resetear")
                puntos -= puntosPorRsetear
                break

            #Se verifica el mapa que no tenga ninguna luz prendida para aumemtar NIVEL
            pasarNivel = pasarDeNivel.verificarSiHayLucesPrendidas(mapa)
            if pasarNivel == True:
                nivel += 1
                puntos += 500
                puntosNivel = puntosPorCadaNivel.puntosPorCadaNivel(puntosNivel,puntos)
                print(puntosNivel)
                print("Paso de nivel ubtuvo: ", str(puntosNivel[nivel - 2]))
                break


            if movimientos < 0:
                break



