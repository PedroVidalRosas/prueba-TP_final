import unittest
import puntosPorCadaNivel

class puntosPorCadaNivelTest(unittest.TestCase):

    def testPuntosPorCadaNivelRecibeUnaListaVaciaYPuntosQuinientosDebeDevolverUnaListaConQuinnientos(self):

        puntos = 500
        puntosNiveles = []

        resultado = puntosPorCadaNivel.puntosPorCadaNivel(puntosNiveles,puntos)

        self.assertEqual(resultado,[500])

    def testPuntosPorCadaNivelRecibeUnaListaConQuinientosYPuntosIgualSetecientosCicuentaDeberiaDevolverUnaListaConQuinientosYDocientosCicuenta(self):

        puntos = 750
        puntosNiveles = [500]

        resultado = puntosPorCadaNivel.puntosPorCadaNivel(puntosNiveles,puntos)

        self.assertEqual(resultado,[500,250])

    def testPuntosPorCadaNivelRecibeUnaListaYpuntosDeberiaDevolverUnaListaAgregandoLaSumaDeLosDatosYRestandoloConLosPuntos(self):

        puntos = 950
        puntosNivel = [500,250]

        resultado = puntosPorCadaNivel.puntosPorCadaNivel(puntosNivel,puntos)

        self.assertEqual(resultado,[500,250,200])


