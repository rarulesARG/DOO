class Paciente:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def __str__(self):
        return f"{self.nombre} : {self.dni}"
    
class Turno:
    def __init__(self, paciente, fecha, hora):
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora

class Agenda:
    def __init__(self):
        self.turnos = []

    def agregar_turno(self, turno):
        for t in self.turnos:
            if t.fecha == turno.fecha and t.hora == turno.hora:
                print("El turno ya está ocupado.")
                return False
        self.turnos.append(turno)
        print("Turno agregado con éxito.")
        return True
    def listar_turnos(self):
        for turno in self.turnos:
            print(f"Paciente: {turno.paciente}, Fecha: {turno.fecha}, Hora: {turno.hora}")  

paciente1 = Paciente("Juan", 12345678)
paciente2 = Paciente("María", 87654321)
paciente3 = Paciente("Pedro", 56781234)

print(paciente1)
print(paciente2)  
turno1 = Turno(paciente1, "2023-05-01", "10:00")
print(turno1.paciente.nombre, turno1.fecha, turno1.hora)
agrega_turno = Agenda()
agrega_turno.agregar_turno(turno1)
lista_turnos = Agenda()
lista_turnos.listar_turnos
