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
        .streamlit-expanderHeader { 
            background-color: #ADD8E6; 
            padding: 10px; 
            border-radius: 5px; 
        } 
        .streamlit-expanderContent { 
            background-color: #F0F8FF; 
            padding: 10px; 
            border-radius: 5px; 
        }
    </style>

    """
    ,
    unsafe_allow_html=True
)

st.markdown("<h1 class='titulo-principal'>Welcome To Task Manager Intelligent</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([2,3])
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
            with st.expander(i[1]):
                st.text(i[2])
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Delete Task", key=f"delete_{i[0]}"):
                        delete_task(i[0])
                        st.success(f"task deleted {i[0]}")
                with col2:
                    if st.button("Check", key=f"archive_{i[0]}"):
                        st.success("Boton precionado")
                    # with st.expander("Update Task"):
                    #     task_id = i[0]
                    #     new_title = st.text_input("Enter New Title:")
                    #     new_content = st.text_area("Enter New Content:")
                    #     if st.button("Enviar", key=f"send_{task_id}"): 
                    #         if task_id and new_title and new_content:  # Verificar que los campos no están vacíos
                    #             result = update_task(task_id, new_title, new_content)
                    #             st.success(result)  # Mostrar mensaje de éxito o error
                    #         else:
                    #             st.error("Please fill all fields")              
                                            
                    