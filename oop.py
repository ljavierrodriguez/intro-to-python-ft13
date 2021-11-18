# Programacion Orientada a Objeto
# Herencia, Encapsulamiento, Polimorfismo y Abstracion

class Persona: 
    nombre = ""
    apellido = ""
    genero = ""
    direccion = ""
    edad = ""

    def __init__(self, nombre, apellido, genero, direccion, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.direccion = direccion
        self.edad = edad

    def comer():
        pass

    def comer():
        pass

    def comer():
        pass

    def comer():
        pass
    
persona = Persona("Luis", "Rodriguez", "Masculino", "Av Vitacura", 39)

print(persona.nombre)

class Estudiante(Persona):
    def __init__(self, nombre, apellido, genero, direccion, edad):
        super().__init__(nombre, apellido, genero, direccion, edad)

    def comer(self):
        return "Hora de comer"

    def __repr__(self):
        return "<Estudiante %s %s>" % (self.nombre, self.apellido)



estudiante = Estudiante("Luis", "Rodriguez", "Masculino", "Av Vitacura", 39)

print(estudiante.__str__)
