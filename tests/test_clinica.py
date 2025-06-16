#Prueba de clinica

import unittest
from datetime import datetime
from clases.clinica import Clinica
from clases.paciente import Paciente
from clases.medico import Medico
from clases.especialidad import Especialidad
from clases.excepciones import *

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("12345678", "Juan Pérez", "15/03/1990")
        self.medico = Medico("Dr. López", "MP001")
        self.medico.agregar_especialidad(Especialidad("Cardiología", ["lunes", "miércoles"]))
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_agregar_paciente(self):
        self.assertIn("12345678", self.clinica.pacientes)

    def test_agregar_medico(self):
        self.assertIn("MP001", self.clinica.medicos)

    def test_agendar_turno_valido(self):
        fecha = datetime(2025, 12, 15, 10, 0)  # lunes
        self.clinica.agendar_turno("12345678", "MP001", fecha)
        self.assertEqual(len(self.clinica.turnos), 1)

    def test_turno_duplicado(self):
        fecha = datetime(2025, 12, 15, 10, 0)
        self.clinica.agendar_turno("12345678", "MP001", fecha)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("12345678", "MP001", fecha)

    def test_paciente_no_existente(self):
        fecha = datetime(2025, 12, 15, 10, 0)
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("00000000", "MP001", fecha)

    def test_medico_no_existente(self):
        fecha = datetime(2025, 12, 15, 10, 0)
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.agendar_turno("12345678", "MP999", fecha)

    def test_emitir_receta_valida(self):
        medicamentos = ["Paracetamol", "Ibuprofeno"]
        self.clinica.emitir_receta("12345678", "MP001", medicamentos)
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertEqual(len(historia.obtener_recetas()), 1)

    def test_emitir_receta_paciente_no_existente(self):
        medicamentos = ["Paracetamol"]
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("00000000", "MP001", medicamentos)

    def test_emitir_receta_medico_no_existente(self):
        medicamentos = ["Paracetamol"]
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.emitir_receta("12345678", "MP999", medicamentos)

    def test_historia_clinica_completa(self):
        fecha = datetime(2025, 12, 15, 10, 0)
        medicamentos = ["Paracetamol", "Ibuprofeno"]
        self.clinica.agendar_turno("12345678", "MP001", fecha)
        self.clinica.emitir_receta("12345678", "MP001", medicamentos)
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertEqual(len(historia.obtener_turnos()), 1)
        self.assertEqual(len(historia.obtener_recetas()), 1)

if __name__ == "__main__":
    unittest.main()