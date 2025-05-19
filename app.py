import streamlit as st

st.title("Hola Streamlit")

nombre = st.text_input("¿Cuál es tu nombre?")

if st.button("Saludar"):
    st.write(f"¡Hola, {nombre}!")
    