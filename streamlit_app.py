import calendar
import datetime
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Agenda de Mamá", page_icon="📖", layout="centered"
)

# Estilos CSS estilo Google Calendar cálido y artesanal
st.markdown(
    """
    <style>
    .main {
        background-color: #F8F9FA;
    }
    h1 {
        color: #2C3E50;
        text-align: center;
        font-size: 2.6rem !important;
        font-weight: 800 !important;
        font-family: 'Georgia', serif;
    }
    .alerta-hoy {
        background-color: #FDEDEC;
        border-left: 10px solid #E74C3C;
        color: #922B21;
        padding: 18px;
        border-radius: 12px;
        font-size: 1.4rem;
        font-weight: bold;
        margin-bottom: 20px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.05);
    }
    .alerta-mañana {
        background-color: #FEF9E7;
        border-left: 10px solid #F1C40F;
        color: #7D6608;
        padding: 18px;
        border-radius: 12px;
        font-size: 1.4rem;
        font-weight: bold;
        margin-bottom: 20px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.05);
    }
    .tranquilo {
        background-color: #EAFAF1;
        border-left: 10px solid #2ECC71;
        color: #196F3D;
        padding: 18px;
        border-radius: 12px;
        font-size: 1.4rem;
        font-weight: bold;
        margin-bottom: 20px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.05);
    }
    /* Tarjeta de cita con recordatorio visual de almuerzo si aplica */
    .tarjeta-cita {
        background-color: #FFFFFF;
        border: 1px solid #E5E7E9;
        border-left: 8px solid #8E44AD;
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.04);
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
        font-size: 1.2rem !important;
    }
    .stButton>button {
        font-size: 1.2rem !important;
        padding: 10px 15px !important;
        border-radius: 10px !important;
        font-weight: bold !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Título principal
st.markdown("<h1>📖 Agenda de Mamá</h1>", unsafe_allow_html=True)

# Inicializar lista de citas en memoria
if "citas" not in st.session_state:
    st.session_state.citas = [
        {
            "titulo": "Control Médico General",
            "fecha": (datetime.date.today() + datetime.timedelta(days=1)),
            "hora": "10:00 AM",
        }
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
            🚨 ¡Atención! Tienes una cita para HOY:<br>
            📌 <b>{cita_hoy['titulo']}</b> a las <b>{cita_hoy['hora']}</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
elif cita_manana:
    st.markdown(
        f"""
        <div class="alerta-mañana">
            ⚠️ Atención: Mañana tienes una cita:<br>
            📌 <b>{cita_manana['titulo']}</b> a las <b>{cita_manana['hora']}</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        '<div class="tranquilo">✨ ¡Todo tranquilo por hoy! Disfruta tu día con calma. ✨</div>',
        unsafe_allow_html=True,
    )

st.divider()

# --- SELECTOR DE MESES (SOLO LOS MESES RESTANTES DEL AÑO EN CURSO) ---
st.markdown(
    "<h3 style='color: #2C3E50; text-align: center;'>🗓️ ¿Qué mes deseas consultar?</h3>",
    unsafe_allow_html=True,
)

# Filtrar solo desde el mes actual en adelante para el año actual
meses_disponibles = []
for m in range(hoy.month, 13):
    meses_disponibles.append((m, meses_nombres[m - 1]))

# Crear selector de meses en botones limpios verticales o en una sola fila organizada
cols_meses = st.columns(len(meses_disponibles))
for idx, (m_num, m_nombre) in enumerate(meses_disponibles):
    with cols_meses[idx]:
        if st.button(
            f"{m_nombre}",
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
    f"<h2 style='text-align: center; color: #8E44AD; margin-top: 20px;'>📖 Calendario de {nombre_mes_actual}</h2>",
    unsafe_allow_html=True,
)

# --- CUADRÍCULA VISUAL DEL MES (TIPO CALENDARIO CLARO) ---
cal = calendar.Calendar(firstweekday=6)  # Domingo primero
dias_mes = cal.monthdayscalendar(
    st.session_state.anio_activo, st.session_state.mes_activo
)

cols_dias = st.columns(7)
nombres_dias_cortos = ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"]
for idx, d_nombre in enumerate(nombres_dias_cortos):
    with cols_dias[idx]:
        st.markdown(
            f"<div style='text-align: center; font-weight: bold; color: #7F8C8D;'>{d_nombre}</div>",
            unsafe_allow_html=True,
        )

citas_del_mes = [
    c
    for c in st.session_state.citas
    if c["fecha"].year == st.session_state.anio_activo
    and c["fecha"].month == st.session_state.mes_activo
]

for semana in dias_mes:
    cols_semana = st.columns(7)
    for idx, dia in enumerate(semana):
        with cols_semana[idx]:
            if dia == 0:
                st.markdown(
                    "<div style='text-align: center; color: #E5E7E9; padding: 8px;'>-</div>",
                    unsafe_allow_html=True,
                )
            else:
                citas_en_dia = [
                    c for c in citas_del_mes if c["fecha"].day == dia
                ]
                if citas_en_dia:
                    num = len(citas_en_dia)
                    st.markdown(
                        f"""
                        <div style='background-color: #F3E5F5; border: 2px solid #8E44AD; border-radius: 8px; text-align: center; padding: 6px; margin-bottom: 4px;'>
                            <span style='color: #8E44AD; font-weight: bold;'>{dia}</span><br>
                            <span style='background-color: #8E44AD; color: white; border-radius: 8px; padding: 1px 5px; font-size: 0.8rem;'>📌 {num}</span>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        f"""
                        <div style='background-color: #FFFFFF; border: 1px solid #EAEDED; border-radius: 8px; text-align: center; padding: 8px; margin-bottom: 4px;'>
                            <span style='color: #5D6D7E;'>{dia}</span>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

st.divider()

# --- DETALLE DE CITAS CON MARCA CLARA DE ALMUERZO SI CAE EN ESA FRANJA ---
st.markdown(
    f"<h3 style='color: #2C3E50;'>📌 Tus Citas en {nombre_mes_actual}</h3>",
    unsafe_allow_html=True,
)

if not citas_del_mes:
    st.info(
        f"No hay citas anotadas para {nombre_mes_actual}. Todo libre por ahora."
    )
else:
    citas_ordenadas = sorted(citas_del_mes, key=lambda x: (x["fecha"], x["hora"]))
    for cita in citas_ordenadas:
        dia_ingles = cita["fecha"].strftime("%A")
        dia_espanol = dias_semana_es.get(dia_ingles, dia_ingles)
        fecha_str = f"{dia_espanol}, {cita['fecha'].day} de {nombre_mes_actual}"

        # Verificar si la hora está entre 12:00 PM y 4:00 PM para mostrar el recordatorio de almuerzo
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
            <div class="tarjeta-cita">
                <div style="font-size: 1.1rem; color: #7F8C8D; font-weight: bold;">📅 {fecha_str}</div>
                <div style="font-size: 1.5rem; font-weight: bold; color: #2C3E50; margin-top: 4px;">
                    ✍️ {cita['titulo']}
                </div>
                <div style="color: #34495E; margin-top: 4px; font-size: 1.2rem;">
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
        nueva_hora = st.text_input(
            "Hora (Ejemplo: 10:00 AM o 01:30 PM):", value="02:00 PM"
        )

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
