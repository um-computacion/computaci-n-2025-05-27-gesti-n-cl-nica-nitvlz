#Prueba de medicos

import unittest
from clases.medico import Medico
from clases.especialidad import Especialidad

class TestMedico(unittest.TestCase):
    def setUp(self):
        self.medico = Medico("Dr. Carla Gómez", "M001")
        self.especialidad1 = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.especialidad2 = Especialidad("Clínica", ["martes", "jueves"])

    def test_agregar_especialidad(self):
        self.medico.agregar_especialidad(self.especialidad1)
        self.assertEqual(self.medico.obtener_especialidad_para_dia("lunes"), "Pediatría")

    def test_no_especialidad_dia(self):
        self.medico.agregar_especialidad(self.especialidad1)
        self.assertIsNone(self.medico.obtener_especialidad_para_dia("viernes"))

    def test_str_medico(self):
        self.medico.agregar_especialidad(self.especialidad1)
        result = str(self.medico)
        self.assertIn("Pediatría", result)
        self.assertIn("lunes", result)

    def test_multiples_especialidades(self):
        self.medico.agregar_especialidad(self.especialidad1)
        self.medico.agregar_especialidad(self.especialidad2)
        self.assertEqual(self.medico.obtener_especialidad_para_dia("martes"), "Clínica")
        self.assertEqual(self.medico.obtener_especialidad_para_dia("miércoles"), "Pediatría")

    def test_no_duplicar_especialidad(self):
        self.medico.agregar_especialidad(self.especialidad1)
        self.medico.agregar_especialidad(self.especialidad1)  # Intento duplicar
        result = str(self.medico)
        self.assertEqual(result.count("Pediatría"), 1)

    def test_obtener_matricula(self):
        self.assertEqual(self.medico.obtener_matricula(), "M001")

if __name__ == "__main__":
    unittest.main()