import unittest

from polinomio import Polinomio


class TestPolinomio(unittest.TestCase):
    def test_deriv(self):
        """
        Test que verifica la derivada del polinomio
        """
        p = Polinomio([2, 3, 4], 2)
        self.assertEqual(p.obtener_deriv(), [3,8])

    def test_evaluar(self):
        """
        Test de evaluación del polinomio
        """
        p = Polinomio([2, 3, 4], 2)
        self.assertEqual(p.evaluar(2), 24)

    def test_evaluar_deriv(self):
        """
        Test que verifica la derivada del polinomio
        """
        p = Polinomio([2, 3, 4], 2)
        self.assertEqual(p.evaluar_deriv(1), 11)


    def test_str(self):
        """
        Test para la impresión de una instancia de Polinomio
        """
        p = Polinomio([2, 3, 4], 2)
        self.assertEqual(str(p), "2 + 3x + 4x^2")

if __name__ == '__main__':
    unittest.main()