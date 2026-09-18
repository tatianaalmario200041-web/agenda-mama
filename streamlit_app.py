import calendar
import datetime
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Agenda de Mamá", page_icon="📖", layout="centered"
)

# Estilos CSS avanzados: Cuaderno artesanal, cuadrícula de calendario y tarjetas de meses
st.markdown(
    """
    <style>
    .main {
        background-color: #FDFEFE;
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
        font-size: 1.5rem;
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
        font-size: 1.5rem;
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
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    }
    .comedor-info {
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
        border: 1px solid #E5E7E9;
        border-left: 8px solid #8E44AD;
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 12px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.04);
    }
    .badge-fecha {
        background-color: #8E44AD;
        color: white;
        padding: 5px 12px;
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

# Configuración de meses y días en español
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

# --- AVISO INFORMATIVO DEL COMEDOR ---
st.markdown(
    """
    <div class="comedor-info">
        <b>🍽️ Horario del Comedor:</b> Puedes asistir al comedor flexiblemente entre las <b>12:00 PM y las 4:00 PM</b>. 
        *(Ten en cuenta este espacio al programar citas nuevas).*
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# --- SELECTOR DE MESES POR TARJETAS / BOTONES (TODOS LOS MESES) ---
st.markdown(
    "<h3 style='color: #2C3E50; text-align: center;'>🗓️ Selecciona el Mes a Consultar</h3>",
    unsafe_allow_html=True,
)

# Creamos una botonera visual organizada en columnas para los 12 meses
cols_meses_1 = st.columns(6)
cols_meses_2 = st.columns(6)

for i in range(1, 7):
    with cols_meses_1[i - 1]:
        nombre_corto = meses_nombres[i - 1][:3]
        if st.button(
            f"{nombre_corto}",
            key=f"mes_{i}",
            use_container_width=True,
            type=(
                "primary" if st.session_state.mes_activo == i else "secondary"
            ),
        ):
            st.session_state.mes_activo = i
            st.rerun()

for i in range(7, 13):
    with cols_meses_2[i - 7]:
        nombre_corto = meses_nombres[i - 1][:3]
        if st.button(
            f"{nombre_corto}",
            key=f"mes_{i}",
            use_container_width=True,
            type=(
                "primary" if st.session_state.mes_activo == i else "secondary"
            ),
        ):
            st.session_state.mes_activo = i
            st.rerun()

nombre_mes_actual = meses_nombres[st.session_state.mes_activo - 1]
st.markdown(
    f"<h2 style='text-align: center; color: #8E44AD; margin-top: 15px;'>📖 Apuntes de {nombre_mes_actual} de {st.session_state.anio_activo}</h2>",
    unsafe_allow_html=True,
)

st.divider()

# --- VISTA TIPO CALENDARIO VISUAL EN CUADRÍCULA (MATRIZ DE DÍAS) ---
st.markdown(
    "<h4 style='color: #34495E;'>📅 Cuadrícula del Mes (Estilo Libreta)</h4>",
    unsafe_allow_html=True,
)

# Generar matriz del mes calendario (Domingo a Sábado)
cal = calendar.Calendar(firstweekday=6)  # 6 = Domingo como primer día
dias_mes = cal.monthdayscalendar(
    st.session_state.anio_activo, st.session_state.mes_activo
)

# Encabezados de los días de la semana
cols_dias = st.columns(7)
nombres_dias_cortos = ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"]
for idx, d_nombre in enumerate(nombres_dias_cortos):
    with cols_dias[idx]:
        st.markdown(
            f"<div style='text-align: center; font-weight: bold; color: #7F8C8D; font-size: 1rem;'>{d_nombre}</div>",
            unsafe_allow_html=True,
        )

# Mapear citas del mes activo por día
citas_del_mes = [
    c
    for c in st.session_state.citas
    if c["fecha"].year == st.session_state.anio_activo
    and c["fecha"].month == st.session_state.mes_activo
]

# Dibujar la cuadrícula de días con indicador de citas múltiples
for semana in dias_mes:
    cols_semana = st.columns(7)
    for idx, dia in enumerate(semana):
        with cols_semana[idx]:
            if dia == 0:
                st.markdown(
                    "<div style='text-align: center; color: #BDC3C7; padding: 10px;'>-</div>",
                    unsafe_allow_html=True,
                )
            else:
                # Verificar si este día tiene citas
                citas_en_dia = [
                    c for c in citas_del_mes if c["fecha"].day == dia
                ]
                if citas_en_dia:
                    num_citas = len(citas_en_dia)
                    # Día marcado con color especial porque tiene citas acumuladas
                    st.markdown(
                        f"""
                        <div style='background-color: #F5EEF8; border: 2px solid #8E44AD; border-radius: 8px; text-align: center; padding: 6px; margin-bottom: 5px;'>
                            <span style='color: #8E44AD; font-weight: bold; font-size: 1.1rem;'>{dia}</span><br>
                            <span style='background-color: #8E44AD; color: white; border-radius: 10px; padding: 1px 6px; font-size: 0.85rem;'>📌 {num_citas} cita(s)</span>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        f"""
                        <div style='background-color: #FFFFFF; border: 1px solid #EAEDED; border-radius: 8px; text-align: center; padding: 8px; margin-bottom: 5px;'>
                            <span style='color: #5D6D7E; font-size: 1.1rem;'>{dia}</span>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

st.divider()

# --- TARJETAS DETALLADAS DE CITAS (CON HORA Y MÚLTIPLES CITAS CLARAS) ---
st.markdown(
    f"<h3 style='color: #2C3E50;'>📝 Detalle de Citas Registradas en {nombre_mes_actual}</h3>",
    unsafe_allow_html=True,
)

if not citas_del_mes:
    st.info(
        f"No hay citas ni eventos anotados para {nombre_mes_actual} de {st.session_state.anio_activo}."
    )
else:
    citas_ordenadas = sorted(citas_del_mes, key=lambda x: (x["fecha"], x["hora"]))
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

# --- ASISTENTE PARA ANOTAR NUEVA CITA ---
st.markdown(
    "<h3 style='color: #2C3E50;'>➕ Anotar Nueva Cita en la Libreta</h3>",
    unsafe_allow_html=True,
)

with st.expander("📝 Abrir formulario para registrar un evento nuevo"):
    with st.form("form_cita"):
        nuevo_titulo = st.text_input("¿Qué evento o cita se va a programar?")
        nueva_fecha = st.date_input("Fecha exacta del evento:", value=hoy)

        st.markdown("---")
        st.markdown(
            "**Verificador de Horas:** Selecciona la hora. *(Recuerda que el comedor está disponible de 12:00 PM a 4:00 PM)*"
        )

        horarios_disponibles = [
            "08:00 AM",
            "09:00 AM",
            "10:00 AM",
            "11:00 AM",
            "12:00 PM (🍽️ Horario de Comedor)",
            "01:00 PM (🍽️ Horario de Comedor)",
            "02:00 PM (🍽️ Horario de Comedor)",
            "03:00 PM (🍽️ Horario de Comedor)",
            "04:00 PM",
            "05:00 PM",
            "06:00 PM",
        ]
        nueva_hora = st.selectbox(
            "Selecciona la hora de la cita:", horarios_disponibles
        )

        guardar = st.form_submit_button("Guardar Apunte en la Libreta")

        if guardar and nuevo_titulo:
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
            st.success("¡Cita anotada con éxito y marcada en el calendario!")
            st.rerun()
