import streamlit as st
import base64
from streamlit_image_coordinates import streamlit_image_coordinates
from PIL import Image
from pathlib import Path
import streamlit.components.v1 as components

from components.flipbook import render_flipbook_desde_carpeta


def get_base64(imagen):
    with open(imagen, "rb") as f:
        return base64.b64encode(f.read()).decode()

banner = get_base64("assets/Banner.png")

st.set_page_config(
    page_title="Partido Político",
    page_icon="🗳️",
    layout="wide"
)

if "pagina" not in st.session_state:
    st.session_state["pagina"] = None

if "logo_click" not in st.session_state:
    st.session_state["logo_click"] = None

st.markdown(f"""
<style>

.main {{
    background-color: #f5f7fa;
}}

.hero {{
    background-image:
        linear-gradient(
            rgba(0,0,0,0.45),
            rgba(0,0,0,0.45)
        ),
        url("data:image/png;base64,{banner}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

    padding: 120px 40px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 20px;
}}

[data-theme="light"] .propuesta {{
    background: white;
    color: black;
}}

[data-theme="dark"] .propuesta {{
    background: #262730;
    color: white;
}}

.propuesta {{
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
    border-left: 5px solid #1976d2;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}}

[data-theme="light"] .perfil {{
    background: white;
    color: black;
}}

[data-theme="dark"] .perfil {{
    background: #262730;
    color: white;
}}

.perfil {{
    padding: 5px;
    border-radius: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
}}

.redes a {{
    text-decoration: none;
    margin-right: 15px;
    font-weight: bold;
}}

.nav-button button {{
    width: 100%;
    height: 55px;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
}}

div.stButton > button {{
    margin-top: 20px;
    width: 100%;
    height: 50px;

    border: none;
    border-bottom: 3px solid transparent;

    border-radius: 8px 8px 0 0;

    background: transparent;

    font-size: 16px;
    font-weight: 600;

    transition: all 0.2s ease;
}}

div.stButton > button:hover {{
    background-color: rgba(128,128,128,0.1);
}}

div.stButton > button:focus {{
    border-bottom: 3px solid #1976d2;
}}

div.stButton > button[kind="secondary"] {{
    border-radius: 10px;
}}

.galeria-img {{
    overflow: hidden;
    border-radius: 15px;
    margin-bottom: 15px;
}}

.galeria-img img {{
    width: 100%;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
    transition: transform 0.3s ease;
}}

.galeria-img img:hover {{
    transform: scale(1.05);
}}

button[kind="secondary"] {{
    font-size: 22px !important;
    font-weight: bold !important;
}}

.flipbook-container {{
    perspective: 1500px;
    margin-top: 20px;
}}

.flipbook-page {{
    background: white;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);

    animation: flipIn .6s ease;
}}

@keyframes flipIn {{
    from {{
        opacity: 0;
        transform:
            rotateY(-25deg)
            translateX(60px);
    }}

    to {{
        opacity: 1;
        transform:
            rotateY(0deg)
            translateX(0px);
    }}
}}

.flip-grid {{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:15px;
}}

.flip-grid img {{
    width:100%;
    border-radius:12px;

    transition:all .3s ease;
}}

.flip-grid img:hover {{
    transform:scale(1.05);
    box-shadow:0 8px 20px rgba(0,0,0,.25);
}}

.flipbook-img img {{
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}}

.flipbook-titulo {{
    text-align:center;
    font-size:32px;
    font-weight:bold;
    margin-bottom:10px;
}}

.flipbook-pagina {{
    text-align:center;
    color:#1976d2;
    font-size:18px;
    margin-bottom:15px;
}}

@keyframes slidePage {{
    from {{
        opacity:0;
        transform:translateX(80px);
    }}

    to {{
        opacity:1;
        transform:translateX(0);
    }}
}}

</style>
""", unsafe_allow_html=True)

nav, espacio, logo = st.columns([5, 0.3, 0.7])

