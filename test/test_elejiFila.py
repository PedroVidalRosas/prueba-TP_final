import unittest
import elejirFila

class elejirFilaTest(unittest.TestCase):

    def testElejirFilaRecibeUnNumeroUnoDeUnIndexDeLUnoAlCincoDeberiaDevolverTrue(self):

        mapa = [
                 ["0","0",".","0","0"],
                 ["0",".","0",".","0"],
                 [".","0","0","0","."],
                 ["0",".","0",".","0"],
                 ["0","0",".","0","0"]

               ]
        posicionFila = "1"

        resultado = elejirFila.verificarFila(posicionFila,mapa)

        self.assertEqual(resultado,True)

    def testElejirFilaRecibeUnNumeroSeisDeUnIndexDelUnoAlCincoDeberiaDevolverFalse(self):

        mapa = [
                 ["0","0",".","0","0"],
                 ["0",".","0",".","0"],
                 [".","0","0","0","."],
                 ["0",".","0",".","0"],
                 ["0","0",".","0","0"]

               ]
        posicionFila = "6"

        resultado = elejirFila.verificarFila(posicionFila,mapa)

        self.assertEqual(resultado,False)

    def testElejirFilaRecibeUnCincoDeUnIndexDelUnoAlCincoDeberiaDevolverTrue(self):

        mapa = [
                 ["0","0",".","0","0"],
                 ["0",".","0",".","0"],
                 [".","0","0","0","."],
                 ["0",".","0",".","0"],
                 ["0","0",".","0","0"]

               ]

        posicionFila = "5"

        resultado = elejirFila.verificarFila(posicionFila,mapa)

        self.assertEqual(resultado,True)

    def testElejirFeilaRecibeUnMenosUnoDeUnIndexDelUnpoAlCincoDeberiaDevolverFalse(self):

        mapa = [
                 ["0","0",".","0","0"],
                 ["0",".","0",".","0"],
                 [".","0","0","0","."],
                 ["0",".","0",".","0"],
                 ["0","0",".","0","0"]

               ]

        posicionFila = "-1"

        resultado = elejirFila.verificarFila(posicionFila,mapa)

        self.assertEqual(resultado,False)

    def testElegirFilaRecibeDosPalabarasDeUnIndexDelUnoAlCincoDeberiaDevolverFalse(self):

        mapa = [
                 ["0","0",".","0","0"],
                 ["0",".","0",".","0"],
                 [".","0","0","0","."],
                 ["0",".","0",".","0"],
                 ["0","0",".","0","0"]

               ]
        posicionFila = "no valido"

        resultado = elejirFila.verificarFila(posicionFila,mapa)

        self.assertEqual(resultado,False)

    def testElejirFilaRecibeVariosEspaciosDeUnIndexDelUnoAlCincoDeberiaDevolverFalse(self):

        mapa = [
             ["0","0",".","0","0"],
             ["0",".","0",".","0"],
             [".","0","0","0","."],
             ["0",".","0",".","0"],
             ["0","0",".","0","0"]

           ]
        posicionFila = "    "

        resultado = elejirFila.verificarFila(posicionFila,mapa)

        self.assertEqual(resultado,False)




