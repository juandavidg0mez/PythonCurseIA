import streamlit as st
from crud_Funtions import add_task, list_task, delete_task
# unsafe_allow_html=True Textos Segruos de fuentes deotras URLS

st.markdown(
    """
    <style>
        .titulo-principal{
            color:#10403B;
            text-align: center;
        }
    </style>

    """
    ,
    unsafe_allow_html=True
)

st.markdown("<h1 class='titulo-principal'>Welcome To Task Manager Intelligent</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([2,1])
with col1: 
    st.header("Do you want to Create a New Task?") 
    title = st.text_input("Taks Title") 
    container = st.text_area("Task Content")
    # Esto es un evento para el boton de crear Tarea
    if st.button("Create task"): 
        result = add_task(title, container) 
        st.success(result)

with col2:
    data = list_task()
    if data == "Create A Task":
        st.header("Create a New Task") 
    else:
        for i in data:
            if len(i) < 3:
                st.error(f"Datos incompletos para la tarea: {i}")
                continue  # Pasa al siguiente ítem si los datos no son válidos
            st.subheader(i[1])
            st.text(i[2])
            if st.button("Delete Task", key=f"delete_{i[0]}"):
                delete_task(i[0])
                st.success(f"task deleted {i[0]}")