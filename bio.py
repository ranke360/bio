import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ranke 360°",
    layout="centered"
)

st.markdown("""
<style>
    /* Força cor branca para todos os textos da página */
    body, h1, h2, h3, h4, h5, h6, p, a, span, label, button, li, td, th, div {
        color: #ffffff !important;
    }
    header[data-testid="stHeader"] {
        display: none;
    }
    #MainMenu {
        visibility: hidden;
    }
    footer {
        visibility: hidden;
    }
    @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
    body {
        background-color: #0D47A1;
        font-family: 'iBrand', 'Montserrat', sans-serif;
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
    h1 {
        text-align: center;
        font-weight: 700;
        margin-bottom: 10px;
        /* cor já garantida pelo seletor geral */
    }
    h2.subtitle {
        text-align: center;
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 30px;
    }
    p.description {
        text-align: center;
        font-size: 0.9rem;
        line-height: 1.5;
        margin-bottom: 1.5rem;
    }
    h3 {
        text-align: center;
        font-size: 1.1rem;
        margin-top: 1.8rem;
        margin-bottom: 1rem;
        font-weight: 600;
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
    }
    .tabs-container {
        max-width: 480px;
        margin-left: auto;
        margin-right: auto;
        padding-bottom: 40px;
    }
    .tab-content-style {
        font-family: 'iBrand', 'Montserrat', sans-serif !important;
        font-size: 1rem !important;
        text-align: center !important;
    }
    .stTabs [role="tablist"] button[aria-selected="true"] {
        border-bottom: 3px solid #ffffff !important;
        font-weight: 700;
    }
    .stTabs [role="tablist"] button {
        border-bottom: 3px solid transparent;
        font-weight: 500;
        transition: border-color 0.3s ease;
        margin-right: 20px;
        font-size: 1rem !important;
        white-space: nowrap !important;
        overflow: visible !important;
        text-overflow: ellipsis;
        min-width: 90px;
    }
    .stTabs [role="tablist"] button:last-child {
        margin-right: 0;
    }
    .stTabs [role="tablist"] button:hover {
        border-bottom: 3px solid #bbbbbb;
        color: #bbbbbb !important;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# --- Resto do código segue normalmente, incluindo logo, textos, abas e iframes ---

st.markdown("""
<img src="https://lh3.googleusercontent.com/p/AF1QipNWXxW-WReAzeTIx8cX2HsuXkC_PII7f-Ff6KTa=w408-h408-k-no" alt="Ranke 360 Logo" class="logo" />
""", unsafe_allow_html=True)

st.markdown("""
<p class="description">Visibilidade Estratégica para Negócios</p>
<p class="description">DESTAQUE | POSICIONAMENTO | CLIENTES</p>
""", unsafe_allow_html=True)

links = {
    "Instagram": "https://www.instagram.com/ranke360",
    "YouTube": "https://www.youtube.com/@Ranke360",
    "WhatsApp": "https://wa.me/5588988385551",
    "Google Maps": "https://maps.app.goo.gl/pp57LioX2Uecsfwj6",
    "Blog Ranke 360°": "https://ranke360.streamlit.app"
}
for nome, url in links.items():
    st.markdown(f'<a class="link-button" href="{url}" target="_blank" rel="noopener noreferrer">{nome}</a>', unsafe_allow_html=True)

st.markdown('<div class="tabs-container">', unsafe_allow_html=True)

tab_img360, tab_tour, tab_video, tab_mapa, tab_exclusivo = st.tabs([
    "IMAGEM 360°",
    "TOUR VIRTUAL",
    "VÍDEO IMERSIVO",
    "MAPA",
    "360° EXCLUSIVO"
])

def embed_centered_iframe(src, width=480, height=450):
    html_code = f"""
    <div style="display: flex; justify-content: center; width: 100%; margin-bottom: 30px;">
        <iframe src="{src}" width="{width}" height="{height}" 
            style="border:0; border-radius: 12px;" allowfullscreen="" loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)

with tab_img360:
    st.markdown('<div class="tab-content-style">', unsafe_allow_html=True)

    st.markdown("<h3>Pitinininha Kids | Roupa infantil | Brejo Santo-CE</h3>", unsafe_allow_html=True)
    embed_centered_iframe("https://www.google.com/maps/embed?pb=!4v1753151196062!6m8!1m7!1sCAoSHENJQUJJaEI4OUxua0JvT1VoaklzY09CaWVUdEg.!2m2!1d-7.493140408761639!2d-38.98694109336261!3f297.8543782167756!4f-10.166367931658101!5f0.7820865974627469")

    # ... Repita embed_centered_iframe para as outras urls conforme seu código ...

    st.markdown('</div>', unsafe_allow_html=True)

with tab_tour:
    st.markdown('<div class="tab-content-style">', unsafe_allow_html=True)
    st.markdown("<h3>BFX Consultoria | Contabilidade | Brejo Santo-CE</h3>", unsafe_allow_html=True)
    embed_centered_iframe("https://www.google.com/maps/embed?pb=!4v1753197635440!6m8!1m7!1sCAoSHENJQUJJaEQtVk8yb1hxaHppRUVVdWxWQnZqMmU.!2m2!1d-7.490032784172747!2d-38.97943065124561!3f192.59282718210963!4f11.423489168813845!5f0.7820865974627469")
    st.markdown('</div>', unsafe_allow_html=True)

with tab_video:
    st.markdown('<div class="tab-content-style">', unsafe_allow_html=True)
    st.markdown("<h3>Skate Radical no Sol Escaldante: Vídeo Imersivo 360° com Ítalo Gomes | Ranke 360</h3>", unsafe_allow_html=True)
    components.iframe("https://www.youtube.com/embed/_wlmH5ync08?si=3Wo3AZumCWlpblW_", width=480, height=315, scrolling=False)
    st.markdown('</div>', unsafe_allow_html=True)

with tab_mapa:
    st.markdown('<div class="tab-content-style">', unsafe_allow_html=True)
    st.markdown("<!-- Conteúdo da aba MAPA - insira seu conteúdo aqui -->", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab_exclusivo:
    st.markdown('<div class="tab-content-style">', unsafe_allow_html=True)
    st.markdown("<!-- Conteúdo da aba 360° EXCLUSIVO - insira seu conteúdo aqui -->", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
