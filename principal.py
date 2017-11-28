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
    mensajeDeBienvenida()
    eleccion = eleccionDelMenuPrincipal.eleccionDelMenuPrincipal(input())
    if eleccion== 1:
        modoPredeterminado.juegopredeterminado()
    if eleccion == 2:
       print("esre modo esta en construccion")

    if eleccion == 3:
        print("Saliste del Juego de Pedro")
menuPrincipal()