with nav:

    b1, b2, b3 = st.columns(3)

    with b1:
        if st.button("🎓 Rector", use_container_width=True):
            st.session_state["pagina"] = "rector"

    with b2:
        if st.button("📚 Vicerrector Académico", use_container_width=True):
            st.session_state["pagina"] = "academico"

    with b3:
        if st.button("🔬 Vicerrector de Investigación", use_container_width=True):
            st.session_state["pagina"] = "investigacion"

with logo:
    
    img = Image.open("assets/logo.png")
    img = img.resize((80, 80))

    click = streamlit_image_coordinates(
        img,
        key="logo_inicio"
    )

    if (
        click is not None
        and click != st.session_state["logo_click"]
    ):
        st.session_state["logo_click"] = click
        st.session_state["pagina"] = None
        st.rerun()


st.image(
            "assets/Banner_2.jpeg",
            use_container_width=True
        )

st.markdown("""
<div class="hero">
<h1>RENOVACIÓN AGUSTINA</h1>
<h3>Compromiso • Transparencia • Integridad</h3>
<p>Comprometidos con una universidad democrática, humana y de calidad.</p>
</div>
""", unsafe_allow_html=True)


if st.session_state["pagina"] is None:

    col1, col2 = st.columns([1,2])

    with col1:
        st.image(
            "assets/Candidatos.jpeg",
            width=350
        )

    with col2:
        st.markdown("""
        <div class="perfil">
        <h2>Candidatos</h2>

        - Dr. Fernando Carlos Mejía Nova - Candidato a Rector
        - Dr. Ubaldo Enríquez Aguirre - Candidato a Vicerrector Académico
        - Dr. José Luis Picoaga Chávez - Candidato a Vicerrector de Investigación

        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("Video de Presentación")
    st.video("assets/Videos/2. video_presentacion_candidatos.mp4")
    
    st.markdown("---")

    st.subheader("📷 Álbumes de Campaña")
    CATEGORIAS = [
        {"carpeta": "assets/PresentacionCandidatos", "titulo": "📸 Presentación de Candidatos"},
        {"carpeta": "assets/PresentacionCandidatos/RecorridoUni_08_06_26", "titulo": "📸 Recorrido de los Candidatos por la UNSA"},
        {"carpeta": "assets/PresentacionCandidatos/RecorridoUni_17_06_26", "titulo": "📸 Recorrido de los Candidatos por la UNSA - 17/06/26"},
    ]

    for cat in CATEGORIAS:
        html = render_flipbook_desde_carpeta(cat["carpeta"], cat["titulo"])
        if html:
            components.html(html, height=700, scrolling=False)

    st.markdown("---")


elif st.session_state["pagina"] == "rector":

    col1, col2 = st.columns([1, 2])

    with col1:

        st.image(
            "assets/Rector.jpg",
            width=330
        )

    with col2:
        st.markdown("""
        <div class="perfil">
        <h1>Dr. Fernando Carlos Mejía Nova</h1>
        <h3>Candidato a Rector</h3>
        <div style="text-align: justify;">
        Más de 34 años de experiencia docente universitaria,
        comprometido con la excelencia académica, la investigación
        y la modernización institucional de la Universidad Nacional
        de San Agustín.
        </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

        with st.expander("🎓 Formación Académica", expanded=True):
            st.markdown("""
            - Doctor en Ciencias: Ingeniería de Producción (UNSA)
            - Magíster en Ingeniería Industrial, mención Marketing (UNSA)
            - Ingeniero en Industrias Alimentarias
            """)

        with st.expander("👨‍🏫 Trayectoria Universitaria"):
            st.markdown("""
            - Más de 34 años de experiencia docente universitaria.
            - Docente en la UNSA desde 1993.
            - Experiencia en formación profesional, investigación y gestión académica.
            """)

        with st.expander("🏛️ Gestión Universitaria"):
            st.markdown("""
            - Director de la Escuela Profesional de Ingeniería de Industrias Alimentarias (2016–2019).
            - Responsable del proceso de acreditación de la Escuela.
            - Director Encargado del Departamento Académico de Industrias Alimentarias (2024–2025).
            - Impulsor de la modernización e implementación de laboratorios.
            """)

        with st.expander("🔬 Investigación e Innovación"):
            st.markdown("""
            - Publicaciones científicas indexadas en Scopus.
            - Investigador y gestor de proyectos financiados por UNSA Investiga.
            - Experiencia en innovación tecnológica y desarrollo agroindustrial.
            """)

        with st.expander("🤝 Compromiso con la UNSA"):
            st.markdown("""
            - Más de tres décadas de servicio institucional.
            - Participación activa en órganos de gobierno universitario.
            - Promotor de una universidad moderna, transparente, innovadora e internacionalizada.
            """)

        with st.expander("🌎 Nuestra Visión"):
            st.markdown("""
            <div style="text-align: justify;padding-bottom: 10px;">
            Una UNSA con excelencia académica, investigación de impacto,
            transparencia, bienestar universitario e internacionalización
            al servicio del desarrollo de Arequipa y del Perú.
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("Imágenes de campaña")

    html_rector = render_flipbook_desde_carpeta(
        "assets/PresentacionCandidatos/Rector",
        "📖 Candidato a Rector",
        imgs_por_pagina=6
    )

    if html_rector:
        components.html(
            html_rector,
            height=700,
            scrolling=False
        )
    
    st.markdown("---")
    
    st.subheader("Mensaje del candidato")

    st.markdown("---")


elif st.session_state["pagina"] == "academico":

    col1, col2 = st.columns([1,2])

    with col1:
        st.image(
            "assets/Vicerrector_Academico.jpeg",
            width=330
        )

    with col2:
        st.markdown("""
        <div class="perfil">
        <h2>Dr. Ubaldo Enríquez Aguirre</h2>
        <h4>Candidato a Vicerrector Académico</h4>
        <div style="text-align: justify;">
        Más de 30 años de trayectoria universitaria en docencia,
        gestión académica e investigación. Lingüista, abogado,
        magíster en Educación Superior y doctor en Ciencias Sociales,
        comprometido con la calidad educativa y el fortalecimiento
        académico de la Universidad Nacional de San Agustín.
        </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        with st.expander("🎓 Formación Académica", expanded=True):
            st.markdown("""
            - Doctor en Ciencias Sociales (UNSA).
            - Magíster en Educación Superior (UCSM).
            - Licenciado en Literatura y Lingüística (UNSA).
            - Abogado por la Universidad Andina Néstor Cáceres Velásquez.
            """)

        with st.expander("👨‍🏫 Trayectoria Universitaria"):
            st.markdown("""
            - Más de 30 años de experiencia docente universitaria.
            - Docente Principal de la UNSA.
            - Ex docente de la Universidad Nacional del Altiplano.
            - Experiencia en pregrado y posgrado.
            """)

        with st.expander("🏛️ Gestión Académica"):
            st.markdown("""
            - Director del Departamento Académico de Literatura y Lingüística.
            - Ex Director de la Escuela Profesional de Literatura y Lingüística.
            - Ex Director de la Unidad de Posgrado de la Facultad de Filosofía y Humanidades.
            - Miembro del Tribunal de Honor Universitario.
            """)

        with st.expander("📚 Investigación y Producción Intelectual"):
            st.markdown("""
            - Autor de libros sobre comunicación, redacción y derecho.
            - Ganador de concursos de publicación académica de UNSA Investiga.
            - Asesor de tesis de maestría y segunda especialidad.
            - Ponente en congresos y seminarios nacionales e internacionales.
            """)

        with st.expander("🏆 Reconocimientos"):
            st.markdown("""
            - Distinciones por investigación y producción académica.
            - Reconocimientos como ponente y organizador de eventos científicos.
            - Participación destacada en proyectos educativos y de formación docente.
            """)

        with st.expander("🌎 Nuestra Visión"):
            st.markdown("""
            <div style="text-align: justify;padding-bottom: 10px;">
            Impulsar una formación académica de excelencia,
            fortaleciendo la investigación, la innovación,
            la internacionalización y el desarrollo integral
            de los estudiantes de la Universidad Nacional de San Agustín.
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("Imágenes de campaña")

    st.markdown("---")

    st.subheader("Mensaje del candidato")

    st.markdown("---")


elif st.session_state["pagina"] == "investigacion":

    col1, col2 = st.columns([1,2])

    with col1:
        st.image(
            "assets/Vicerrector_De_Investigacion.jpeg",
            width=330
        )

    with col2:
        st.markdown("""
        <div class="perfil">
        <h2>Dr. José Luis Picoaga Chávez</h2>
        <h4>Candidato a Vicerrector de Investigación</h4>
        <div style="text-align: justify;">
        Médico oncólogo con una destacada trayectoria en docencia,
        investigación, gestión universitaria y desarrollo de servicios
        especializados de salud. Reconocido por su liderazgo académico
        y su aporte al fortalecimiento de la investigación científica
        y médica en el sur del país.
        </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        with st.expander("🎓 Formación Académica", expanded=True):
            st.markdown("""
            - Doctor en Ciencias: Medicina (Suma Cum Laude).
            - Magíster en Ciencias: Medicina (Suma Cum Laude).
            - Especialista en Oncología Médica.
            - Formación especializada en el Hospital de Oncología de México.
            """)

        with st.expander("👨‍🏫 Trayectoria Académica"):
            st.markdown("""
            - Formado en el Colegio San Francisco de Asís durante 11 años.
            - Docente de la misma institución durante 11 años.
            - Amplia experiencia en formación universitaria y médica.
            - Compromiso permanente con la excelencia académica.
            """)

        with st.expander("🏛️ Gestión Universitaria y Liderazgo"):
            st.markdown("""
            - Jefe del Departamento Académico de Medicina en tres periodos consecutivos.
            - Primer Gerente y fundador del Instituto Regional de Enfermedades Neoplásicas del Sur (IREN Sur).
            - Impulsor del fortalecimiento institucional y de la investigación médica.
            """)

        with st.expander("🔬 Investigación e Innovación"):
            st.markdown("""
            - Autor de más de 150 trabajos científicos presentados en eventos académicos.
            - Expositor, organizador y participante en más de 200 congresos y encuentros científicos nacionales e internacionales.
            - Promotor de la investigación científica aplicada a la salud y al desarrollo regional.
            """)

        with st.expander("🏥 Aporte al Sistema de Salud"):
            st.markdown("""
            - Médico fundador del Servicio de Oncología Médica del Hospital Nacional CASE de EsSalud Arequipa.
            - Consultor Ad Honorem en Oncología del Hospital Honorio Delgado por más de 28 años.
            - Contribución permanente a la atención especializada y la formación médica.
            """)

        with st.expander("🏅 Reconocimientos y Distinciones"):
            st.markdown("""
            - Académico de Número de la Academia Nacional de Medicina del Perú.
            - Miembro titular, fundador o directivo de diversas sociedades científicas.
            - Medalla y Diploma de Honor al Mérito del Colegio Médico del Perú.
            - Distinción por su labor educativa, científica y asistencial en beneficio de la salud pública.
            """)

        with st.expander("🌎 Nuestra Visión"):
            st.markdown("""
            <div style="text-align: justify;padding-bottom: 10px;">
            Consolidar una UNSA líder en investigación,
            innovación y transferencia del conocimiento,
            fortaleciendo la producción científica, la
            internacionalización y el impacto de la universidad
            en el desarrollo de Arequipa y del Perú.
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("Imágenes de campaña")

    html_rector = render_flipbook_desde_carpeta(
        "assets/PresentacionCandidatos/ViceRectorInv",
        "📖 Candidato a Vicerrector de Investigación",
        imgs_por_pagina=6
    )

    if html_rector:
        components.html(
            html_rector,
            height=700,
            scrolling=False
        )

    st.markdown("---")

    st.subheader("Mensaje del candidato")

    st.markdown("---")