import streamlit as st
from CRUD_Funtions import add_task, list_task, delete_task,update_task
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
                col1, col2,col3 = st.columns(3)
                with col1:
                    if st.button("Delete Task", key=f"delete_{i[0]}"):
                        delete_task(i[0])
                        st.success(f"task deleted {i[0]}")
                with col2:
                    if st.button("Check", key=f"archive_{i[0]}"):
                        st.success("Boton precionado")
                with col3:
                     if st.button("Edit", key=f"edit_{i[0]}"):
                    # Guardar el ID en la sesión
                        st.session_state["selected_task_id"] = i[0]
                        st.session_state["selected_task_title"] = i[1]
                        st.session_state["selected_task_content"] = i[2]
                        st.success(f"Editing Task {i[0]}")

                if "selected_task_id" in st.session_state and st.session_state["selected_task_id"] == i[0]:
                        st.text_input("Enter New Title:", value=st.session_state["selected_task_title"], key=f"new_title_{i[1]}")
                        st.text_area("Enter New Content:", value=st.session_state["selected_task_content"], key=f"new_content_{i[2]}")
                        if st.button("Update Task", key=f"update_{i[0]}"):
                            new_title = st.session_state[f"new_title_{i[1]}"]
                            new_content = st.session_state[f"new_content_{i[2]}"]
                            if new_title and new_content:
                                result = update_task(i[0], new_title, new_content)
                                st.success(result)
                            else:
                                st.error("Please fill all fields")           
                                    
                                