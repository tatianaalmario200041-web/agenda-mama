import calendar
import datetime
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Agenda de Mamá", page_icon="💖", layout="centered"
)

# Estilos CSS accesibles y amigables
st.markdown(
    """
    <style>
    .main {
        background-color: #F8F9FA;
    }
    h1 {
        color: #4A154B;
        text-align: center;
        font-size: 2.8rem !important;
        font-weight: 800 !important;
    }
    .status-card-urgente {
        background-color: #FF6B6B;
        color: white;
        padding: 22px;
        border-radius: 20px;
        text-align: center;
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .status-card-tranquilo {
        background-color: #51CF66;
        color: white;
        padding: 22px;
        border-radius: 20px;
        text-align: center;
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .routine-subtle {
        background-color: #E9ECEF;
        border-left: 8px solid #ADB5BD;
        color: #495057;
        padding: 18px 22px;
        border-radius: 12px;
        font-size: 1.4rem;
        margin-bottom: 25px;
    }
    .calendar-card {
        background-color: white;
        border: 2px solid #E2E8F0;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.04);
    }
    .calendar-date-badge {
        background-color: #7950F2;
        color: white;
        padding: 8px 15px;
        border-radius: 10px;
        font-weight: bold;
        font-size: 1.2rem;
        display: inline-block;
        margin-bottom: 10px;
    }
    p, label, span, div, input {
        font-size: 1.3rem !important;
    }
    .stButton>button {
        font-size: 1.4rem !important;
        padding: 10px 20px !important;
        border-radius: 12px !important;
        font-weight: bold !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Título principal
st.markdown("<h1>📅 Agenda de Mamá</h1>", unsafe_allow_html=True)

# Inicializar lista de citas en memoria de sesión
if "citas" not in st.session_state:
    st.session_state.citas = [
        {
            "titulo": "Control Médico General",
            "fecha": (datetime.date.today() + datetime.timedelta(days=1)),
            "hora": "10:00 AM",
        }
    ]

# --- CONTROL DE MES ACTIVO EN SESIÓN ---
hoy = datetime.date.today()
if "mes_activo" not in st.session_state:
    st.session_state.mes_activo = hoy.month
if "anio_activo" not in st.session_state:
    st.session_state.anio_activo = hoy.year

# --- BLOQUE DE ESTADO DINÁMICO DETALLADO ---
manana = hoy + datetime.timedelta(days=1)

cita_hoy = next((c for c in st.session_state.citas if c["fecha"] == hoy), None)
cita_manana = next(
    (c for c in st.session_state.citas if c["fecha"] == manana), None
)

if cita_hoy:
    st.markdown(
        f"""
        <div class="status-card-urgente">
            🚨 ¡ATENCIÓN HOY! 🚨<br>
            📌 <b>{cita_hoy['titulo']}</b> a las <b>{cita_hoy['hora']}</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
elif cita_manana:
    st.markdown(
        f"""
        <div class="status-card-urgente">
            ⚠️ MAÑANA TIENES CITA ⚠️<br>
            📌 <b>{cita_manana['titulo']}</b> a las <b>{cita_manana['hora']}</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        '<div class="status-card-tranquilo">✨ ¡Todo tranquilo por hoy! Disfruta tu día ✨</div>',
        unsafe_allow_html=True,
    )

# --- RUTINA FIJA DIARIA ---
st.markdown(
    """
    <div class="routine-subtle">
        <b>🕒 Rutina Diaria Fija:</b> Almuerzo / Lonchera de <b>12:00 PM – 4:00 PM</b> *(Horario reservado)*
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# --- NAVEGACIÓN DE MESES CON BOTONES (SIN DESPLETABLES) ---
meses_nombres = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
]

st.markdown("### 🗓️ Calendario por Meses", unsafe_allow_html=True)

col_izq, col_centro, col_der = st.columns([1, 2, 1])

with col_izq:
    if st.button("⬅️ Anterior"):
        if st.session_state.mes_activo == 1:
            st.session_state.mes_activo = 12
            st.session_state.anio_activo -= 1
        else:
            st.session_state.mes_activo -= 1
        st.rerun()

with col_centro:
    nombre_mes_actual = meses_nombres[st.session_state.mes_activo - 1]
    st.markdown(
        f"<h3 style='text-align: center; color: #7950F2; margin: 0;'>{nombre_mes_actual} {st.session_state.anio_activo}</h3>",
        unsafe_allow_html=True,
    )

with col_der:
    if st.button("Siguiente ➡️"):
        if st.session_state.mes_activo == 12:
            st.session_state.mes_activo = 1
            st.session_state.anio_activo += 1
        else:
            st.session_state.mes_activo += 1
        st.rerun()

# Mostrar cuadrícula de texto del mes actual
cal_texto = calendar.TextCalendar(calendar.SUNDAY).formatmonth(
    st.session_state.anio_activo, st.session_state.mes_activo
)
st.code(cal_texto, language="")

st.divider()

# --- TARJETAS DE CITAS DEL MES SELECCIONADO ---
st.markdown(
    f"### 📌 Citas Programadas en {nombre_mes_actual} {st.session_state.anio_activo}",
    unsafe_allow_html=True,
)

citas_del_mes = [
    c
    for c in st.session_state.citas
    if c["fecha"].year == st.session_state.anio_activo
    and c["fecha"].month == st.session_state.mes_activo
]

if not citas_del_mes:
    st.info(
        f"No hay citas registradas para {nombre_mes_actual} {st.session_state.anio_activo}."
    )
else:
    citas_ordenadas = sorted(citas_del_mes, key=lambda x: x["fecha"])
    for cita in citas_ordenadas:
        fecha_str = cita["fecha"].strftime("%A, %d de %B de %Y")
        st.markdown(
            f"""
            <div class="calendar-card">
                <div><span class="calendar-date-badge">📅 {fecha_str}</span></div>
                <div style="font-size: 1.6rem; font-weight: bold; color: #212529; margin-top: 5px;">
                    📌 {cita['titulo']}
                </div>
                <div style="color: #6C757D; margin-top: 5px;">
                    ⏰ Hora programada: <b>{cita['hora']}</b>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# --- PANEL DE GESTIÓN Y VERIFICADOR DE HORAS ---
st.markdown("### ➕ Agendar Nueva Cita y Verificar Horas Libres")

with st.expander("🛠️ Abrir asistente para agendar cita"):
    with st.form("form_cita"):
        nuevo_titulo = st.text_input("Nombre de la cita o evento:")
        nueva_fecha = st.date_input("Fecha de la cita:", value=hoy)

        st.markdown("---")
        st.markdown(
            "**Verificador de Horarios:** Elige una hora para la cita. *(Recuerda evitar el bloque de almuerzo de 12:00 PM a 4:00 PM)*"
        )

        horarios_disponibles = [
            "08:00 AM",
            "09:00 AM",
            "10:00 AM",
            "11:00 AM",
            "12:00 PM (⚠️ Almuerzo)",
            "01:00 PM (⚠️ Almuerzo)",
            "02:00 PM (⚠️ Almuerzo)",
            "03:00 PM (⚠️ Almuerzo)",
            "04:00 PM",
            "05:00 PM",
            "06:00 PM",
        ]
        nueva_hora = st.selectbox(
            "Selecciona la hora sugerida:", horarios_disponibles
        )

        guardar = st.form_submit_button("Guardar Cita en la Agenda")

        if guardar and nuevo_titulo:
            if "Almuerzo" in nueva_hora:
                st.error(
                    "❌ ¡Esa hora está reservada para el Almuerzo/Lonchera (12:00 PM - 4:00 PM)! Elige otra."
                )
            else:
                st.session_state.citas.append(
                    {
                        "titulo": nuevo_titulo,
                        "fecha": nueva_fecha,
                        "hora": nueva_hora,
                    }
                )
                # Actualizar automáticamente el mes activo al mes de la nueva cita para que la vea de inmediato
                st.session_state.mes_activo = nueva_fecha.month
                st.session_state.anio_activo = nueva_fecha.year
                st.success("¡Cita agendada con éxito y verificada!")
                st.rerun()
