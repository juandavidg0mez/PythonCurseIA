# los modelos son las tablas esta debe ser tomada del modulo para poder hacer una herencia y asi poder crear ORM
# o las tablas de nuestra base dedatos
from sqlalchemy.ext.declarative import declarative_base
#Aca vamos a trabajar con el objeto de tipo colum apra crear el tipode dato de cada atributo de la clase Taks
from sqlalchemy import Column, Integer, String,Text, Sequence, DateTime
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

'''
from datetime import datetime es parte de la librería estándar de Python, no de SQLAlchemy. Esto significa que datetime ya viene incluido en cualquier instalación de Python y no necesitas instalar ningún paquete adicional para usarlo.

Por otro lado, SQLAlchemy también incluye un tipo llamado DateTime que se utiliza para definir columnas de tipo fecha y hora en los modelos de base de datos, pero no ofrece funcionalidad para manejar fechas y horas directamente (como formateo o manipulación de objetos de tiempo).
'''


# Reemplaza con tus datos de conexión 


username = 'root' 
password = 'juandavidgomez15' 
host = 'localhost' 
port = '3306' 
database = 'Alchemy'
engine = create_engine(f'mysql+mysqldb://{username}:{password}@{host}:{port}/{database}')


Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer,Sequence('post_id_seq'), primary_key=True)
    title_taks = Column(String(100), nullable=False)
    container_taks = Column(Text, nullable=False)
    created_at = Column(DateTime(), default=datetime.now)

    def __str__(self):
        return f"Task(title={self.title_taks}, created_at={self.created_at})"
# es un puente entre modelos y la base datos desde la seseiones podemos intereactuar con ellas(CRUD)
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
