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
        font-size: 2rem;
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
        font-size: 2rem;
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
    p, label, span, div, select, input {
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

# --- BLOQUE DE ESTADO DINÁMICO ---
hoy = datetime.date.today()
manana = hoy + datetime.timedelta(days=1)

hay_cita_mañana = any(c["fecha"] == manana for c in st.session_state.citas)
hay_cita_hoy = any(c["fecha"] == hoy for c in st.session_state.citas)

if hay_cita_hoy:
    st.markdown(
        '<div class="status-card-urgente">🚨 ¡ATENCIÓN: Hoy tienes una cita programada! 🚨</div>',
        unsafe_allow_html=True,
    )
elif hay_cita_mañana:
    st.markdown(
        '<div class="status-card-urgente">⚠️ Mañana tienes una cita importante ⚠️</div>',
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

# --- SELECTOR DE MES PARA EL CALENDARIO ---
st.markdown("### 🗓️ Selector de Mes y Calendario", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    anio_seleccionado = st.selectbox(
        "Año:", [hoy.year, hoy.year + 1], index=0
    )
with col2:
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
    mes_seleccionado_nombre = st.selectbox(
        "Mes:", meses_nombres, index=(hoy.month - 1)
    )
    mes_num = meses_nombres.index(mes_seleccionado_nombre) + 1

# Mostrar calendario visual del mes seleccionado en texto claro
st.markdown(f"#### Vista Calendario: {mes_seleccionado_nombre} {anio_seleccionado}")
cal_texto = calendar.TextCalendar(calendar.SUNDAY).formatmonth(
    anio_seleccionado, mes_num
)
st.code(cal_texto, language="")

st.divider()

# --- FILTRAR CITAS DEL MES SELECCIONADO ---
st.markdown(f"### 📌 Citas Programadas en {mes_seleccionado_nombre}")

citas_del_mes = [
    c
    for c in st.session_state.citas
    if c["fecha"].year == anio_seleccionado and c["fecha"].month == mes_num
]

if not citas_del_mes:
    st.info(
        f"No hay citas registradas para {mes_seleccionado_nombre} {anio_seleccionado}."
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

# --- PANEL DE GESTIÓN Y VERIFICADOR DE HORAS DISPONIBLES ---
st.markdown("### ➕ Agendar Nueva Cita y Verificar Horas Libres")

with st.expander("🛠️ Abrir asistente para agendar cita"):
    with st.form("form_cita"):
        nuevo_titulo = st.text_input("Nombre de la cita o evento:")
        nueva_fecha = st.date_input("Fecha de la cita:", value=hoy)

        st.markdown("---")
        st.markdown(
            "**Verificador de Horarios:** Elige una hora para la cita. *(Recuerda evitar el bloque de almuerzo de 12:00 PM a 4:00 PM)*"
        )

        # Franjas horarias cómodas disponibles para el día
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
                st.success("¡Cita agendada con éxito y verificada!")
                st.rerun()
