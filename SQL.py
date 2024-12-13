# los modelos son las tablas esta debe ser tomada del modulo para poder hacer una herencia y asi poder crear ORM
# o las tablas de nuestra base dedatos
from sqlalchemy.orm import declarative_base
#Aca vamos a trabajar con el objeto de tipo colum apra crear el tipode dato de cada atributo de la clase Taks
from sqlalchemy import Column, Integer, String,Text, Sequence, DateTime
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# import datetime

'''
from datetime import datetime es parte de la librería estándar de Python, no de SQLAlchemy. Esto significa que datetime ya viene incluido en cualquier instalación de Python y no necesitas instalar ningún paquete adicional para usarlo.

Por otro lado, SQLAlchemy también incluye un tipo llamado DateTime que se utiliza para definir columnas de tipo fecha y hora en los modelos de base de datos, pero no ofrece funcionalidad para manejar fechas y horas directamente (como formateo o manipulación de objetos de tiempo).
'''


# Reemplaza con tus datos de conexión 

#Coneccion Base De datos MYsql
username = 'root' 
password = 'juandavidgomez15' 
host = 'localhost' 
port = '3306' 
database = 'Alchemy'
engine = create_engine(f'mysql+mysqldb://{username}:{password}@{host}:{port}/{database}')


Base = declarative_base()

#Creacion de modelo(Tabla TAREA) 
class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer,Sequence('post_id_seq'), primary_key=True)
    title_task = Column(String(100), nullable=False)
    container_task= Column(Text, nullable=False)

    def __str__(self):
        return f"Task(title={self.title_task})"
# es un puente entre modelos y la base datos desde la seseiones podemos intereactuar con ellas(CRUD)
Session = sessionmaker(bind=engine)
session = Session()

def pass_String(world):
    return world.title()

# Creacion de Tarea
def add_task(title_t, container):
    format_title = title_t.title()
    format_container = container.title()
    # Crear una nueva instancia de Task con los valores de title y container
    task = Task(title_task=format_title, container_task=format_container)
    session.add(task)
    session.commit()
    return "Task Created!!"

#Listar Tareas
def list_taks():
    tasks =  session.query(Task).all()
    for task in tasks:
        print(task)

# Funcion filtropor nombre 
def filter_By_name(name):
    farmat_name = name.title()
    Query = session.query(Task.title_task, Task.container_task).filter(
        Task.title_task == farmat_name
    ).all()
    for task in Query:
       print(f'--------------\nTitulo : {task[0]}\nContenido : {task[1]}\n--------------')

# Actualizar Tarea 
def update_task(title, new_title , new_content):
    up_title = pass_String(title)
    task = session.query(Task).filter(Task.title_task == up_title).first()
    if task:
        # Actualizar los valores
        task.title_task = new_title
        task.container_task = new_content
        
        # Guardar los cambios
        session.commit()
        print(f"Task updated: {title} -> {new_title}, {new_content}")
    else:
        print(f"No task found with title: {title}")

#update_task('test 6', 'test 6', 'update_test 5 to 6')

#Elieminar Registros Tareas
def delete_task(name_task):
    task_to_delete = session.query(Task).filter(
        Task.title_task == name_task
    ).first()

    if task_to_delete:
        session.delete(task_to_delete)  # Eliminar el registro
        session.commit()  # Confirmar los cambios
        print(f"The Task with id: {task_to_delete.id} and Name: '{task_to_delete.title_task}' was Deleted")
    else:
        print(f"No task found with the name: {name_task}")

delete_task("test 6")
# Funcion filtro por Contenido / Opcional 
# consultas = session.query(Task.title_task , Task.container_task).all()
# print(consultas)
# print(f"Titulo de la Tarea : {consultas[0][0]}\nCuerpo: {consultas[0][1]}")
# print(add_task("test5","creacion de Test 5"))

# filter_By_name('test5')
# list_taks()

if __name__ == '__main__':
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
