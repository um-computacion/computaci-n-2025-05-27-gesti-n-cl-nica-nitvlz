#Prueba de paciente

import unittest
from clases.paciente import Paciente

class TestPaciente(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("12345678", "Juan Pérez", "15/03/1990")

    def test_creacion_paciente(self):
        self.assertEqual(self.paciente.obtener_dni(), "12345678")
        self.assertIn("Juan Pérez", str(self.paciente))
        self.assertIn("15/03/1990", str(self.paciente))

    def test_dni_tipo_str(self):
        self.assertIsInstance(self.paciente.obtener_dni(), str)

    def test_str_formato_correcto(self):
        resultado = str(self.paciente)
        self.assertRegex(resultado, r"Juan Pérez, 12345678, 15/03/1990")

    def test_dni_unico_simulado(self):
        otro_paciente = Paciente("87654321", "Ana Gómez", "01/01/2000")
        self.assertNotEqual(self.paciente.obtener_dni(), otro_paciente.obtener_dni())

    def test_nombre_en_str(self):
        self.assertIn("Juan Pérez", str(self.paciente))

    def test_fecha_nacimiento_en_str(self):
        self.assertIn("15/03/1990", str(self.paciente))

    def test_distintos_pacientes_distinto_str(self):
        otro_paciente = Paciente("87654321", "Ana Gómez", "01/01/2000")
        self.assertNotEqual(str(self.paciente), str(otro_paciente))

if __name__ == "__main__":
    unittest.main()