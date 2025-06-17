#Prueba de turnos

import unittest
from datetime import datetime
from clases.paciente import Paciente
from clases.medico import Medico
from clases.especialidad import Especialidad
from clases.turno import Turno

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("12345678", "Ana Torres", "01/01/1980")
        self.medico = Medico("Dr. Test", "M123")
        self.medico.agregar_especialidad(Especialidad("Clínica", ["lunes"]))
        self.fecha = datetime(2025, 12, 15, 9, 0)  # lunes
        self.turno = Turno(self.paciente, self.medico, self.fecha, "Clínica")

    def test_obtener_fecha(self):
        self.assertEqual(self.turno.obtener_fecha_hora(), self.fecha)

    def test_obtener_medico(self):
        self.assertEqual(self.turno.obtener_medico().obtener_matricula(), "M123")

    def test_str_turno(self):
        result = str(self.turno)
        self.assertIn("Ana Torres", result)
        self.assertIn("Dr. Test", result)
        self.assertIn("Clínica", result)

if __name__ == "__main__":
    unittest.main()