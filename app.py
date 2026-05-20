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

if pagina == "🏠 Home":
    st.title("🖥️ Proyecto 1 – Fundamentos de Programación en Python")
    st.subheader("Especialización en Python for Analytics · Módulo 1 – Python Fundamentals")
    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 👤 Información del estudiante")
        st.write("**Nombre:** Tu Nombre Completo")
        st.write("**Módulo:** Módulo 1 – Python Fundamentals")
        st.write("**Curso:** Especialización en Python for Analytics")
        st.write("**Año:** 2025")
        st.markdown("---")

        st.markdown("### 📋 Descripción del proyecto")
        st.markdown(
            """
            Esta aplicación interactiva integra los conceptos fundamentales del Módulo 1:
            - **Ejercicio 1:** Flujo de caja con listas y `st.session_state`
            - **Ejercicio 2:** Registro de equipos TI con arrays NumPy y DataFrames
            - **Ejercicio 3:** Calculadoras de métricas TI usando funciones de librería externa
            - **Ejercicio 4:** Gestión CRUD de servidores con la clase `Servidor`
            """
        )

        st.markdown("### 🛠️ Tecnologías utilizadas")
        tech = {
            "Tecnología": ["Python 3.x", "Streamlit", "NumPy", "Pandas"],
            "Uso": ["Lenguaje base", "Interfaz interactiva", "Arrays numéricos", "DataFrames"],
        }
        st.dataframe(pd.DataFrame(tech), use_container_width=True, hide_index=True)

    with col2:
        st.markdown("### 🐍 Python for Analytics")
        st.info("Proyecto 1 – Aplicación en Streamlit\n\nMódulo 1: Python Fundamentals")
        st.markdown("**Instructor:** MSc. Carlos Carrillo Villavicencio")
