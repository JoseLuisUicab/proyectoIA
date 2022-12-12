import sys


class Paciente:
    def __int__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def ingresar_paciente(self, pacientes):
        pacientes.append(self)

    def consultar_paciente(self, pacientes):
        for paciente in pacientes:
            if paciente.nombre == self.nombre:
                return paciente
        return None

    def actualizar_paciente(self, pacientes, nuevo_nombre, nueva_edad, nuevo_genero):
        for paciente in pacientes:
            if paciente.nombre == self.nombre:
                paciente.nombre = nuevo_nombre
                paciente.edad = nueva_edad
                paciente.genero = nuevo_genero


class Cita:
    def __init__(self, fecha, hora, medico):
        self.fecha = fecha
        self.hora = hora
        self.medico = medico

    def programar_cita(self, citas, paciente):
        citas.append(self)

    def cancelar_cita(self, citas, paciente):
        for cita in citas:
            if cita.fecha == self.fecha and cita.hora == self.hora and cita.medico == self.medico:
                cita.remove(cita)


class Receta:
    def __init__(self, diagnostico, medicamentos):
        self.diagnostico = diagnostico
        self.medicamentos = medicamentos

    def crear_receta(self, recetas, paciente):
        recetas.append(self)

    def consultar_receta(self, recetas, paciente):
        for receta in recetas:
            if receta.diagnostico == self.diagnostico and receta.medicamentos == receta.medicamentos:
                return receta
        return None


pacientes = []
citas = []
recetas = []

while True:
    print(""" 
    .--------------------------------.
    |    proceso Medico A Realizar   |
    |--------------------------------|
    | 1. | Ingresar Paciente         |
    | 2. | Programar cita            |
    | 3. | Crear cita                |
    | 4. | Crear historia Clinica    |
    | 5. | MOstrar Pacientes         |
    | 6. | Mostrar citas             |
    | 7. | Mostrar Recetas           |
    | 8. | MOstrar historia clinica  |
    | 9. | Salir                     |
    .--------------------------------.""")
    print("""""")
    opcion = int(input("seleccionar una opcion"))
    print("""""")

    if opcion == 1:
        nombre = input("ingrese nombre")
        edad = input("ingrese edad")
        genero = input("ingrese genero (M/F)")
        p1 = Paciente(nombre, edad, genero)
        p1.ingresar_paciente(pacientes)
        print("""""")

    elif opcion == 2:

    elif opcion == 3:
    elif opcion == 4:
    elif opcion == 5:
    elif opcion == 6:
    elif opcion == 7:
    elif opcion == 8:
        print("Pacientes: ")
        for i,paciente in enumerate(pacientes):
            print(i+1,paciente.nombre)
        paciente_index=int(input("Seleccione paciente: "))
        p1 = pacientes[paciente_index-1]
        p1.
    else:
        print("""
        .-----------------------.
        |gracias !!!!!!!!!!!!!!!|
        .-----------------------|.""")
        sys.exit()