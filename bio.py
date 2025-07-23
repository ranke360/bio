import streamlit as st
import streamlit.components.v1 as components  # Import necessário para vídeo YouTube

st.set_page_config(
    page_title="Ranke 360°",
    layout="centered"
)

# CSS global com cor branca para todas as fontes, títulos menores e alinhamento central, e remoção da barra laranja das abas
st.markdown("""
<style>
    /* Forçar cor branca para todos os textos */
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
    /* Remover barra laranja animada da aba selecionada */
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: transparent !important;
    }
    /* Aba selecionada: somente border-bottom branca */
    .stTabs [role="tablist"] button[aria-selected="true"] {
        border-bottom: 3px solid #ffffff !important;
        background-color: transparent !important;
        color: #ffffff !important;
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
        color: #ffffff !important;
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

# Logo centralizada
st.markdown("""
<img src="https://lh3.googleusercontent.com/p/AF1QipNWXxW-WReAzeTIx8cX2HsuXkC_PII7f-Ff6KTa=w408-h408-k-no" alt="Ranke 360 Logo" class="logo" />
""", unsafe_allow_html=True)

# Textos de apresentação
st.markdown("""
<p class="description">Visibilidade Estratégica para Negócios</p>
<p class="description">DESTAQUE | POSICIONAMENTO | CLIENTES</p>
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

# Container das abas
st.markdown('<div class="tabs-container">', unsafe_allow_html=True)

tab_img360, tab_tour, tab_video, tab_mapa, tab_exclusivo = st.tabs([
    "IMAGEM 360°",
    "TOUR VIRTUAL",
    "VÍDEO IMERSIVO",
    "MAPA",
    "360° EXCLUSIVO"
])

def embed_centered_iframe(src, width=480, height=450):
    html_code = f'''
    <div style="display: flex; justify-content: center; width: 100%; margin-bottom: 30px;">
        <iframe src="{src}" width="{width}" height="{height}" style="border:0; border-radius: 12px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
    '''
    st.markdown(html_code, unsafe_allow_html=True)

with tab_img360:
    st.markdown('<div class="tab-content-style">', unsafe_allow_html=True)

    st.markdown("<h3>Pitinininha Kids | Roupa infantil | Brejo Santo-CE</h3>", unsafe_allow_html=True)
    embed_centered_iframe("https://www.google.com/maps/embed?pb=!4v1753151196062!6m8!1m7!1sCAoSHENJQUJJaEI4OUxua0JvT1VoaklzY09CaWVUdEg.!2m2!1d-7.493140408761639!2d-38.98694109336261!3f297.8543782167756!4f-10.166367931658101!5f0.7820865974627469")

    st.markdown("<h3>Next Level | Academia | Cajazeiras - PB</h3>", unsafe_allow_html=True)
    embed_centered_iframe("https://www.google.com/maps/embed?pb=!4v1753180786706!6m8!1m7!1sCAoSHENJQUJJaEFxQUtEOWxMaEdRekpiYk5SbGEzeGc.!2m2!1d-6.887891776224389!2d-38.55972383357095!3f1.520990456891578!4f-30.982226239046547!5f0.4000000000000002")

    st.markdown("<h3>Next Level | Academia | Brejo Santo-CE</h3>", unsafe_allow_html=True)
    embed_centered_iframe("https://www.google.com/maps/embed?pb=!4v1753151300722!6m8!1m7!1sCAoSHENJQUJJaENabnYta1NIYnk3U0VTZXg2cVZFSUQ.!2m2!1d-7.486728599999999!2d-38.9976357!3f14.212028543852037!4f-10.245711121253734!5f0.7820865974627469")

    st.markdown("<h3>Ginásio Poliesportivo Welingtão | Brejo Santo-CE</h3>", unsafe_allow_html=True)
    embed_centered_iframe("https://www.google.com/maps/embed?pb=!4v1753150938298!6m8!1m7!1sCAoSHENJQUJJaEQwY09MVkRONG5ic1VnamQtTkw0SV8.!2m2!1d-7.489376802708099!2d-38.9901219288986!3f190.74911673396883!4f3.1483665025552057!5f0.7820865974627469")

    st.markdown("<h3>Bar Caldeira do Inferno | Brejo Santo-CE</h3>", unsafe_allow_html=True)
    embed_centered_iframe("https://www.google.com/maps/embed?pb=!4v1753231196225!6m8!1m7!1sCAoSHENJQUJJaEQxcnI1cGMyTWlqQ3Z5NUxiV2tpZlY.!2m2!1d-7.492859299999999!2d-38.98546!3f157.1298482595132!4f-34.00956372051077!5f0.7820865974627469")

    st.markdown("<h3>Pista Pública de Skate | Brejo Santo-CE</h3>", unsafe_allow_html=True)
    embed_centered_iframe("https://www.google.com/maps/embed?pb=!4v1753231252386!6m8!1m7!1sCAoSHENJQUJJaEJodGhOaDNiWTg4MDIwYWVFQzdqXzg.!2m2!1d-7.48501101224435!2d-38.98611708745776!3f8.388327367476812!4f-13.107200825728412!5f0.4000000000000002")

    st.markdown("<h3>Quadra de Basquete | Brejo Santo-CE</h3>", unsafe_allow_html=True)
    embed_centered_iframe("https://www.google.com/maps/embed?pb=!4v1753150711289!6m8!1m7!1sCAoSHENJQUJJaERnaG1mQmpPOEpHZk9LYnNWUmlQaXM.!2m2!1d-7.484971799999999!2d-38.9860056!3f195.21!4f-0.5600000000000023!5f0.4000000000000002")

    st.markdown("<h3>CineTeatro Municipal Professor Júlio Macedo Costa | Brejo Santo-CE</h3>", unsafe_allow_html=True)
    embed_centered_iframe("https://www.google.com/maps/embed?pb=!4v1753310567315!6m8!1m7!1sCAoSHENJQUJJaEJpelU0dGRScTVzY3hGQXVwaDNCTkc.!2m2!1d-7.491297399999999!2d-38.9761639!3f357.427296679104!4f-4.339601456811053!5f0.4000000000000002")

    st.markdown('</div>', unsafe_allow_html=True)

with tab_tour:
    st.markdown('<div class="tab-content-style">', unsafe_allow_html=True)

    st.markdown("<h3>BFX Consultoria | Contabilidade | Brejo Santo-CE</h3>", unsafe_allow_html=True)
    embed_centered_iframe("https://www.google.com/maps/embed?pb=!4v1753197635440!6m8!1m7!1sCAoSHENJQUJJaEQtVk8yb1hxaHppRUVVdWxWQnZqMmU.!2m2!1d-7.490032784172747!2d-38.97943065124561!3f192.59282718210963!4f11.423489168813845!5f0.7820865974627469")

    st.markdown("<h3>Museu Municipal Historiadora Marineusa Santana Basílio Leite | Brejo Santo-CE</h3>", unsafe_allow_html=True)
    embed_centered_iframe("https://www.google.com/maps/embed?pb=!4v1753231442306!6m8!1m7!1sCAoSHENJQUJJaEFMV2tRTUxYT1VIdEdnMmNwbzltYzk.!2m2!1d-7.488856276863652!2d-38.98997716077863!3f5.084682959484297!4f1.5985458206393588!5f0.4000000000000002")

    st.markdown('</div>', unsafe_allow_html=True)

with tab_video:
    st.markdown('<div class="tab-content-style">', unsafe_allow_html=True)

    # Vídeo 1: Pitinininha Kids
    st.markdown("<h3>Pitinininha Kids | A Melhor Loja de Roupas Infantis de Brejo Santo-CE</h3>", unsafe_allow_html=True)
    video_html_1 = """
    <div style="display: flex; justify-content: center;">
      <iframe 
        width="480" 
        height="315" 
        src="https://www.youtube.com/embed/Ur5kwNnWq8A?si=Ci_G4SkarslpgfsW" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        allowfullscreen>
      </iframe>
    </div>
    """
    components.html(video_html_1, height=350)

    # Vídeo 2: Next Level
    st.markdown("<h3>Next Level | Cajazeiras-PB | A Academia Mais Moderna de Cajazeiras-PB</h3>", unsafe_allow_html=True)
    video_html_2 = """
    <div style="display: flex; justify-content: center;">
      <iframe 
        width="480" 
        height="315" 
        src="https://www.youtube.com/embed/lwStG-fQeok?si=OF8M5ZwyK8gsjplq" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        allowfullscreen>
      </iframe>
    </div>
    """
    components.html(video_html_2, height=350)

    # Vídeo 3: Skate Radical
    st.markdown("<h3>Skate Radical no Sol Escaldante: Vídeo Imersivo 360° com Ítalo Gomes | Ranke 360</h3>", unsafe_allow_html=True)
    video_html_3 = """
    <div style="display: flex; justify-content: center;">
      <iframe 
        width="480" 
        height="315" 
        src="https://www.youtube.com/embed/_wlmH5ync08?si=3Wo3AZumCWlpblW_" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        allowfullscreen>
      </iframe>
    </div>
    """
    components.html(video_html_3, height=350)

    st.markdown('</div>', unsafe_allow_html=True)



with tab_mapa:
    st.markdown('<div class="tab-content-style">', unsafe_allow_html=True)
    st.markdown("<!-- Conteúdo da aba MAPA - insira seu conteúdo aqui -->", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab_exclusivo:
    st.markdown('<div class="tab-content-style">', unsafe_allow_html=True)
    st.markdown("<!-- Conteúdo da aba 360° EXCLUSIVO - insira seu conteúdo aqui -->", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
