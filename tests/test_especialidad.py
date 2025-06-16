#Prueba de especialidades

import unittest
from clases.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    def setUp(self):
        self.especialidad = Especialidad("Cardiología", ["lunes", "miércoles", "viernes"])

    def test_obtener_especialidad(self):
        self.assertEqual(self.especialidad.obtener_especialidad(), "Cardiología")

    def test_verificar_dia_true(self):
        self.assertTrue(self.especialidad.verificar_dia("lunes"))
        self.assertTrue(self.especialidad.verificar_dia("Miércoles"))  # con mayúscula

    def test_verificar_dia_false(self):
        self.assertFalse(self.especialidad.verificar_dia("domingo"))

    def test_dias_normalizados(self):
        # Asegura que todos los días se guarden en minúscula
        self.assertIn("viernes", str(self.especialidad))

    def test_str_especialidad_con_dias(self):
        resultado = str(self.especialidad)
        self.assertIn("Cardiología", resultado)
        self.assertIn("lunes", resultado)
        self.assertIn("miércoles", resultado)

if __name__ == "__main__":
    unittest.main()