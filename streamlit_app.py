import calendar
import datetime
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Agenda de Mamá", page_icon="📖", layout="centered"
)

# Estilos CSS estilo Cuaderno / Agenda Manual con ingeniería visual e intuitiva
st.markdown(
    """
    <style>
    .main {
        background-color: #F4F6F9;
    }
    h1 {
        color: #2C3E50;
        text-align: center;
        font-size: 2.8rem !important;
        font-weight: 800 !important;
        font-family: 'Georgia', serif;
    }
    .alerta-hoy {
        background-color: #FDEDEC;
        border-left: 10px solid #E74C3C;
        color: #922B21;
        padding: 20px;
        border-radius: 12px;
        font-size: 1.6rem;
        font-weight: bold;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    }
    .alerta-mañana {
        background-color: #FEF9E7;
        border-left: 10px solid #F1C40F;
        color: #7D6608;
        padding: 20px;
        border-radius: 12px;
        font-size: 1.6rem;
        font-weight: bold;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    }
    .tranquilo {
        background-color: #EAFAF1;
        border-left: 10px solid #2ECC71;
        color: #196F3D;
        padding: 20px;
        border-radius: 12px;
        font-size: 1.6rem;
        font-weight: bold;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    }
    .rutina-fija {
        background-color: #EBF5FB;
        border-left: 8px solid #3498DB;
        color: #1B4F72;
        padding: 15px 20px;
        border-radius: 12px;
        font-size: 1.3rem;
        margin-bottom: 25px;
    }
    .tarjeta-cita {
        background-color: #FFFFFF;
        border: 1px solid #D5DBDB;
        border-left: 8px solid #8E44AD;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.04);
    }
    .badge-fecha {
        background-color: #8E44AD;
        color: white;
        padding: 6px 12px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 1.1rem;
        display: inline-block;
        margin-bottom: 8px;
    }
    p, label, span, div, input {
        font-size: 1.25rem !important;
    }
    .stButton>button {
        font-size: 1.3rem !important;
        padding: 10px 20px !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        background-color: #8E44AD !important;
        color: white !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Título principal de la agenda estilo cuaderno
st.markdown("<h1>📖 Agenda Personal de Mamá</h1>", unsafe_allow_html=True)

# Inicializar lista de citas en memoria
if "citas" not in st.session_state:
    st.session_state.citas = [
        {
            "titulo": "Control Médico General",
            "fecha": (datetime.date.today() + datetime.timedelta(days=1)),
            "hora": "10:00 AM",
        }
    ]

# Configuración de fechas en español
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

dias_semana_es = {
    "Monday": "Lunes",
    "Tuesday": "Martes",
    "Wednesday": "Miércoles",
    "Thursday": "Jueves",
    "Friday": "Viernes",
    "Saturday": "Sábado",
    "Sunday": "Domingo",
}

hoy = datetime.date.today()
if "mes_activo" not in st.session_state:
    st.session_state.mes_activo = hoy.month
if "anio_activo" not in st.session_state:
    st.session_state.anio_activo = hoy.year

# --- BLOQUE DE ALERTAS INTELIGENTES ---
manana = hoy + datetime.timedelta(days=1)

cita_hoy = next((c for c in st.session_state.citas if c["fecha"] == hoy), None)
cita_manana = next(
    (c for c in st.session_state.citas if c["fecha"] == manana), None
)

if cita_hoy:
    st.markdown(
        f"""
        <div class="alerta-hoy">
            🚨 ¡Atención! Tienes una cita programada para HOY:<br>
            📌 <b>{cita_hoy['titulo']}</b> a las <b>{cita_hoy['hora']}</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
elif cita_manana:
    st.markdown(
        f"""
        <div class="alerta-mañana">
            ⚠️ Atención: Mañana tienes una cita importante:<br>
            📌 <b>{cita_manana['titulo']}</b> a las <b>{cita_manana['hora']}</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        '<div class="tranquilo">✨ ¡Todo tranquilo por hoy! Disfruta de tu día con calma. ✨</div>',
        unsafe_allow_html=True,
    )

# --- RUTINA FIJA DIARIA ---
st.markdown(
    """
    <div class="routine-fija">
        <b>🕒 Rutina Diaria Fija:</b> Almuerzo / Lonchera reservada de <b>12:00 PM – 4:00 PM</b> *(Horario de descanso)*
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# --- NAVEGACIÓN ARMÓNICA DE MESES ---
st.markdown(
    "<h3 style='text-align: center; color: #2C3E50;'>📅 Calendario Mensual</h3>",
    unsafe_allow_html=True,
)

col_izq, col_centro, col_der = st.columns([1, 2, 1])

with col_izq:
    if st.button("⬅️ Mes Anterior"):
        if st.session_state.mes_activo == 1:
            st.session_state.mes_activo = 12
            st.session_state.anio_activo -= 1
        else:
            st.session_state.mes_activo -= 1
        st.rerun()

with col_centro:
    nombre_mes_actual = meses_nombres[st.session_state.mes_activo - 1]
    st.markdown(
        f"<h3 style='text-align: center; color: #8E44AD; margin: 0;'>{nombre_mes_actual} de {st.session_state.anio_activo}</h3>",
        unsafe_allow_html=True,
    )

with col_der:
    if st.button("Mes Siguiente ➡️"):
        if st.session_state.mes_activo == 12:
            st.session_state.mes_activo = 1
            st.session_state.anio_activo += 1
        else:
            st.session_state.mes_activo += 1
        st.rerun()

# Vista clásica de calendario en texto limpio
cal_texto = calendar.TextCalendar(calendar.SUNDAY).formatmonth(
    st.session_state.anio_activo, st.session_state.mes_activo
)
st.code(cal_texto, language="")

st.divider()

# --- LISTADO DE APUNTES / CITAS DEL MES SELECCIONADO ---
st.markdown(
    f"<h3 style='color: #2C3E50;'>📌 Apuntes y Citas de {nombre_mes_actual}</h3>",
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
        f"No hay citas ni eventos anotados para {nombre_mes_actual} de {st.session_state.anio_activo}."
    )
else:
    citas_ordenadas = sorted(citas_del_mes, key=lambda x: x["fecha"])
    for cita in citas_ordenadas:
        dia_ingles = cita["fecha"].strftime("%A")
        dia_espanol = dias_semana_es.get(dia_ingles, dia_ingles)
        fecha_str = f"{dia_espanol}, {cita['fecha'].day} de {nombre_mes_actual} de {cita['fecha'].year}"

        st.markdown(
            f"""
            <div class="tarjeta-cita">
                <div><span class="badge-fecha">📅 {fecha_str}</span></div>
                <div style="font-size: 1.5rem; font-weight: bold; color: #2C3E50; margin-top: 5px;">
                    ✍️ {cita['titulo']}
                </div>
                <div style="color: #7F8C8D; margin-top: 5px; font-size: 1.2rem;">
                    ⏰ Hora fijada: <b>{cita['hora']}</b>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# --- ASISTENTE PARA AGENDAR NUEVA CITA ---
st.markdown(
    "<h3 style='color: #2C3E50;'>➕ Anotar Nueva Cita en la Libreta</h3>",
    unsafe_allow_html=True,
)

with st.expander("📝 Abrir formulario para registrar un evento"):
    with st.form("form_cita"):
        nuevo_titulo = st.text_input("¿Qué evento o cita se va a programar?")
        nueva_fecha = st.date_input("Fecha exacta del evento:", value=hoy)

        st.markdown("---")
        st.markdown(
            "**Verificador de Horarios Libres:** Selecciona una hora adecuada. *(Evita el bloque de almuerzo/lonchera de 12:00 PM a 4:00 PM)*"
        )

        horarios_disponibles = [
            "08:00 AM",
            "09:00 AM",
            "10:00 AM",
            "11:00 AM",
            "12:00 PM (⚠️ Almuerzo/Lonchera)",
            "01:00 PM (⚠️ Almuerzo/Lonchera)",
            "02:00 PM (⚠️ Almuerzo/Lonchera)",
            "03:00 PM (⚠️ Almuerzo/Lonchera)",
            "04:00 PM",
            "05:00 PM",
            "06:00 PM",
        ]
        nueva_hora = st.selectbox(
            "Selecciona la hora disponible:", horarios_disponibles
        )

        guardar = st.form_submit_button("Guardar Apunte en la Agenda")

        if guardar and nuevo_titulo:
            if "Almuerzo" in nueva_hora:
                st.error(
                    "❌ ¡Esa hora está ocupada por la rutina de almuerzo/lonchera (12:00 PM - 4:00 PM)! Por favor selecciona otra hora."
                )
            else:
                st.session_state.citas.append(
                    {
                        "titulo": nuevo_titulo,
                        "fecha": nueva_fecha,
                        "hora": nueva_hora,
                    }
                )
                # Salto automático al mes de la cita agregada
                st.session_state.mes_activo = nueva_fecha.month
                st.session_state.anio_activo = nueva_fecha.year
                st.success("¡Cita anotada con éxito en la libreta!")
                st.rerun()
