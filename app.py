import streamlit as st
import base64

def get_base64(imagen):
    with open(imagen, "rb") as f:
        return base64.b64encode(f.read()).decode()

banner = get_base64("assets/Banner.png")

st.set_page_config(
    page_title="Partido Político",
    page_icon="🗳️",
    layout="wide"
)

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

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>RENOVACIÓN AGUSTINA</h1>
<h3>Compromiso • Transparencia • Integridad</h3>
<p>Comprometidos con una universidad democrática, humana y de calidad.</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs([
    "🎓 Rector",
    "📚 Vicerrector Académico",
    "🔬 Vicerrector de Investigación"
])

with tab1:

    col1, col2 = st.columns([1,2])

    with col1:
        st.image(
            "assets/Rector.png",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        <div class="perfil">
        <h2>Dr. Fernado Carlos Mejía Nova</h2>
        <h4>Candidato a Rector</h4>

        Profesional con amplia experiencia en gestión pública,
        liderazgo comunitario y desarrollo urbano.

        </div>
        """, unsafe_allow_html=True)


    st.subheader("Imagenes de campaña")


with tab2:

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


    st.subheader("Imagenes de campaña")


with tab3:

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

    st.subheader("Imagenes de campaña")

st.markdown("---")

st.caption(
    "Publicidad política. Verifique y contraste la información antes de tomar decisiones electorales."
)