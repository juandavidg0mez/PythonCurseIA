#creacion de las entidades

class Taks:
    def __init__(self, task_name, task_content):
        self.taskName = task_name
        self.taskContent = task_content
    
    def mostrar(self):
        return(f"Nombre tarea :{self.taskName}\nContenido : {self.taskContent}")

CreacionTareaNueva = Taks("Test1", "Creacion de clase Taks")
print(CreacionTareaNueva.mostrar())

        