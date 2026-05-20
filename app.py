import streamlit as st
import pandas as pd
import numpy as bp

st.set_page_config(
    page_title="Proyecto 1 – Aplicación en Streamlit",
    page_icon="🖥️",
    layout="wide",
)

# st.sidebar.title("Secciones")
# st.title("PROYECTO 1 – APLICACIÓN EN STREAMLIT")
# st.write("Elaborado por Jose Alex Mosquera Amaro")

pagina = st.sidebar.selectbox(
    "📂 Navegación",
    ["🏠 Home", "📊 Ejercicio 1", "🧮 Ejercicio 2", "⚙️ Ejercicio 3", "🗄️ Ejercicio 4"],
)

if pagina == "🏠 Home":
    st.title("🖥️ Proyecto 1 – Fundamentos de Programación en Python")
    st.subheader("Especialización en Python Potenciado con IA · Módulo 1 – Python Fundamentals")
    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 👤 Información Personal")
        st.write("**Nombre:** José Alex Mosquera Amaro")
        st.write("**Módulo:** Módulo 1 – Python Fundamentals")
        st.write("**Curso:** Especialización en Python for Analytics")
        st.write("**Año:** 2026")
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

elif pagina == "📊 Ejercicio 1":
    st.title("📊 Ejercicio 1 – Flujo de Caja con Listas")

    st.markdown(
        """
        **Descripción:** Módulo para registrar movimientos financieros.
        Ingresa un concepto, selecciona el tipo de movimiento e indica el valor.
        La aplicación calcula ingresos, gastos, saldo y determina si el flujo está a favor o en contra.
        """
    )
    st.markdown("---")

    # Inicializar estado
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("➕ Registrar movimiento")
        concepto = st.text_input("Concepto", placeholder="Ej: Pago de factura AWS")
        tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
        valor = st.number_input("Valor ($)", min_value=0.01, step=0.01, format="%.2f")

        if st.button("Agregar movimiento", use_container_width=True):
            if concepto.strip() == "":
                st.warning("⚠️ Por favor ingresa un concepto.")
            else:
                st.session_state.movimientos.append(
                    {"Concepto": concepto.strip(), "Tipo": tipo, "Valor ($)": round(valor, 2)}
                )
                st.success(f"✅ Movimiento '{concepto}' agregado.")

        if st.button("🗑️ Limpiar todos los movimientos", use_container_width=True):
            st.session_state.movimientos = []
            st.info("Lista limpiada.")

    with col2:
        st.subheader("📋 Resumen del flujo de caja")

        if st.session_state.movimientos:
            df = pd.DataFrame(st.session_state.movimientos)
            st.dataframe(df, use_container_width=True, hide_index=True)

            total_ingresos = sum(m["Valor ($)"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
            total_gastos = sum(m["Valor ($)"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
            saldo = total_ingresos - total_gastos

            c1, c2, c3 = st.columns(3)
            c1.metric("💰 Total Ingresos", f"${total_ingresos:,.2f}")
            c2.metric("💸 Total Gastos", f"${total_gastos:,.2f}")
            c3.metric("🏦 Saldo Final", f"${saldo:,.2f}", delta=f"${saldo:,.2f}")

            st.markdown("---")
            if saldo >= 0:
                st.success(f"✅ El flujo de caja está **a favor** con un saldo positivo de ${saldo:,.2f}")
            else:
                st.error(f"❌ El flujo de caja está **en contra** con un déficit de ${abs(saldo):,.2f}")
        else:
            st.info("Aún no hay movimientos registrados. ¡Agrega el primero!")

elif pagina == "🧮 Ejercicio 2":
    st.title("🧮 Ejercicio 2 – Registro de Equipos TI con NumPy y DataFrame")

    st.markdown(
        """
        **Descripción:** Formulario para registrar equipos tecnológicos del inventario.
        Los datos se almacenan en arrays NumPy y se convierten en un DataFrame actualizado.
        """
    )
    st.markdown("---")

    # Inicializar arrays en session_state
    if "eq_nombres" not in st.session_state:
        st.session_state.eq_nombres = np.array([], dtype=str)
        st.session_state.eq_categorias = np.array([], dtype=str)
        st.session_state.eq_precios = np.array([], dtype=float)
        st.session_state.eq_cantidades = np.array([], dtype=int)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("➕ Nuevo equipo")
        nombre = st.text_input("Nombre del equipo", placeholder="Ej: Laptop Dell XPS 15")
        categoria = st.selectbox("Categoría", ["Laptop", "Servidor", "Switch", "Router", "Monitor", "Otro"])
        precio = st.number_input("Precio unitario ($)", min_value=0.01, step=0.01, format="%.2f")
        cantidad = st.number_input("Cantidad", min_value=1, step=1, value=1)

        if st.button("Agregar equipo", use_container_width=True):
            if nombre.strip() == "":
                st.warning("⚠️ Ingresa el nombre del equipo.")
            else:
                st.session_state.eq_nombres = np.append(st.session_state.eq_nombres, nombre.strip())
                st.session_state.eq_categorias = np.append(st.session_state.eq_categorias, categoria)
                st.session_state.eq_precios = np.append(st.session_state.eq_precios, precio)
                st.session_state.eq_cantidades = np.append(st.session_state.eq_cantidades, cantidad)
                st.success(f"✅ Equipo '{nombre}' agregado.")

        if st.button("🗑️ Limpiar registros", use_container_width=True):
            st.session_state.eq_nombres = np.array([], dtype=str)
            st.session_state.eq_categorias = np.array([], dtype=str)
            st.session_state.eq_precios = np.array([], dtype=float)
            st.session_state.eq_cantidades = np.array([], dtype=int)
            st.info("Registros limpiados.")

    with col2:
        st.subheader("📋 Inventario registrado")

        if len(st.session_state.eq_nombres) > 0:
            totales = st.session_state.eq_precios * st.session_state.eq_cantidades

            df_equipos = pd.DataFrame({
                "Equipo": st.session_state.eq_nombres,
                "Categoría": st.session_state.eq_categorias,
                "Precio Unit. ($)": st.session_state.eq_precios,
                "Cantidad": st.session_state.eq_cantidades,
                "Total ($)": np.round(totales, 2),
            })

            st.dataframe(df_equipos, use_container_width=True, hide_index=True)

            c1, c2 = st.columns(2)
            c1.metric("📦 Total equipos registrados", len(st.session_state.eq_nombres))
            c2.metric("💰 Valor total inventario", f"${totales.sum():,.2f}")
        else:
            st.info("Aún no hay equipos registrados.")
