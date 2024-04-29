import unittest

from vocales_contador import vocales_contar

class TestContarVocales(unittest.TestCase):
    def test_sin_vocales(self):
        palabra = "tryhgf"
        resultado = vocales_contar(palabra)
        self.assertEqual(resultado, {})

    def test_con_vocal_o(self):
        palabra = "sol"
        resultado = vocales_contar(palabra)
        self.assertEqual(resultado, {"o": 1})
    
    def test_con_vocal_doble_o(self):
        palabra = "solo"
        resultado = vocales_contar(palabra)
        self.assertEqual(resultado, {"o": 2})
        
    def test_con_dos_vocales(self):
        palabra = "sola"
        resultado = vocales_contar(palabra)
        self.assertEqual(resultado, {"o": 1, "a": 1})

    def test_con_todas_las_vocales(self):
        palabra = "solamente quiero que gane Boca"
        resultado = vocales_contar(palabra)
        self.assertEqual(
            resultado,
            {"a": 3, "e": 5, "i": 1, "o": 3, "u": 2},
            )

    def test_con_vocales_en_mayuscula(self):
        palabra = "SOlAmente quIerO"
        resultado = vocales_contar(palabra)
        self.assertEqual(
            resultado,
            {"a": 1, "e": 3, "i": 1, "o": 2, "u": 1},
        )

    def test_con_vocales_en_oracion_larga(self):
        palabra = "Yo quisiera comer pochoclos"
        resultado = vocales_contar(palabra)
        self.assertEqual(
            resultado,
            {"a": 1, "e": 2, "i": 2, "o": 5, "u": 1},
        )
    
    def test_con_vocales_en_oracion_con_mayusculas_y_guiones(self):
        palabra = "Yo-Qui erO- coMeR-UN - ASaDo"
        resultado = vocales_contar(palabra)
        self.assertEqual(
            resultado,
            {"a": 2, "e": 2, "i": 1, "o": 4, "u": 2},
        )

if __name__ == '__main__':
    unittest.main()