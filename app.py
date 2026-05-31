import streamlit as st

st.set_page_config(
    page_title="Partido Político",
    page_icon="🗳️",
    layout="wide"
)

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.hero {
    background: linear-gradient(135deg,#0d47a1,#1976d2);
    padding: 40px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 20px;
}

.propuesta {
    background: white;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
    border-left: 5px solid #1976d2;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}

.perfil {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
}

.redes a {
    text-decoration: none;
    margin-right: 15px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>RENOVACIÓN AGUSTINA</h1>
<h3>Compromiso • Transparencia • Calidad</h3>
<p>Conoce a nuestros candidatos y propuestas para transformar nuestra universidad.</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs([
    "🏛️ Rector",
    "🤝 Vicerrector Académico",
    "🌎 Vicerrector de Investigación"
])

with tab1:

    col1, col2 = st.columns([1,2])

    with col1:
        st.image(
            "assets/candidato1.jpg",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        <div class="perfil">
        <h2>Juan Pérez</h2>
        <h4>Candidato a Alcalde</h4>

        Profesional con amplia experiencia en gestión pública,
        liderazgo comunitario y desarrollo urbano.

        </div>
        """, unsafe_allow_html=True)

    st.subheader("Principales Propuestas")

    propuestas = [
        "Mejoramiento integral de vías urbanas.",
        "Mayor seguridad ciudadana.",
        "Impulso al empleo juvenil.",
        "Modernización de servicios municipales.",
        "Recuperación de espacios públicos."
    ]

    for p in propuestas:
        st.markdown(
            f'<div class="propuesta">✅ {p}</div>',
            unsafe_allow_html=True
        )

    st.subheader("Mensaje del candidato")

    st.video(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    )

with tab2:

    col1, col2 = st.columns([1,2])

    with col1:
        st.image(
            "assets/candidato2.jpg",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        <div class="perfil">
        <h2>María Torres</h2>
        <h4>Candidata a Regidora</h4>

        Defensora de la participación ciudadana,
        la transparencia y el desarrollo social.

        </div>
        """, unsafe_allow_html=True)

    st.subheader("Principales Propuestas")

    propuestas = [
        "Fiscalización eficiente.",
        "Programas para mujeres emprendedoras.",
        "Impulso a actividades culturales.",
        "Mayor transparencia municipal.",
        "Promoción del deporte."
    ]

    for p in propuestas:
        st.markdown(
            f'<div class="propuesta">✅ {p}</div>',
            unsafe_allow_html=True
        )

    st.subheader("Mensaje de la candidata")

    st.video(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    )

with tab3:

    col1, col2 = st.columns([1,2])

    with col1:
        st.image(
            "assets/candidato3.jpg",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        <div class="perfil">
        <h2>Carlos Ramos</h2>
        <h4>Candidato a Consejero Regional</h4>

        Especialista en planificación regional,
        infraestructura y desarrollo económico.

        </div>
        """, unsafe_allow_html=True)

    st.subheader("Principales Propuestas")

    propuestas = [
        "Impulso al turismo regional.",
        "Mejora de infraestructura vial.",
        "Fortalecimiento de la educación.",
        "Proyectos de agua y saneamiento.",
        "Promoción de inversiones."
    ]

    for p in propuestas:
        st.markdown(
            f'<div class="propuesta">✅ {p}</div>',
            unsafe_allow_html=True
        )

    st.subheader("Mensaje del candidato")

    st.video(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    )

st.divider()

st.header("📞 Contacto del Partido")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📧 contacto@partido.com")

with col2:
    st.info("📱 +51 999 999 999")

with col3:
    st.info("📍 Dirección de campaña")

st.markdown("---")

st.caption(
    "Publicidad política. Verifique y contraste la información antes de tomar decisiones electorales."
)