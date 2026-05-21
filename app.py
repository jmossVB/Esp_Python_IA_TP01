import streamlit as st
import pandas as pd
import numpy as np

from libreria_funciones_proyecto1 import (
    calcular_disponibilidad_sistema,
    calcular_tiempo_transferencia_archivo,
    calcular_tasa_error_transacciones,
    calcular_almacenamiento_respaldo,
    calcular_metricas_clasificacion,
)
from libreria_clases_proyecto1 import Servidor

st.set_page_config(
    page_title="Proyecto 1 – Aplicación en Streamlit",
    page_icon="🖥️",
    layout="wide",
)

pagina = st.sidebar.selectbox(
    "📂 Navegación",
    ["🏠 Home", "📊 Ejercicio 1", "🧮 Ejercicio 2", "⚙️ Ejercicio 3", "🗄️ Ejercicio 4"],
)

if pagina == "🏠 Home":
    st.title("🖥️ Proyecto 1 – Fundamentos de Programación en Python")
    st.subheader("Especialización en Python Potenciado con IA · Módulo 1 – Python Fundamentals")
    st.markdown("---")

    col1, col2, col3 = st.columns([1, 2, 2])

    with col1:
        st.image("jmosquera.jpeg", width=200)
    with col2:
        st.markdown("### 👤 Información Personal")
        st.write("**Nombre:** José Alex Mosquera Amaro")
        st.write("**Linkedin:** https://www.linkedin.com/in/josemosquera/")
        st.write("**Curso:** Especialización en Python for Analytics")
        st.write("**Año:** 2026")
        st.markdown("---")
    with col3:
        st.markdown("### 🐍 Python for Analytics")
        st.info("Proyecto 1 – Aplicación en Streamlit\n\nMódulo 1: Python Fundamentals")
        st.markdown("**Instructor:** MSc. Carlos Carrillo Villavicencio")

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
    
    st.markdown("---")
    
    st.markdown("### 🛠️ Tecnologías utilizadas")
    tech = {
            "Tecnología": ["Python 3.x", "Streamlit", "NumPy", "Pandas"],
            "Uso": ["Lenguaje base", "Interfaz interactiva", "Arrays numéricos", "DataFrames"],
        }
    st.dataframe(pd.DataFrame(tech), use_container_width=True, hide_index=True)

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

