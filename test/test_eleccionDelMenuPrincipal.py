import unittest
import eleccionDelMenuPrincipal

class eleccionDelMenuPrincipalTest(unittest.TestCase):

    def testeleccionDelMenuPrincipalRecibeUnoDeberiaDevoolverUno(self):

        eleccion = "1"

        resultado = eleccionDelMenuPrincipal.eleccionDelMenuPrincipal(eleccion)

        self.assertEqual(resultado,1)

    def testseleccionDelMenuPrincipalRecibeDosPalabrasDeberiaDevolverCuatro(self):

        eleccion = "No valido"

        resultado = eleccionDelMenuPrincipal.eleccionDelMenuPrincipal(eleccion)

        self.assertEqual(resultado,10)

    def testseleccionDelMenuPrincipalRecibeVariosEspaciosDeberiaDevolverDiez(self):

        eleccion = "10"

        resultado = eleccionDelMenuPrincipal.eleccionDelMenuPrincipal(eleccion)

        self.assertEqual(resultado,10)

    def testseleccionDelMenuPrincipalRecibeUnaPalabraDeberiaDevolverDiez(self):

        eleccion = "novalido"

        resultado = eleccionDelMenuPrincipal.eleccionDelMenuPrincipal(eleccion)

        self.assertEqual(resultado,10)

    def testeleccionDelMenuPrincipalRecibeMenosUnoDeberiaDevolverDiez(self):

        eleccion = "-1"

        resultado = eleccionDelMenuPrincipal.eleccionDelMenuPrincipal(eleccion)

        self.assertEqual(resultado,10)