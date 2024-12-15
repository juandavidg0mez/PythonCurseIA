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
password = 'juandavidgomez' 
host = 'localhost' 
port = '3306' 
database = 'NewData'
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')


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


# add_task('Test Casa Aura', 'Creacion de basses de datos y entornos virtuales desde la casa de mi hermana')

#Listar Tareas
# retorna una lista de tuplas
def list_task():
    if session.query(Task).count() == 0:
        return "Create A Task"
    else:
        task_list = session.query(Task).all()
        list_about_task= [(i.id, i.title_task, i.container_task) for i in task_list]
        return list_about_task
print(list_task())
# Funcion filtropor nombre 
def filter_By_name(name):
    farmat_name = name.title()
    Query = session.query(Task.title_task, Task.container_task).filter(
        Task.title_task == farmat_name
    ).all()
    for task in Query:
       print(f'--------------\nTitulo : {task[0]}\nContenido : {task[1]}\n--------------')

# Actualizar Tarea 
def update_task(task_id, new_title , new_content):
    task = session.query(Task).get(task_id)
    if task:
        # Actualizar los valores
        task.title_task = new_title
        task.container_task = new_content
        
        # Guardar los cambios
        session.commit()
        return "Updated Task"
    else:
        return "Task Not Exists"

#update_task('test 6', 'test 6', 'update_test 5 to 6')

#Elieminar Registros Tareas
def delete_task(task_id):
    task_to_delete = session.query(Task).get(task_id)
    if task_to_delete:
        session.delete(task_to_delete)
        session.commit()
    else:
        return "Task Can't be deleted"


#delete_task("test 6")
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
    