elif pagina == "⚙️ Ejercicio 3":
    st.title("⚙️ Ejercicio 3 – Calculadoras TI (librería externa)")

    st.markdown(
        """
        **Descripción:** Uso de funciones del área de **Tecnología / Informática** desde `libreria_funciones_proyecto1.py`.
        Selecciona una función, ingresa los parámetros y ejecuta el cálculo.
        Los resultados se guardan en un historial.
        """
    )
    st.markdown("---")

    # Inicializar historial
    if "historial_funciones" not in st.session_state:
        st.session_state.historial_funciones = []

    FUNCIONES = {
        "Disponibilidad del sistema": "disponibilidad",
        "Tiempo de transferencia de archivo": "transferencia",
        "Tasa de error en transacciones": "tasa_error",
        "Almacenamiento para respaldo": "almacenamiento",
        "Métricas de clasificación ML (Precisión / Recall / F1)": "metricas_ml",
    }

    funcion_seleccionada = st.selectbox("🔧 Selecciona una función", list(FUNCIONES.keys()))
    clave = FUNCIONES[funcion_seleccionada]

    st.markdown("#### 📥 Parámetros de entrada")
    resultado = None

    # ── Disponibilidad del sistema
    if clave == "disponibilidad":
        st.markdown("Calcula qué porcentaje del tiempo un sistema estuvo disponible (uptime).")
        tiempo_total = st.number_input("Tiempo total del período (horas)", min_value=0.1, value=720.0, step=1.0)
        tiempo_caida = st.number_input("Tiempo de caída (horas)", min_value=0.0, value=2.0, step=0.1)

        if st.button("▶️ Calcular", use_container_width=True):
            try:
                resultado = calcular_disponibilidad_sistema(tiempo_total, tiempo_caida)
                st.metric("Disponibilidad del sistema", f"{resultado['disponibilidad_pct']}%")
                if resultado["disponibilidad_pct"] >= 99.9:
                    st.success("✅ Excelente disponibilidad (≥ 99.9% – nivel enterprise)")
                elif resultado["disponibilidad_pct"] >= 99.0:
                    st.info("ℹ️ Buena disponibilidad (≥ 99%)")
                else:
                    st.warning("⚠️ Disponibilidad por debajo del estándar")
                st.session_state.historial_funciones.append({
                    "Función": funcion_seleccionada,
                    "Parámetros": f"Total={tiempo_total}h, Caída={tiempo_caida}h",
                    **resultado,
                })
            except ValueError as e:
                st.error(f"Error: {e}")

    # ── Tiempo de transferencia
    elif clave == "transferencia":
        st.markdown("Estima cuánto tardará en transferirse un archivo según el ancho de banda.")
        tamano_mb = st.number_input("Tamaño del archivo (MB)", min_value=0.01, value=500.0, step=1.0)
        velocidad_mbps = st.number_input("Velocidad de red (Mbps)", min_value=0.01, value=100.0, step=1.0)

        if st.button("▶️ Calcular", use_container_width=True):
            try:
                resultado = calcular_tiempo_transferencia_archivo(tamano_mb, velocidad_mbps)
                c1, c2 = st.columns(2)
                c1.metric("⏱️ Tiempo estimado (seg)", f"{resultado['tiempo_segundos']} s")
                c2.metric("⏱️ Tiempo estimado (min)", f"{resultado['tiempo_minutos']} min")
                st.session_state.historial_funciones.append({
                    "Función": funcion_seleccionada,
                    "Parámetros": f"Archivo={tamano_mb}MB, Velocidad={velocidad_mbps}Mbps",
                    **resultado,
                })
            except ValueError as e:
                st.error(f"Error: {e}")

    # ── Tasa de error en transacciones
    elif clave == "tasa_error":
        st.markdown("Calcula qué porcentaje de transacciones fallaron en un sistema.")
        fallidas = st.number_input("Transacciones fallidas", min_value=0, value=12, step=1)
        totales = st.number_input("Transacciones totales", min_value=1, value=10000, step=100)

        if st.button("▶️ Calcular", use_container_width=True):
            try:
                resultado = calcular_tasa_error_transacciones(int(fallidas), int(totales))
                c1, c2 = st.columns(2)
                c1.metric("❌ Tasa de error", f"{resultado['tasa_error_pct']}%")
                c2.metric("✅ Tasa de éxito", f"{resultado['tasa_exito_pct']}%")
                if resultado["tasa_error_pct"] <= 0.1:
                    st.success("✅ Tasa de error excelente (≤ 0.1%)")
                elif resultado["tasa_error_pct"] <= 1.0:
                    st.info("ℹ️ Tasa de error aceptable")
                else:
                    st.error("🚨 Tasa de error alta — requiere atención")
                st.session_state.historial_funciones.append({
                    "Función": funcion_seleccionada,
                    "Parámetros": f"Fallidas={int(fallidas)}, Totales={int(totales)}",
                    **resultado,
                })
            except ValueError as e:
                st.error(f"Error: {e}")

    # ── Almacenamiento para respaldo
    elif clave == "almacenamiento":
        st.markdown("Estima el espacio de almacenamiento necesario para respaldar archivos de usuarios.")
        n_usuarios = st.number_input("Número de usuarios", min_value=1, value=100, step=1)
        archivos_usuario = st.number_input("Archivos por usuario", min_value=1, value=50, step=1)
        tamano_prom_mb = st.number_input("Tamaño promedio por archivo (MB)", min_value=0.01, value=5.0, step=0.5)
        factor_respaldo = st.number_input("Factor de respaldo (redundancia)", min_value=1.0, value=2.0, step=0.5,
                                          help="Ej: 2 = doble copia, 3 = triple copia")

        if st.button("▶️ Calcular", use_container_width=True):
            try:
                resultado = calcular_almacenamiento_respaldo(int(n_usuarios), int(archivos_usuario), tamano_prom_mb, factor_respaldo)
                c1, c2 = st.columns(2)
                c1.metric("💾 Almacenamiento estimado (MB)", f"{resultado['almacenamiento_estimado_mb']:,}")
                c2.metric("💾 Almacenamiento estimado (GB)", f"{resultado['almacenamiento_estimado_gb']:,}")
                st.session_state.historial_funciones.append({
                    "Función": funcion_seleccionada,
                    "Parámetros": f"Usuarios={int(n_usuarios)}, Archivos={int(archivos_usuario)}, Factor={factor_respaldo}x",
                    **resultado,
                })
            except ValueError as e:
                st.error(f"Error: {e}")

    # ── Métricas ML
    elif clave == "metricas_ml":
        st.markdown("Evalúa el rendimiento de un modelo de clasificación con Precisión, Recall y F1-Score.")
        tp = st.number_input("True Positives (TP)", min_value=0, value=85, step=1)
        fp = st.number_input("False Positives (FP)", min_value=0, value=10, step=1)
        fn = st.number_input("False Negatives (FN)", min_value=0, value=5, step=1)

        if st.button("▶️ Calcular", use_container_width=True):
            try:
                resultado = calcular_metricas_clasificacion(int(tp), int(fp), int(fn))
                c1, c2, c3 = st.columns(3)
                c1.metric("🎯 Precisión", resultado["precision"])
                c2.metric("📡 Recall", resultado["recall"])
                c3.metric("⚖️ F1-Score", resultado["f1_score"])
                st.session_state.historial_funciones.append({
                    "Función": funcion_seleccionada,
                    "Parámetros": f"TP={int(tp)}, FP={int(fp)}, FN={int(fn)}",
                    **resultado,
                })
            except ValueError as e:
                st.error(f"Error: {e}")

    # Historial
    st.markdown("---")
    st.subheader("📜 Historial de cálculos")
    if st.session_state.historial_funciones:
        df_hist = pd.DataFrame(st.session_state.historial_funciones)
        st.dataframe(df_hist, use_container_width=True, hide_index=True)
        if st.button("🗑️ Limpiar historial"):
            st.session_state.historial_funciones = []
            st.rerun()
    else:
        st.info("Aún no hay cálculos en el historial.")

