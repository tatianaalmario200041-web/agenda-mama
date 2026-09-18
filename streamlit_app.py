import calendar
import datetime
import streamlit as st

# Configuración de página optimizada para celular e iPad
st.set_page_config(
    page_title="Agenda de Mamá", page_icon="📖", layout="centered"
)

# Estilos CSS modernos, limpios y 100% adaptados a móviles
st.markdown(
    """
    <style>
    .main {
        background-color: #F8F9FA;
    }
    h1 {
        color: #2C3E50;
        text-align: center;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        font-family: 'Georgia', serif;
    }
    .alerta-proxima {
        background-color: #FEF9E7;
        border-left: 8px solid #F1C40F;
        color: #7D6608;
        padding: 16px;
        border-radius: 12px;
        font-size: 1.25rem;
        font-weight: bold;
        margin-bottom: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .tranquilo {
        background-color: #EAFAF1;
        border-left: 8px solid #2ECC71;
        color: #196F3D;
        padding: 16px;
        border-radius: 12px;
        font-size: 1.25rem;
        font-weight: bold;
        margin-bottom: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .tarjeta-dia-movil {
        background-color: #FFFFFF;
        border: 1px solid #E5E7E9;
        border-left: 8px solid #8E44AD;
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
    }
    .badge-almuerzo {
        background-color: #FADBD8;
        color: #78281F;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.95rem;
        font-weight: bold;
        display: inline-block;
        margin-top: 6px;
    }
    p, label, span, div, input {
        font-size: 1.15rem !important;
    }
    .stButton>button {
        font-size: 1.15rem !important;
        padding: 10px 14px !important;
        border-radius: 10px !important;
        font-weight: bold !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Título principal
st.markdown("<h1>📖 Agenda de Mamá</h1>", unsafe_allow_html=True)

# Inicializar lista con TODAS las citas reales del calendario físico de Septiembre, Octubre y Noviembre 2026
if "citas" not in st.session_state:
    st.session_state.citas = [
        # --- SEPTIEMBRE 2026 ---
        {
            "titulo": "Fatima RBC",
            "fecha": datetime.date(2026, 9, 2),
            "hora": "08:00 AM",
        },
        {
            "titulo": "San Benito - Fono",
            "fecha": datetime.date(2026, 9, 2),
            "hora": "11:00 AM",
        },
        {
            "titulo": "Derecho de petición (Tatiana y Yuly)",
            "fecha": datetime.date(2026, 9, 2),
            "hora": "09:00 AM",
        },
        {
            "titulo": "Candelaria TO",
            "fecha": datetime.date(2026, 9, 4),
            "hora": "07:30 AM",
        },
        {
            "titulo": "San Benito Psico / Fono",
            "fecha": datetime.date(2026, 9, 7),
            "hora": "09:00 AM",
        },
        {
            "titulo": "Candelaria TO",
            "fecha": datetime.date(2026, 9, 8),
            "hora": "10:30 AM",
        },
        {
            "titulo": "Fatima RBC",
            "fecha": datetime.date(2026, 9, 9),
            "hora": "08:00 AM",
        },
        {
            "titulo": "Norte - Chapinero (Teletón)",
            "fecha": datetime.date(2026, 9, 10),
            "hora": "09:00 AM",
        },
        {
            "titulo": "Candelaria Física",
            "fecha": datetime.date(2026, 9, 12),
            "hora": "09:00 AM",
        },
        {
            "titulo": "San Benito Fono",
            "fecha": datetime.date(2026, 9, 14),
            "hora": "11:00 AM",
        },
        {
            "titulo": "Candelaria TO",
            "fecha": datetime.date(2026, 9, 15),
            "hora": "10:30 AM",
        },
        {
            "titulo": "San José Terapia de Choque",
            "fecha": datetime.date(2026, 9, 15),
            "hora": "02:00 PM",
        },
        {
            "titulo": "Fatima RBC / San Benito Psico / Fono / Citología",
            "fecha": datetime.date(2026, 9, 16),
            "hora": "08:00 AM",
        },
        {
            "titulo": "San José Terapia de Choque",
            "fecha": datetime.date(2026, 9, 17),
            "hora": "01:30 PM",
        },
        {
            "titulo": "Cump. Jana Parra",
            "fecha": datetime.date(2026, 9, 18),
            "hora": "10:00 AM",
        },
        {
            "titulo": "Cine Tatiana",
            "fecha": datetime.date(2026, 9, 19),
            "hora": "03:00 PM",
        },
        {
            "titulo": "San José Terapia de Choque",
            "fecha": datetime.date(2026, 9, 22),
            "hora": "01:30 PM",
        },
        {
            "titulo": "Fatima RBC / San Benito / Derecho petición",
            "fecha": datetime.date(2026, 9, 23),
            "hora": "08:00 AM",
        },
        {
            "titulo": "San José Terapia de Choque",
            "fecha": datetime.date(2026, 9, 24),
            "hora": "01:30 PM",
        },
        {
            "titulo": "Candelaria Física",
            "fecha": datetime.date(2026, 9, 25),
            "hora": "02:00 PM",
        },
        {
            "titulo": "San Benito Fono",
            "fecha": datetime.date(2026, 9, 28),
            "hora": "09:00 AM",
        },
        {
            "titulo": "Fatima RBC / San Benito Fono",
            "fecha": datetime.date(2026, 9, 30),
            "hora": "08:00 AM",
        },
        # --- OCTUBRE 2026 ---
        {
            "titulo": "Fatima RBC / Psico / San Benito",
            "fecha": datetime.date(2026, 10, 7),
            "hora": "08:00 AM",
        },
        {
            "titulo": "Tatiana - CC en Soacha / Odontología",
            "fecha": datetime.date(2026, 10, 9),
            "hora": "09:40 AM",
        },
        {
            "titulo": "Fono San Benito",
            "fecha": datetime.date(2026, 10, 19),
            "hora": "08:30 AM",
        },
        {
            "titulo": "Fatima RBC",
            "fecha": datetime.date(2026, 10, 21),
            "hora": "08:00 AM",
        },
        {
            "titulo": "Cita de Psicograma / Retina",
            "fecha": datetime.date(2026, 10, 22),
            "hora": "10:00 AM",
        },
        {
            "titulo": "Psicología",
            "fecha": datetime.date(2026, 10, 23),
            "hora": "10:00 AM",
        },
        {
            "titulo": "Fono San Benito",
            "fecha": datetime.date(2026, 10, 26),
            "hora": "08:30 AM",
        },
        {
            "titulo": "Fatima RBC",
            "fecha": datetime.date(2026, 10, 28),
            "hora": "08:00 AM",
        },
        # --- NOVIEMBRE 2026 ---
        {
            "titulo": "Fatima RBC",
            "fecha": datetime.date(2026, 11, 4),
            "hora": "08:00 AM",
        },
        {
            "titulo": "Tunal - Ecografía",
            "fecha": datetime.date(2026, 11, 5),
            "hora": "12:00 PM",
        },
        {
            "titulo": "Desparasitación Morita ($8000)",
            "fecha": datetime.date(2026, 11, 21),
            "hora": "10:00 AM",
        },
    ]

# Meses y días en español
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

# --- BLOQUE DE ALERTAS INTELIGENTES (HOY Y LOS DOS DÍAS SIGUIENTES) ---
dias_a_revisar = [
    (hoy, "🚨 HOY"),
    (hoy + datetime.timedelta(days=1), "⚠️ MAÑANA"),
    (hoy + datetime.timedelta(days=2), "📅 EN DOS DÍAS"),
]

citas_encontradas_alerta = False
for fecha_obj, etiqueta in dias_a_revisar:
    citas_dia = [c for c in st.session_state.citas if c["fecha"] == fecha_obj]
    for c in citas_dia:
        citas_encontradas_alerta = True
        st.markdown(
            f"""
            <div class="alerta-proxima">
                {etiqueta}: <b>{c['titulo']}</b><br>
                ⏰ Fecha: {fecha_obj.strftime('%d/%m/%Y')} a las <b>{c['hora']}</b>
            </div>
            """,
            unsafe_allow_html=True,
        )

if not citas_encontradas_alerta:
    st.markdown(
        '<div class="tranquilo">✨ ¡Todo tranquilo para estos días! Disfruta con calma. ✨</div>',
        unsafe_allow_html=True,
    )

st.divider()

# --- SELECTOR DE MESES (SOLO RESTANTES DEL AÑO) ---
meses_disponibles = []
for m in range(hoy.month, 13):
    meses_disponibles.append((m, meses_nombres[m - 1]))

cols_meses = st.columns(len(meses_disponibles))
for idx, (m_num, m_nombre) in enumerate(meses_disponibles):
    with cols_meses[idx]:
        if st.button(
            f"{m_nombre[:3]}",
            key=f"mes_btn_{m_num}",
            use_container_width=True,
            type=(
                "primary" if st.session_state.mes_activo == m_num else "secondary"
            ),
        ):
            st.session_state.mes_activo = m_num
            st.rerun()

nombre_mes_actual = meses_nombres[st.session_state.mes_activo - 1]
st.markdown(
    f"<h3 style='text-align: center; color: #8E44AD; margin-top: 10px;'>📖 Citas de {nombre_mes_actual}</h3>",
    unsafe_allow_html=True,
)

# Filtrar citas del mes seleccionado
citas_del_mes = [
    c
    for c in st.session_state.citas
    if c["fecha"].year == st.session_state.anio_activo
    and c["fecha"].month == st.session_state.mes_activo
]

# --- VISTA MÓVIL OPTIMIZADA: TARJETAS DIARIAS CLARAS Y GIGANTES ---
if not citas_del_mes:
    st.info(
        f"No hay citas anotadas para {nombre_mes_actual}. ¡Todo libre por ahora!"
    )
else:
    citas_ordenadas = sorted(citas_del_mes, key=lambda x: (x["fecha"], x["hora"]))
    for cita in citas_ordenadas:
        dia_ingles = cita["fecha"].strftime("%A")
        dia_espanol = dias_semana_es.get(dia_ingles, dia_ingles)
        fecha_str = f"{dia_espanol}, {cita['fecha'].day} de {nombre_mes_actual}"

        # Verificar si la hora está en la franja de almuerzo (12:00 PM - 4:00 PM)
        es_hora_almuerzo = False
        hora_str = cita["hora"]
        if any(
            h in hora_str for h in ["12:00", "01:00", "02:00", "03:00", "04:00"]
        ) and ("PM" in hora_str):
            es_hora_almuerzo = True

        aviso_almuerzo_html = ""
        if es_hora_almuerzo:
            aviso_almuerzo_html = '<div class="badge-almuerzo">🍽️ ¡Atención: Esta cita es en horario de comedor (12:00 PM - 4:00 PM)! No olvides almorzar.</div>'

        st.markdown(
            f"""
            <div class="tarjeta-dia-movil">
                <div style='font-size: 1.1rem; color: #7F8C8D; font-weight: bold;'>📅 {fecha_str}</div>
                <div style='font-size: 1.4rem; font-weight: bold; color: #2C3E50; margin-top: 4px;'>
                    ✍️ {cita['titulo']}
                </div>
                <div style='color: #34495E; margin-top: 4px; font-size: 1.2rem;'>
                    ⏰ Hora: <b>{cita['hora']}</b>
                </div>
                {aviso_almuerzo_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# --- FORMULARIO PARA ANOTAR NUEVA CITA ---
st.markdown(
    "<h3 style='color: #2C3E50;'>➕ Anotar Nueva Cita</h3>", unsafe_allow_html=True
)

with st.expander("📝 Toca aquí para registrar un evento nuevo"):
    with st.form("form_cita"):
        nuevo_titulo = st.text_input("¿Qué cita o evento tienes?")
        nueva_fecha = st.date_input("Fecha del evento:", value=hoy)
        nueva_hora = st.text_input("Hora (Ej: 10:00 AM o 02:00 PM):", value="02:00 PM")

        guardar = st.form_submit_button("Guardar en la Agenda")

        if guardar and nuevo_titulo:
            st.session_state.citas.append(
                {
                    "titulo": nuevo_titulo,
                    "fecha": nueva_fecha,
                    "hora": nueva_hora,
                }
            )
            st.session_state.mes_activo = nueva_fecha.month
            st.session_state.anio_activo = nueva_fecha.year
            st.success("¡Cita guardada con éxito!")
            st.rerun()
