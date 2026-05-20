import streamlit as st

st.set_page_config(
    page_title="Proyecto 1 – Aplicación en Streamlit",
    page_icon="🖥️",
    layout="wide",
)

st.sidebar.title("Secciones")
st.title("PROYECTO 1 – APLICACIÓN EN STREAMLIT")
st.write("Elaborado por Jose Alex Mosquera Amaro")

pagina = st.sidebar.selectbox(
    "📂 Navegación",
    ["🏠 Home", "📊 Ejercicio 1", "🧮 Ejercicio 2", "⚙️ Ejercicio 3", "🗄️ Ejercicio 4"],
)
