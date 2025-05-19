# ¿De qué trata esta app?

Esta aplicación es un ejemplo básico desarrollado con [Streamlit](https://streamlit.io/), una herramienta de código abierto para crear aplicaciones web interactivas en Python de forma sencilla.

## Funcionalidad principal
- Permite al usuario ingresar su nombre en un campo de texto (`st.text_input`)
- Al presionar el botón "Saludar" (`st.button`), la app muestra un saludo personalizado en pantalla (`st.write`)
- Interfaz reactiva que actualiza el contenido instantáneamente

## Componentes utilizados
```python
# Componentes principales de Streamlit
st.title()    # Para el título principal
st.write()    # Para mostrar texto
st.text_input()  # Para entrada de texto
st.button()   # Para el botón de acción
```

## Personalización
Puedes personalizar la aplicación de varias formas:
1. **Cambiar el estilo del saludo:**
   ```python
   st.markdown(f"### ¡Hola, {nombre}! 👋")
   ```

2. **Agregar más elementos:**
   ```python
   st.selectbox("Elige un idioma:", ["Español", "Inglés", "Francés"])
   ```

3. **Personalizar colores:**
   ```python
   st.markdown("""
   <style>
   .stButton>button {
       background-color: #4CAF50;
       color: white;
   }
   </style>
   """, unsafe_allow_html=True)
   ```

## Propósito educativo
El objetivo de esta app es servir como ejemplo introductorio para:
- Aprender los conceptos básicos de Streamlit
- Entender la estructura de una aplicación web simple
- Practicar la creación de interfaces interactivas
- Explorar las posibilidades de personalización



## Próximos pasos sugeridos
1. Agregar más campos de entrada
2. Implementar diferentes tipos de saludos
3. Añadir elementos visuales (gráficos, imágenes)
4. Incorporar temas y estilos personalizados
5. Integrar con bases de datos

## Recursos adicionales
- [Guía de componentes de Streamlit](https://docs.streamlit.io/library/api-reference)
- [Ejemplos de personalización](https://docs.streamlit.io/library/api-reference/theming)
- [Mejores prácticas](https://docs.streamlit.io/library/get-started/main-concepts)

