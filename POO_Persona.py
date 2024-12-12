import tkinter as tk
#importar modulos restatntes
#Esto es como en JAVA que exportabamos difrentes cosas para que
#  funcionadarn las cosas modulos y eso con BUttons

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def decirDatos(self):
        print(f"hola mis datos son {self.nombre} {self.apellido} y mi edad es {self.edad}")


persona = Persona("monda", "test", 22)
persona.decirDatos()