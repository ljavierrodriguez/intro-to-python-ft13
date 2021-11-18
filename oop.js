// Programacion Orientada a Objetos (OOP)
// Herencia, Encapsulamiento, Polimorfismo y Abstracion

class Persona {
    nombre
    apellido
    genero
    direccion
    edad

    constructor(nombre, apellido, genero, direccion, edad){
        this.nombre = nombre;
        this.apellido = apellido;
        this.genero = genero;
        this.direccion = direccion;
        this.edad = edad;
    }

    comer = function () {

    }
    dormir = function () {
        return "Hora de Dormir";
    }
    correr = function () {

    }
    caminar = function () {

    }
}

let persona = new Persona("Luis", "Rodriguez", "Masculino", "Av Vitacura", 39);

class Estudiante extends Persona {
    constructor(nombre, apellido, genero, direccion, edad){
        super(nombre, apellido, genero, direccion, edad);
    }

    dormir = function(){
        return "Me voy a dormir a las 11";
    }
}

let estudiante = new Estudiante("Luis", "Rodriguez", "Masculino", "Av Vitacura", 39);

console.log(estudiante)