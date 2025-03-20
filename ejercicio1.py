class Persona():
    tipo= "Mamifero"
    def __init__(self ):
        self.__nombre =""
        self.__cedula =0
        self.__genero = ""

    # Setters
    def asignarNombre(self,h):
        self.__nombre = h
    def asignarCedula(self,h):
        self.__cedula = h
    def asignarGenero(self,h):
        self.__genero = h

    # Getters 
    def verNombre(self): 
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    
    # Deleters
    def borrarNombre(self):
        del self.__nombre
    def borrarCedula(self):
        del self.__cedula
    def borrarGenero(self):
        del self.__genero

class Paciente(Persona):
    pacientes = []
    
    def __init__(self):
        super().__init__()
        self.__servicio = ""
        Paciente.pacientes.append(self)
    
    def asignarServicio(self, servicio):
        self.__servicio = servicio
    def verServicio(self):
        return self.__servicio
    
    def mostrar_datos(self):
        print(f"Paciente: Nombre: {self.verNombre()}, Cédula: {self.verCedula()}, Género: {self.verGenero()}, Servicio: {self.verServicio()}")

class Empleado_Hospital(Persona):
    def __init__(self):
        super().__init__()
        self.__turno = ''

    def asignarTurno(self, turno):
        self.__turno = turno
    def verturno(self):
        return self.__turno

class Enfermera(Empleado_Hospital):
    enfermeras = []
    
    def __init__(self):
        super().__init__()
        self.__rango = ''
        Enfermera.enfermeras.append(self)
    
    def asignarRango(self, rango):
        self.__rango = rango
    def verRango(self):
        return self.__rango
    
    def mostrar_datos(self):
        print(f"Enfermera: Nombre: {self.verNombre()}, Cédula: {self.verCedula()}, Género: {self.verGenero()}, Turno: {self.verturno()}, Rango: {self.verRango()}")

class Medico(Empleado_Hospital):
    medicos = []
    
    def __init__(self):
        super().__init__()
        self.__especialidad = ''
        Medico.medicos.append(self)
    
    def asignarEspecialidad(self, especialidad):
        self.__especialidad = especialidad
    def verEspecialidad(self):
        return self.__especialidad
    
    def mostrar_datos(self):
        print(f"Médico: Nombre: {self.verNombre()}, Cédula: {self.verCedula()}, Género: {self.verGenero()}, Turno: {self.verturno()}, Especialidad: {self.verEspecialidad()}")

class SistemaHospital:
    def mostrar_pacientes(self):
        if not Paciente.pacientes:
            print("No hay pacientes registrados")
        else:
            for paciente in Paciente.pacientes:
                paciente.mostrar_datos()
    
    def mostrar_enfermeras(self):
        if not Enfermera.enfermeras:
            print("No hay enfermeras registradas")
        else:
            for enfermera in Enfermera.enfermeras:
                enfermera.mostrar_datos()
    
    def mostrar_medicos(self):
        if not Medico.medicos:
            print("No hay medicos registrados")
        else:
            for medico in Medico.medicos:
                medico.mostrar_datos()
    
    def eliminar_paciente(self):
        cedula = input("Ingrese la cedula del paciente a eliminar: ")
        for paciente in Paciente.pacientes:
            if paciente.verCedula() == cedula:
                Paciente.pacientes.remove(paciente)
                print("Paciente eliminado correctamente\n")
                return
        print("No se encontró el paciente con esa cedula\n")
    
    def eliminar_enfermera(self):
        cedula = input("Ingrese la cedula de la enfermera a eliminar: ")
        for enfermera in Enfermera.enfermeras:
            if enfermera.verCedula() == cedula:
                Enfermera.enfermeras.remove(enfermera)
                print("Enfermera eliminada correctamente\n")
                return
        print("No se encontró la enfermera con esa cedula\n")
    
    def eliminar_medico(self):
        cedula = input("Ingrese la cédula del médico a eliminar: ")
        for medico in Medico.medicos:
            if medico.verCedula() == cedula:
                Medico.medicos.remove(medico)
                print("Médico eliminado correctamente\n")
                return
        print("No se encontró el médico con esa cédula.\n")
    
    def menu(self):
        while True:
            print("\n Bienvenido al Sistema de Hospital del Sisben")
            print("1. Agregar Paciente")
            print("2. Agregar Enfermera")
            print("3. Agregar Médico")
            print("4. Mostrar Pacientes")
            print("5. Mostrar Enfermeras")
            print("6. Mostrar Médicos")
            print("7. Eliminar Paciente")
            print("8. Eliminar Enfermera")
            print("9. Eliminar Médico")
            print("10. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                paciente = Paciente()
                paciente.asignarNombre(input("Ingrese nombre del paciente: "))
                paciente.asignarCedula(input("Ingrese cedula del paciente: "))
                paciente.asignarGenero(input("Ingrese genero del paciente: "))
                paciente.asignarServicio(input("Ingrese servicio del paciente: "))
                paciente.mostrar_datos()
            elif opcion == "2":
                enfermera = Enfermera()
                enfermera.asignarNombre(input("Ingrese nombre de la enfermera: "))
                enfermera.asignarCedula(input("Ingrese cedula de la enfermera: "))
                enfermera.asignarGenero(input("Ingrese genero de la enfermera: "))
                enfermera.asignarTurno(input("Ingrese turno de la enfermera: "))
                enfermera.asignarRango(input("Ingrese rango de la enfermera: "))
                enfermera.mostrar_datos()
            elif opcion == "3":
                medico = Medico()
                medico.asignarNombre(input("Ingrese nombre del médico: "))
                medico.asignarCedula(input("Ingrese cedula del médico: "))
                medico.asignarGenero(input("Ingrese genero del médico: "))
                medico.asignarTurno(input("Ingrese turno del médico: "))
                medico.asignarEspecialidad(input("Ingrese especialidad del médico: "))
                medico.mostrar_datos()
            elif opcion == "4":
                self.mostrar_pacientes()
            elif opcion == "5":
                self.mostrar_enfermeras()
            elif opcion == "6":
                self.mostrar_medicos()
            elif opcion == "7":
                self.eliminar_paciente()
            elif opcion == "8":
                self.eliminar_enfermera()
            elif opcion == "9":
                self.eliminar_medico()
            elif opcion == "10":
                print("Saliendo del sistema")
                break
            else:
                print("Opción inválida, intente de nuevo.")

sistema = SistemaHospital()
sistema.menu()

