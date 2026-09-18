import datetime
import streamlit as st

# Configuración de la página orientada a accesibilidad visual
st.set_page_config(
    page_title="Agenda de Mamá", page_icon="💖", layout="centered"
)

# Estilos CSS personalizados para textos gigantes, alto contraste y botones táctiles cómodos
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
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        font-size: 2.2rem;
        font-weight: bold;
        margin-bottom: 25px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .status-card-tranquilo {
        background-color: #51CF66;
        color: white;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        font-size: 2.2rem;
        font-weight: bold;
        margin-bottom: 25px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .routine-card {
        background-color: #339AF0;
        color: white;
        padding: 22px;
        border-radius: 20px;
        font-size: 1.8rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .appointment-card {
        background-color: white;
        border-left: 12px solid #7950F2;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        font-size: 1.5rem;
        color: #212529;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
    }
    p, label, span, div {
        font-size: 1.3rem !important;
    }
    .stButton>button {
        font-size: 1.5rem !important;
        padding: 12px 24px !important;
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

# --- BLOQUE DE ESTADO DINÁMICO GIGANTE ---
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
    '<div class="routine-card">🕒 Rutina Diaria Fija<br>🍽️ Almuerzo / Lonchera: 12:00 PM – 4:00 PM</div>',
    unsafe_allow_html=True,
)

st.divider()

# --- SECCIÓN VISUAL DE CITAS ---
st.markdown("### 📌 Próximos Eventos y Citas", unsafe_allow_html=True)

if not st.session_state.citas:
    st.info("No hay citas registradas por ahora.")
else:
    for cita in st.session_state.citas:
        fecha_str = cita["fecha"].strftime("%A %d de %B, %Y")
        st.markdown(
            f"""
            <div class="appointment-card">
                <b>{cita['titulo']}</b><br>
                📅 Fecha: {fecha_str}<br>
                ⏰ Hora: {cita['hora']}
            </div>
            """,
            unsafe_allow_html=True,
        )

# --- PANEL DE GESTIÓN ---
with st.expander("➕ Agregar una nueva cita (Familiar)"):
    with st.form("form_cita"):
        nuevo_titulo = st.text_input("Nombre de la cita o evento:")
        nueva_fecha = st.date_input("Fecha de la cita:", value=hoy)
        nueva_hora = st.text_input("Hora (ej: 3:00 PM):", value="2:00 PM")
        guardar = st.form_submit_button("Guardar Cita")

        if guardar and nuevo_titulo:
            st.session_state.citas.append(
                {
                    "titulo": nuevo_titulo,
                    "fecha": nueva_fecha,
                    "hora": nueva_hora,
                }
            )
            st.success("¡Cita agregada con éxito!")
            st.rerun()
