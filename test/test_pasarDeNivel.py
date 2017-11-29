import unittest
import pasarDeNivel

class verificarSiHayLucesPrendidasTest(unittest.TestCase):

    def testverificarSiHayLucesPrendidasRecibeUnMapaConTodosPuntosDeberiaDevolverTrue(self):

        mapa = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]

        resultado = pasarDeNivel.verificarSiHayLucesPrendidas(mapa)

        self.assertEqual(resultado,True)

    def testverificarSiHayLucesPrendidasRecibeUnMapaConTodosCerosDeberiaDevolverFalse(self):
        mapa = [
            ['0', '0', '0'],
            ['0', '0', '0'],
            ['0', '0', '0'],
            ]
        resultado = pasarDeNivel.verificarSiHayLucesPrendidas(mapa)

        self.assertEqual(resultado,False)

    def testverificarSiHayLucesPrendidasRecibeUnMapaConTodosPuntosYUnCeroEnUnaEsquinaArribaALaDerechaDeberiaDevolverFalse(self):
        mapa = [
            ['.', '.', '0'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        resultado = pasarDeNivel.verificarSiHayLucesPrendidas(mapa)

        self.assertEqual(resultado,False)

    def testverificarSiHayLucesPrendidasRecibeUnMapaConTodosPuntosYUnCeroEnUnaEsquinaAbajoALaDerechaDeberiaDevolverFalse(self):
        mapa = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '0'],
        ]
        resultado = pasarDeNivel.verificarSiHayLucesPrendidas(mapa)

        self.assertEqual(resultado,False)

    def testverificarSiHayLucesPrendidasRecibeUnMapaConTodosPuntosYUnCeroEnUnaEsquinaAbajoALaIzquierdaDeberiaDevolverFalse(self):
        mapa = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['0', '.', '.'],
        ]
        resultado = pasarDeNivel.verificarSiHayLucesPrendidas(mapa)

        self.assertEqual(resultado,False)

    def testverificarSiHayLucesPrendidasRecibeUnMapaConTodosPuntosYUnCeroEnUnaEsquinaArribaALaIzquierdaDeberiaDevolverFalse(self):
        mapa = [
            ['0', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        resultado = pasarDeNivel.verificarSiHayLucesPrendidas(mapa)

        self.assertEqual(resultado,False)
