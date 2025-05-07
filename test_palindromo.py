# Importamos el fichero anterior y la librería

from charfun import esPalindromo
import unittest

class Test_palindromo(unittest.TestCase):

    #Creamos la función que comprueba el resultado de esPalindromo
    
    def test_palindroma(self):
        self.assertTrue(esPalindromo("Anita lava la tina"))

    def test_no_palindroma(self):
        self.assertFalse(esPalindromo("Esta frase no es un palíndromo"))

    def test_espa_simbo(self):
        self.assertTrue(esPalindromo("Anita, lava la tina"))
    
    def test_frase_con_mayus_y_minus(self):
        self.assertTrue(esPalindromo("Anita lava la Tina"))
    
    def test_numeros(self):
        self.assertFalse(esPalindromo("Anita lava la tina 2"))
        


# Se ejecutan todas las funciones
if __name__ == '__main__':
    unittest.main()