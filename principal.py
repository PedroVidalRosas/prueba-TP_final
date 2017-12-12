import eleccionDelMenuPrincipal
import modoPredeterminado

def mensajeDeBienvenida():
    print("Bienvenido al juedo de Pedro")
    print("Puede ingresar las sigientes opciones: ")
    print("Si ingresa una opcion invalida saldra del juego")
    print("1 para jugar en modo PREDETERMINADO")
    print("2 para jugar en mmodo ALEATORIO")
    print("3 para salir")

def menuPrincipal():

    eleccion = 0
    while eleccion != 3:

        mensajeDeBienvenida()
        eleccion = eleccionDelMenuPrincipal.eleccionDelMenuPrincipal(input())
        if eleccion== 1:
            usuario = modoPredeterminado.juegopredeterminado()
            print("\n ganaste \n")
        if eleccion == 2:
           print("esre modo esta en construccion")

        if eleccion == 3:
            print("Saliste del Juego de Pedro")
menuPrincipal()