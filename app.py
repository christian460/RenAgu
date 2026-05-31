import streamlit as st
import base64
from streamlit_image_coordinates import streamlit_image_coordinates
from PIL import Image   

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
    padding: 25px;
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

</style>
""", unsafe_allow_html=True)

nav, logo = st.columns([5,1])

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

st.markdown("""
<div class="hero">
<h1>RENOVACIÓN AGUSTINA</h1>
<h3>Compromiso • Transparencia • Integridad</h3>
<p>Comprometidos con una universidad democrática, humana y de calidad.</p>
</div>
""", unsafe_allow_html=True)


if st.session_state["pagina"] is None:

    st.markdown("""
    ## Bienvenido a Renovación Agustina

    Seleccione una candidatura en la barra superior
    para conocer a nuestros candidatos.
    """)

elif st.session_state["pagina"] == "rector":

    col1, col2 = st.columns([1,2])

    with col1:
        st.image(
            "assets/Rector.png",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        <div class="perfil">
        <h2>Dr. Fernando Carlos Mejía Nova</h2>
        <h4>Candidato a Rector</h4>

        Profesional con amplia experiencia en gestión pública,
        liderazgo comunitario y desarrollo urbano.

        </div>
        """, unsafe_allow_html=True)

    st.subheader("Imágenes de campaña")


elif st.session_state["pagina"] == "academico":

    col1, col2 = st.columns([1,2])

    with col1:
        st.image(
            "assets/Vicerrector_academico.png",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        <div class="perfil">
        <h2>Dr. Ubaldo Enríquez Aguirre</h2>
        <h4>Candidato a Vicerrector Académico</h4>

        Defensor de la participación ciudadana,
        la transparencia y el desarrollo social.

        </div>
        """, unsafe_allow_html=True)

    st.subheader("Imágenes de campaña")


elif st.session_state["pagina"] == "investigacion":

    col1, col2 = st.columns([1,2])

    with col1:
        st.image(
            "assets/VicerrectorDeInvestigacion.png",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        <div class="perfil">
        <h2>Dr. José Luis Picoaga Chávez</h2>
        <h4>Candidato a Vicerrector de Investigación</h4>

        Especialista en planificación regional,
        infraestructura y desarrollo económico.

        </div>
        """, unsafe_allow_html=True)

    st.subheader("Imágenes de campaña")

st.markdown("---")

st.caption(
    "Publicidad política. Verifique y contraste la información antes de tomar decisiones electorales."
)