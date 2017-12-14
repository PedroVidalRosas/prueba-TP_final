import eleccionDelMenuPrincipal
import modoPredeterminado
import GuardarUsuariosGanadores
import mostrarGanadores

def mensajeDeBienvenida():
    print("Bienvenido al juedo de Pedro")
    print("Puede ingresar las sigientes opciones: ")
    print("Si ingresa una opcion invalida saldra del juego")
    print("1 para jugar en modo PREDETERMINADO")
    print("2 para jugar en mmodo ALEATORIO")
    print("3 mostrar ganadores")
    print("4 para salir")

def menuPrincipal():

    eleccion = 0
    while eleccion != 3:

        mensajeDeBienvenida()
        eleccion = eleccionDelMenuPrincipal.eleccionDelMenuPrincipal(input())
        if eleccion== 1:
            usuario,validacion = modoPredeterminado.juegopredeterminado()
            print("\n Ganaste \n")
            GuardarUsuariosGanadores.guardarDatos(usuario,validacion)

        if eleccion == 2:
           print("esre modo esta en construccion")

        if eleccion == 3:
            mostrarGanadores.mostrarGanadores()

        if eleccion == 4:
            print("Saliste del Juego de Pedro")
menuPrincipal()