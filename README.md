# Tanks Manager
Este proyecto gestiona tareas y recursos asociados. La aplicación permite a los usuarios visualizar y gestionar los datos relacionados con tareas, utilizando Streamlit para la interfaz de usuario y SQLAlchemy para la gestión de la base de datos.

# Requisitos previos
- Python 3.7+ instalado en tu sistema.
- pip para la instalación de dependencias.
- Mysql o algun gestor de bases de datos
(Recuerda que esto fue desarrollado con Mysql)

# Instalación

## 1. Clona el repositorio
Clona el repositorio en tu máquina local:

```python
git clone https://github.com/tu_usuario/tanks-manager.git
cd tanks-manager
```

## 2. Crea un entorno virtual (opcional, pero recomendado)

Es recomendable crear un entorno virtual para manejar las dependencias del proyecto:
```python
python -m venv venv
```
Activa el entorno virtual:

En Windows:
```python
    venv\Scripts\activate
```
En macOS/Linux:

```python
    source venv/bin/activate
```
## 3. Instala las dependencias
Instala SQLAlchemy, Streamlit y otras dependencias necesarias:
```python
pip install sqlalchemy streamlit pymysql 
```
## 4. Crear la base de datos

Crea una base de datos en tu gestor de bases de datos y edita el Arichivo CRUD_Funtions.py
```python
username = 'root' 
password = 'tu_Pass' 
host = 'localhost' 
port = '3306' 
database = 'Tu_base_de_datos'
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')
```

Ejecuta el Scripts
```python
python CRUD_Funtions.py
```
## 5. Ejecuta la aplicación Streamlit
Una vez que la base de datos esté configurada, puedes iniciar la aplicación Streamlit para visualizar y gestionar los datos.
```python
streamlit run Front_ST.py
```
Se abrira un pop-up en tu navegador
