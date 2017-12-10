import unittest
import resetear

class resetearMapaTest(unittest.TestCase):

    def testrestearMapaRecibeUnaMapaSinCerosDeberiaDevolverCeroPuntos(self):

        mapa = [
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
        resultado = resetear.resetearMapa(mapa)

        self.assertEqual(resultado,0)

    def testResetearMapaRecibeUnMapaConUnCeroDeberiaDevolverCicuentaPuntos(self):
        mapa = [
            [".", ".", ".", "0"],
            [".", ".", ".", "."]
            ]
        resultado = resetear.resetearMapa(mapa)

        self.assertEqual(resultado,50)

    def testResetearMapaRecibeUnmapaConDosCerosDeberiaDevolverCienPuntos(self):
        mapa = [
            [".", ".", ".", "0"],
            ["0", ".", ".", "."]
            ]
        resultado = resetear.resetearMapa(mapa)

        self.assertEqual(resultado,100)

    def testResetarMapaRecibeUnMapaConOchoCerosDeberiaDevolverOchoCeros(self):
        mapa = [
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"]
            ]
        resultado = resetear.resetearMapa(mapa)

        self.assertEqual(resultado,400)