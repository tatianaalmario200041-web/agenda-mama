import datetime
import streamlit as st

# Configuración de la página orientada a accesibilidad visual
st.set_page_config(
    page_title="Agenda de Mamá", page_icon="💖", layout="centered"
)

# Estilos CSS mejorados: calendario visual limpio y rutina en tono tenue
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
    /* Estilo tenue y elegante para la rutina diaria (sin caja azul pesada) */
    .routine-subtle {
        background-color: #E9ECEF;
        border-left: 8px solid #ADB5BD;
        color: #495057;
        padding: 18px 22px;
        border-radius: 12px;
        font-size: 1.4rem;
        margin-bottom: 25px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    /* Estilo tipo Calendario Tradicional para las citas */
    .calendar-card {
        background-color: white;
        border: 2px solid #E2E8F0;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.04);
        display: flex;
        flex-direction: column;
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
        text-align: center;
    }
    p, label, span, div {
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

# Título principal gigante
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

# --- RUTINA FIJA DIARIA EN TONO TENUE ---
st.markdown(
    """
    <div class="routine-subtle">
        <b>🕒 Rutina Diaria:</b> Almuerzo / Lonchera de <b>12:00 PM – 4:00 PM</b>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# --- VISTA DE CALENDARIO VISUAL ---
st.markdown(
    "### 🗓️ Calendario de Eventos y Citas", unsafe_allow_html=True
)

if not st.session_state.citas:
    st.info("No hay citas registradas en el calendario.")
else:
    # Ordenar citas por fecha
    citas_ordenadas = sorted(st.session_state.citas, key=lambda x: x["fecha"])

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

# --- PANEL DE GESTIÓN ---
with st.expander("➕ Agregar una nueva cita al calendario"):
    with st.form("form_cita"):
        nuevo_titulo = st.text_input("Nombre de la cita o evento:")
        nueva_fecha = st.date_input("Fecha de la cita:", value=hoy)
        nueva_hora = st.text_input("Hora (ej: 3:00 PM):", value="2:00 PM")
        guardar = st.form_submit_button("Guardar en el Calendario")

        if guardar and nuevo_titulo:
            st.session_state.citas.append(
                {
                    "titulo": nuevo_titulo,
                    "fecha": nueva_fecha,
                    "hora": nueva_hora,
                }
            )
            st.success("¡Cita agregada al calendario con éxito!")
            st.rerun()