elif pagina == "🗄️ Ejercicio 4":
    st.title("🗄️ Ejercicio 4 – Gestión de Servidores (CRUD con clase Servidor)")

    st.markdown(
        """
        **Descripción:** CRUD completo usando la clase `Servidor` de `libreri_a_clases_proyecto1.py`.
        Puedes **Crear**, **Leer**, **Actualizar** y **Eliminar** registros de servidores.
        """
    )
    st.markdown("---")

    # Inicializar almacenamiento de servidores
    if "servidores" not in st.session_state:
        st.session_state.servidores = {}  # dict: nombre → dict de atributos

    tabs = st.tabs(["➕ Crear", "📋 Ver todos", "✏️ Actualizar", "🗑️ Eliminar"])

    # ── TAB CREAR
    with tabs[0]:
        st.subheader("➕ Registrar nuevo servidor")
        with st.container():
            nombre_sv = st.text_input("Nombre del servidor", placeholder="Ej: web-server-01")
            col1, col2 = st.columns(2)
            with col1:
                tiempo_total = st.number_input("Tiempo total del período (h)", min_value=0.1, value=720.0, step=1.0, key="c_tt")
                almacenamiento_total = st.number_input("Almacenamiento total (GB)", min_value=0.1, value=500.0, step=10.0, key="c_at")
            with col2:
                tiempo_caida = st.number_input("Tiempo de caída (h)", min_value=0.0, value=0.0, step=0.1, key="c_tc")
                almacenamiento_usado = st.number_input("Almacenamiento usado (GB)", min_value=0.0, value=120.0, step=5.0, key="c_au")

            if st.button("💾 Crear servidor", use_container_width=True):
                if nombre_sv.strip() == "":
                    st.warning("⚠️ Ingresa el nombre del servidor.")
                elif nombre_sv.strip() in st.session_state.servidores:
                    st.error("❌ Ya existe un servidor con ese nombre.")
                else:
                    try:
                        sv = Servidor(nombre_sv.strip(), tiempo_total, tiempo_caida, almacenamiento_total, almacenamiento_usado)
                        st.session_state.servidores[nombre_sv.strip()] = {
                            "nombre": nombre_sv.strip(),
                            "tiempo_total_h": tiempo_total,
                            "tiempo_caida_h": tiempo_caida,
                            "almacenamiento_total_gb": almacenamiento_total,
                            "almacenamiento_usado_gb": almacenamiento_usado,
                            **sv.resumen(),
                        }
                        st.success(f"✅ Servidor '{nombre_sv.strip()}' creado correctamente.")
                    except ValueError as e:
                        st.error(f"Error de validación: {e}")

    # ── TAB VER TODOS
    with tabs[1]:
        st.subheader("📋 Servidores registrados")
        if st.session_state.servidores:
            filas = []
            for sv_data in st.session_state.servidores.values():
                filas.append({
                    "Nombre": sv_data["nombre"],
                    "Disponibilidad (%)": sv_data["disponibilidad_pct"],
                    "Uso Almac. (%)": sv_data["uso_almacenamiento_pct"],
                    "Estado": sv_data["estado"],
                    "Total Almac. (GB)": sv_data["almacenamiento_total_gb"],
                    "Usado (GB)": sv_data["almacenamiento_usado_gb"],
                })
            df_sv = pd.DataFrame(filas)

            # Colorear estado
            def color_estado(val):
                colores = {"Óptimo": "background-color: #d4edda", "Advertencia": "background-color: #fff3cd", "Crítico": "background-color: #f8d7da"}
                return colores.get(val, "")

            st.dataframe(
                df_sv.style.map(color_estado, subset=["Estado"]),
                use_container_width=True,
                hide_index=True,
            )

            # Métricas globales
            st.markdown("---")
            c1, c2, c3 = st.columns(3)
            c1.metric("🖥️ Total servidores", len(filas))
            optimos = sum(1 for r in filas if r["Estado"] == "Óptimo")
            c2.metric("✅ En estado Óptimo", optimos)
            criticos = sum(1 for r in filas if r["Estado"] == "Crítico")
            c3.metric("🚨 En estado Crítico", criticos)
        else:
            st.info("No hay servidores registrados aún. Ve a ➕ Crear para empezar.")

    # ── TAB ACTUALIZAR
    with tabs[2]:
        st.subheader("✏️ Actualizar servidor existente")
        if not st.session_state.servidores:
            st.info("No hay servidores para actualizar.")
        else:
            sv_nombre = st.selectbox("Selecciona el servidor a actualizar", list(st.session_state.servidores.keys()), key="upd_select")
            sv_actual = st.session_state.servidores[sv_nombre]

            st.markdown(f"**Estado actual:** `{sv_actual['estado']}` | Disponibilidad: `{sv_actual['disponibilidad_pct']}%` | Uso almac.: `{sv_actual['uso_almacenamiento_pct']}%`")
            st.markdown("Modifica los valores que necesites:")

            col1, col2 = st.columns(2)
            with col1:
                new_tt = st.number_input("Tiempo total (h)", min_value=0.1, value=float(sv_actual["tiempo_total_h"]), key="u_tt")
                new_at = st.number_input("Almacenamiento total (GB)", min_value=0.1, value=float(sv_actual["almacenamiento_total_gb"]), key="u_at")
            with col2:
                new_tc = st.number_input("Tiempo caída (h)", min_value=0.0, value=float(sv_actual["tiempo_caida_h"]), key="u_tc")
                new_au = st.number_input("Almacenamiento usado (GB)", min_value=0.0, value=float(sv_actual["almacenamiento_usado_gb"]), key="u_au")

            if st.button("💾 Guardar cambios", use_container_width=True):
                try:
                    sv_upd = Servidor(sv_nombre, new_tt, new_tc, new_at, new_au)
                    st.session_state.servidores[sv_nombre] = {
                        "nombre": sv_nombre,
                        "tiempo_total_h": new_tt,
                        "tiempo_caida_h": new_tc,
                        "almacenamiento_total_gb": new_at,
                        "almacenamiento_usado_gb": new_au,
                        **sv_upd.resumen(),
                    }
                    st.success(f"✅ Servidor '{sv_nombre}' actualizado. Nuevo estado: **{sv_upd.estado_servidor()}**")
                except ValueError as e:
                    st.error(f"Error de validación: {e}")

    # ── TAB ELIMINAR
    with tabs[3]:
        st.subheader("🗑️ Eliminar servidor")
        if not st.session_state.servidores:
            st.info("No hay servidores para eliminar.")
        else:
            sv_del = st.selectbox("Selecciona el servidor a eliminar", list(st.session_state.servidores.keys()), key="del_select")
            sv_info = st.session_state.servidores[sv_del]
            st.warning(f"⚠️ Estás a punto de eliminar: **{sv_del}** (Estado: {sv_info['estado']}). Esta acción no se puede deshacer.")

            if st.button("🗑️ Confirmar eliminación", use_container_width=True):
                del st.session_state.servidores[sv_del]
                st.success(f"✅ Servidor '{sv_del}' eliminado correctamente.")
                st.rerun()
