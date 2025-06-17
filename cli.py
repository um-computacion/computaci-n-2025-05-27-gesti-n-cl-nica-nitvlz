#Consola del sistema

from datetime import datetime
from clases.clinica import Clinica
from clases.paciente import Paciente
from clases.medico import Medico
from clases.especialidad import Especialidad
from clases.excepciones import PacienteNoEncontradoException
from clases.excepciones import MedicoNoDisponibleException
from clases.excepciones import TurnoOcupadoException
from clases.excepciones import RecetaInvalidaException


class CLI:
    def __init__(self):
        self.clinica = Clinica()

    def mostrar_menu(self):
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar paciente")
        print("2. Agregar médico")
        print("3. Agendar turno")
        print("4. Emitir receta")
        print("5. Ver historia clínica")
        print("6. Ver todos los turnos")
        print("7. Ver todos los pacientes")
        print("8. Ver todos los médicos")
        print("9. Salir")

    def agregar_paciente(self):
        dni = input("DNI: ")
        nombre = input("Nombre completo: ")
        fecha = input("Fecha de nacimiento (dd/mm/aaaa): ")
        paciente = Paciente(dni, nombre, fecha)
        self.clinica.agregar_paciente(paciente)
        print("Paciente agregado correctamente.")

    def agregar_medico(self):
        nombre = input("Nombre del médico: ")
        matricula = input("Matrícula: ")
        medico = Medico(nombre, matricula)

        while True:
            tipo = input("Especialidad (ej: Clínica): ")
            dias = input("Días de atención (separados por coma): ").split(',')
            dias_limpios = [d.strip() for d in dias]
            especialidad = Especialidad(tipo, dias_limpios)
            medico.agregar_especialidad(especialidad)

            otro = input("¿Agregar otra especialidad? (s/n): ").lower()
            if otro != 's':
                break

        self.clinica.agregar_medico(medico)
        print("Médico agregado correctamente.")

    def agendar_turno(self):
        try:
            dni = input("DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            fecha_str = input("Fecha y hora del turno (dd/mm/aaaa HH:MM): ")
            print(f"Fecha ingresada: {fecha_str}")
            fecha_hora = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
            self.clinica.agendar_turno(dni, matricula, fecha_hora)
            print("Turno agendado exitosamente.")
        except (PacienteNoEncontradoException, MedicoNoDisponibleException, TurnoOcupadoException, ValueError) as e:
            print(f"Error: {e}")

    def emitir_receta(self):
        try:
            dni = input("DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            medicamentos = input("Medicamentos (separados por coma): ").split(',')
            meds = [m.strip() for m in medicamentos]
            self.clinica.emitir_receta(dni, matricula, meds)
            print("Receta emitida exitosamente.")
        except (PacienteNoEncontradoException, MedicoNoDisponibleException, RecetaInvalidaException) as e:
            print(f"Error: {e}")

    def ver_historia_clinica(self):
        try:
            dni = input("DNI del paciente: ")
            historia = self.clinica.obtener_historia_clinica(dni)
            print(historia)
        except PacienteNoEncontradoException as e:
            print(f"Error: {e}")

    def ver_todos_los_turnos(self):
        turnos = self.clinica.turnos
        if not turnos:
            print("No hay turnos registrados.")
        for turno in turnos:
            print(turno)

    def ver_todos_los_pacientes(self):
        pacientes = self.clinica.pacientes
        if not pacientes:
            print("No hay pacientes registrados.")
        for p in pacientes.values():
            print(p)

    def ver_todos_los_medicos(self):
        medicos = self.clinica.medicos
        if not medicos:
            print("No hay médicos registrados.")
        for m in medicos.values():
            print(m)

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("\nSeleccione una opción: ")
            if opcion == '1':
                self.agregar_paciente()
            elif opcion == '2':
                self.agregar_medico()
            elif opcion == '3':
                self.agendar_turno()
            elif opcion == '4':
                self.emitir_receta()
            elif opcion == '5':
                self.ver_historia_clinica()
            elif opcion == '6':
                self.ver_todos_los_turnos()
            elif opcion == '7':
                self.ver_todos_los_pacientes()
            elif opcion == '8':
                self.ver_todos_los_medicos()
            elif opcion == '9':
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    cli = CLI()
    cli.ejecutar()