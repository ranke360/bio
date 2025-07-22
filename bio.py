import streamlit as st

st.set_page_config(
    page_title="Ranke 360°",
    layout="centered"
)

st.markdown("""
<style>
    /* Remove cabeçalho */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    /* Remove menu hambúrguer */
    #MainMenu {
        visibility: hidden !important;
    }
    /* Remove rodapé */
    footer {
        visibility: hidden !important;
    }
    /* Remove link <a> no topo (XPath /html/body/div/div[1]/div/div/a) */
    body > div > div:nth-child(1) > div > div > a {
        display: none !important;
    }
    /* Remove div no topo (XPath /html/body/div/div[1]/div/div/div) */
    body > div > div:nth-child(1) > div > div > div {
        display: none !important;
    }

    /* Seu CSS customizado */
    @font-face {
        font-weight: normal;
        font-style: normal;
    }
    @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

    body {
        background-color: #0D47A1;
        font-family: 'iBrand', 'Montserrat', sans-serif;
        color: #ffffff !important;
    }

    .container {
        max-width: 480px;
        margin: auto;
        padding: 30px 40px;
        background-color: #0D47A1;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(13, 71, 161, 0.15);
    }

    .logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 140px;
        height: 140px;
        margin-bottom: 25px;
        border-radius: 50%;
        object-fit: cover;
    }

    h1, h2.subtitle {
        color: #ffffff !important;
    }

    h1 {
        text-align: center;
        font-weight: 700;
        margin-bottom: 10px;
    }

    h2.subtitle {
        text-align: center;
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 30px;
    }

    p.description {
        text-align: center;
        color: #ffffff !important;
        font-size: 1rem;
        line-height: 1.5;
        margin-bottom: 40px;
    }

    a.link-button {
        display: block;
        text-align: center;
        background-color: #0D47A1;
        color: white !important;
        padding: 14px 0;
        margin: 12px 0;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        transition: background-color 0.3s ease;
        box-shadow: 0 3px 8px rgba(13,71,161,0.25);
    }
    a.link-button:hover {
        background-color: #1565C0;
        box-shadow: 0 5px 15px rgba(21,101,192,0.5);
        color: #ffffff !important;
    }

    .footer {
        margin-top: 50px;
        font-size: 0.85rem;
        color: #ffffff !important;
        text-align: center;
        line-height: 1.4;
    }
    .footer a {
        color: #ffffff !important;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }

    .tabs-container {
        max-width: 480px;
        margin-left: auto;
        margin-right: auto;
    }

    .tab-content-style {
        font-family: 'iBrand', 'Montserrat', sans-serif !important;
        color: #ffffff !important;
        font-size: 1rem !important;
        text-align: center !important;
    }

    /* Remove barra animada laranja da aba selecionada */
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: transparent !important;
    }

    /* Aba selecionada */
    .stTabs [role="tablist"] button[aria-selected="true"] {
        border-bottom: 3px solid #ffffff !important;
        color: #ffffff !important;
        font-weight: 700;
    }

    /* Abas não selecionadas */
    .stTabs [role="tablist"] button {
        border-bottom: 3px solid transparent;
        color: #ffffff !important;
        font-weight: 500;
        transition: border-color 0.3s ease;
        margin-right: 20px;
        font-size: 1rem !important;
        white-space: nowrap !important;         /* força texto em uma única linha */
        overflow: visible !important;
        text-overflow: ellipsis;
        min-width: 90px;
    }
    .stTabs [role="tablist"] button:last-child {
        margin-right: 0;
    }

    /* Hover nas abas */
    .stTabs [role="tablist"] button:hover {
        border-bottom: 3px solid #bbbbbb;
        color: #bbbbbb !important;
        cursor: pointer;
    }

    /* Fonte e estilo texto título das abas */
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1rem !important;
        margin: 0;
        white-space: nowrap !important;
        overflow: visible !important;
        text-overflow: ellipsis;
    }
</style>
""", unsafe_allow_html=True)

# Logo centralizada no topo
st.markdown("""
<img src="https://lh3.googleusercontent.com/p/AF1QipNWXxW-WReAzeTIx8cX2HsuXkC_PII7f-Ff6KTa=w408-h408-k-no" alt="Ranke 360 Logo" class="logo" />
""", unsafe_allow_html=True)

# Apresentação resumida
st.markdown("""
<p class="description">
Visibilidade Estratégica para Negócios
</p>
""", unsafe_allow_html=True)

