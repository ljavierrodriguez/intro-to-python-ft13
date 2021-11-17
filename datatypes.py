"""
Comentario de multiples lineas

String, Number, Boolean, None, Dictionary

Array: 
    Listas, Tuples, Sets


"""

nombre = "Luis"

numero = 34
numero2 = 34.5
numero3 = -10

bool1 = True
bool2 = False

edad = None

persona = dict() # persona = dict()
persona["nombre"] = "Luis"
persona["apellido"] = "Rodriguez" 

persona = {
    nombre: "Luis",
    apellido: "Rodriguez"
}

persona["nombre"]

notas = [12, 28, 32, 12, 30]
notas = list(12, 28, 32, 12, 30)

status = ("active", "inactive", "canceled", "suspended")
status = tuple("active", "inactive", "canceled", "suspended")

mySet = {"active", "inactive", "canceled", "suspended"}