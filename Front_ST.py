import streamlit as st
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

with col2: 
    st.header("Columna 2") 
    st.write("Este es un texto en la columna 2") 
    st.button("Botón en Columna 2") 