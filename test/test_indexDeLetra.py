import indexDeLetra
import unittest

class indexDeLetraTest(unittest.TestCase):

    def testindexDeLetraTestRecibeUnLongitudDeUnMapaIgualANueveDebeDevolvverUnaListaABCDEFGHIJ(self):
        mapa = [["a","a","a","a","a","a","a","a","a","a"]]

        resultado = indexDeLetra.indexLetras(mapa)

        self.assertEqual(resultado,'ABCDEFGHIJ')

    def testindexDeLetraRecibeUnaLongitudDeUnMapaDeCuatroDebeDevolverUnaListaABCDE(self):

        mapa = [["a","a","a","a","a"]]

        resultado = indexDeLetra.indexLetras(mapa)

        self.assertEqual(resultado,'ABCDE')

    def testindexDeLetraRecibeUnaLongitudDeUnMapaDeUnoDebeDevolverA(self):

        mapa = [["a"]]

        resultado = indexDeLetra.indexLetras(mapa)

        self.assertEqual(resultado,'A')

    def indexDeLetraRecibeUnaLongitudDeUNmapaDeDiezDebeDevolverUnalistaVacia(self):

        mapa = [["a","a","a","a","a","a","a","a","a","a","a"]]

        resultado = indexDeLetra.indexLetras(mapa)

        self.assertEqual(resultado,[])

