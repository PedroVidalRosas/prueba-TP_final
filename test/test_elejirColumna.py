import unittest
import elejirColumna

class elejirColumnaTest(unittest.TestCase):

    def testElejirColumnaRecibeUnaLetraADeUnIndexABCDEDDeberiaDevolverTrue(self):

        mapa = [
             ["0","0",".","0","0"],
             ["0",".","0",".","0"],
             [".","0","0","0","."],
             ["0",".","0",".","0"],
             ["0","0",".","0","0"]

           ]
        posicionColumna = "A"

        resultado = elejirColumna.verificarColumna(posicionColumna,mapa)

        self.assertEqual(resultado,True)

    def testElejirColumnaRecibeEDeUnIndexABCDEDeberiaDevolverTrue(self):
        mapa = [
            ["0", "0", ".", "0", "0"],
            ["0", ".", "0", ".", "0"],
            [".", "0", "0", "0", "."],
            ["0", ".", "0", ".", "0"],
            ["0", "0", ".", "0", "0"]

                ]
        posicionColumna = "E"

        resultado = elejirColumna.verificarColumna(posicionColumna,mapa)

        self.assertEqual(resultado,True)

    def testElejirColumnaRecibeUnNumeroDosDeberiaDevolverFalse(self):

        mapa = [
            ["0", "0", ".", "0", "0"],
            ["0", ".", "0", ".", "0"],
            [".", "0", "0", "0", "."],
            ["0", ".", "0", ".", "0"],
            ["0", "0", ".", "0", "0"]

                ]
        posicionColumna = "2"

        resultado = elejirColumna.verificarColumna(posicionColumna,mapa)

        self.assertEqual(resultado,False)

    def testElejidColumnaRecibeVariosEspaciosDeberiaDevolverFalse(self):
        mapa = [
            ["0", "0", ".", "0", "0"],
            ["0", ".", "0", ".", "0"],
            [".", "0", "0", "0", "."],
            ["0", ".", "0", ".", "0"],
            ["0", "0", ".", "0", "0"]

        ]
        posicionColumna = "    "

        resultado = elejirColumna.verificarColumna(posicionColumna,mapa)

        self.assertEqual(resultado,False)

    def testElejirColumnaRecibeDosPalabarasDeberiaDevolverFalse(self):
        mapa = [
            ["0", "0", ".", "0", "0"],
            ["0", ".", "0", ".", "0"],
            [".", "0", "0", "0", "."],
            ["0", ".", "0", ".", "0"],
            ["0", "0", ".", "0", "0"]

        ]
        posicionColumna = "no valido"

        resultado = elejirColumna.verificarColumna(posicionColumna,mapa)

        self.assertEqual(resultado,False)

    def testElejirColumnaRecibeUnaPalabraDebveriaDevolverFalse(self):
        mapa = [
            ["0", "0", ".", "0", "0"],
            ["0", ".", "0", ".", "0"],
            [".", "0", "0", "0", "."],
            ["0", ".", "0", ".", "0"],
            ["0", "0", ".", "0", "0"]

        ]
        posicionColumna = "novalido"

        resultado = elejirColumna.verificarColumna(posicionColumna,mapa)

        self.assertEqual(resultado,False)

    def testdevolverPosicionDeLetraDelIndexRecineUnaLetraADeberiaDevolverUnCero(self):
        mapa = [
            ["0", "0", ".", "0", "0"],
            ["0", ".", "0", ".", "0"],
            [".", "0", "0", "0", "."],
            ["0", ".", "0", ".", "0"],
            ["0", "0", ".", "0", "0"]

        ]
        posicionColumna = "A"

        resultado = elejirColumna.devolverPosicionDeLetraDelIndex(posicionColumna,mapa)

        self.assertEqual(resultado,0)

    def testdevolverPosicionDeLetraDelIndexRecibeUnaLetraEDeberiaDevolverUnCuatro(self):
        mapa = [
            ["0", "0", ".", "0", "0"],
            ["0", ".", "0", ".", "0"],
            [".", "0", "0", "0", "."],
            ["0", ".", "0", ".", "0"],
            ["0", "0", ".", "0", "0"]

        ]
        posicionColumna = "E"

        resultado = elejirColumna.devolverPosicionDeLetraDelIndex(posicionColumna, mapa)

        self.assertEqual(resultado, 4)

