#Prueba de historia clinica

import unittest
from datetime import datetime
from clases.paciente import Paciente
from clases.medico import Medico
from clases.turno import Turno
from clases.receta import Receta
from clases.historiaclinica import HistoriaClinica
from clases.excepciones import RecetaInvalidaException

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("12345678", "Sofía Ríos", "10/10/1990")
        self.medico = Medico("Dr. García", "M202")
        self.historia = HistoriaClinica(self.paciente)
        self.fecha1 = datetime(2025, 12, 15, 11, 0)
        self.fecha2 = datetime(2025, 12, 16, 12, 0)
        self.turno1 = Turno(self.paciente, self.medico, self.fecha1, "Clínica")
        self.turno2 = Turno(self.paciente, self.medico, self.fecha2, "Clínica")
        self.receta1 = Receta(self.paciente, self.medico, ["Paracetamol"])
        self.receta2 = Receta(self.paciente, self.medico, ["Ibuprofeno"])

    def test_agregar_turno(self):
        self.historia.agregar_turno(self.turno1)
        self.assertEqual(len(self.historia.obtener_turnos()), 1)

    def test_agregar_varios_turnos(self):
        self.historia.agregar_turno(self.turno1)
        self.historia.agregar_turno(self.turno2)
        turnos = self.historia.obtener_turnos()
        self.assertEqual(len(turnos), 2)
        self.assertIn(self.turno1, turnos)
        self.assertIn(self.turno2, turnos)

    def test_agregar_receta(self):
        self.historia.agregar_receta(self.receta1)
        self.assertEqual(len(self.historia.obtener_recetas()), 1)

    def test_agregar_varias_recetas(self):
        self.historia.agregar_receta(self.receta1)
        self.historia.agregar_receta(self.receta2)
        recetas = self.historia.obtener_recetas()
        self.assertEqual(len(recetas), 2)
        self.assertIn(self.receta1, recetas)
        self.assertIn(self.receta2, recetas)

    def test_str_historia(self):
        self.historia.agregar_turno(self.turno1)
        self.historia.agregar_receta(self.receta1)
        result = str(self.historia)
        self.assertIn("Sofía Ríos", result)
        self.assertIn("Turno", result)
        self.assertIn("Receta", result)
        self.assertIn("Paracetamol", result)

    def test_historia_sin_turnos_y_recetas(self):
        self.assertEqual(self.historia.obtener_turnos(), [])
        self.assertEqual(self.historia.obtener_recetas(), [])

if __name__ == "__main__":
    unittest.main()