# Apresentação resumida
st.markdown("""
<p class="description">
DESTAQUE | POSICIONAMENTO | CLIENTES
</p>
""", unsafe_allow_html=True)

# Links com botões estilizados
links = {
    "Instagram": "https://www.instagram.com/ranke360",
    "YouTube": "https://www.youtube.com/@Ranke360",
    "WhatsApp": "https://wa.me/5588988385551",
    "Google Maps": "https://maps.app.goo.gl/pp57LioX2Uecsfwj6",
    "Blog Ranke 360°": "https://ranke360.streamlit.app"
}

for nome, url in links.items():
    st.markdown(f'<a class="link-button" href="{url}" target="_blank" rel="noopener noreferrer">{nome}</a>', unsafe_allow_html=True)

# Container das abas centralizado e limitado
st.markdown('<div class="tabs-container">', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "VÍDEO IMERSIVO",
    "IMAGEM 360°",
    "TOUR VIRTUAL",
    "MAP",
    "360° EXCLUSIVO",
    "SOBRE"
])

with tab1:
    st.markdown("""
    <div class="tab-content-style">
    <h3 style="font-size: 1.1rem;">
        Skate Radical no Sol Escaldante: Vídeo Imersivo 360° com Ítalo Gomes | Ranke 360
    </h3>
    <iframe width="100%" height="315" src="https://www.youtube.com/embed/_wlmH5ync08?si=3Wo3AZumCWlpblW_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="tab-content-style">
    <h3>Quadra de Basquete | Brejo Santo-CE</h3>
    <iframe src="https://www.google.com/maps/embed?pb=!4v1753150711289!6m8!1m7!1sCAoSHENJQUJJaERnaG1mQmpPOEpHZk9LYnNWUmlQaXM.!2m2!1d-7.484971799999999!2d-38.9860056!3f195.21!4f-0.5600000000000023!5f0.4000000000000002" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>

    <h3>Ginásio Poliesportivo Welingtão | Brejo Santo-CE</h3>
    <iframe src="https://www.google.com/maps/embed?pb=!4v1753150938298!6m8!1m7!1sCAoSHENJQUJJaEQwY09MVkRONG5ic1VnamQtTkw0SV8.!2m2!1d-7.489376802708099!2d-38.9901219288986!3f190.74911673396883!4f3.1483665025552057!5f0.7820865974627469" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>

    <h3>Pitinininha Kids | Roupa infantil | Brejo Santo-CE</h3>
    <iframe src="https://www.google.com/maps/embed?pb=!4v1753151196062!6m8!1m7!1sCAoSHENJQUJJaEI4OUxua0JvT1VoaklzY09CaWVUdEg.!2m2!1d-7.493140408761639!2d-38.98694109336261!3f297.8543782167756!4f-10.166367931658101!5f0.7820865974627469" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>

    <h3>Next Level | Academia | Brejo Santo-CE</h3>
    <iframe src="https://www.google.com/maps/embed?pb=!4v1753151300722!6m8!1m7!1sCAoSHENJQUJJaENabnYta1NIYnk3U0VTZXg2cVZFSUQ.!2m2!1d-7.486728599999999!2d-38.9976357!3f14.212028543852037!4f-10.245711121253734!5f0.7820865974627469" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>

    <h3>Next Level | Academia | Cajazeiras - PB</h3>
    <iframe src="https://www.google.com/maps/embed?pb=!4v1753180786706!6m8!1m7!1sCAoSHENJQUJJaEFxQUtEOWxMaEdRekpiYk5SbGEzeGc.!2m2!1d-6.887891776224389!2d-38.55972383357095!3f1.520990456891578!4f-30.982226239046547!5f0.4000000000000002" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div class="tab-content-style">
    <h3>BFX Consultoria | Contabilidade | Brejo Santo-CE</h3>
    <iframe src="https://www.google.com/maps/embed?pb=!4v1753197635440!6m8!1m7!1sCAoSHENJQUJJaEQtVk8yb1hxaHppRUVVdWxWQnZqMmU.!2m2!1d-7.490032784172747!2d-38.97943065124561!3f192.59282718210963!4f11.423489168813845!5f0.7820865974627469" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.markdown("""
    <div class="tab-content-style">
    </div>
    """, unsafe_allow_html=True)

with tab5:
    st.markdown("""
    <div class="tab-content-style">
    </div>
    """, unsafe_allow_html=True)

with tab6:
    st.markdown("""
    <div class="tab-content-style">
    </div>
    """, unsafe_allow_html=True)
