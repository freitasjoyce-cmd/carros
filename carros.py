import streamlit as st
import pandas as pd
import os

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="AutoCadastro PRO",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "carros.csv"


# =========================================================
# IMAGENS
# =========================================================

IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1492144534655-ae79c964c9d7"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_FROTA = (
    "https://images.unsplash.com/"
    "photo-1502877338535-766e1452684a"
    "?auto=format&fit=crop&w=1200&q=85"
)


# =========================================================
# CSS
# =========================================================

st.markdown(f"""
<style>

@import url(
'https://googleapis.com'
);

/* =========================================================
FONTE
========================================================= */

html,
body,
[class*="css"] {{
    font-family: 'Poppins', sans-serif;
}}


/* =========================================================
FUNDO PRINCIPAL
========================================================= */

.stApp {{
    background:
        linear-gradient(
            135deg,
            #F0F0E5 0%,
            #E1E4C8 50%,
            #D4DCB5 100%
        );
}}


/* =========================================================
ÁREA PRINCIPAL
========================================================= */

.block-container {{
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}}


/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"] {{
    background:
        linear-gradient(
            180deg,
            #162630,
            #223944
        );

    border-right:
        2px solid #77864B;
}}

[data-testid="stSidebar"] * {{
    color: #FFFFFF !important;
}}


/* =========================================================
LOGO
========================================================= */

.logo-title {{
    font-size: 28px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-bottom: 5px;
}}

.logo-subtitle {{
    font-size: 11px;
    font-weight: 700;
    color: #BFCB9C !important;
    letter-spacing: 1px;
}}


/* =========================================================
TÍTULOS
========================================================= */

.page-title {{
    font-size: 38px;
    font-weight: 800;
    color: #26311F !important;
    margin-bottom: 5px;
}}

.page-subtitle {{
    font-size: 17px;
    color: #46513B !important;
    margin-bottom: 30px;
}}


/* =========================================================
HERO
========================================================= */

.hero-container {{
    position: relative;
    height: 430px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;

    background-image: url('{IMAGEM_HERO}');
    background-size: cover;
    background-position: center;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.22);
}}

.hero-overlay {{
    position: absolute;
    inset: 0;

    background:
        linear-gradient(
            90deg,
            rgba(14,28,38,0.97) 0%,
            rgba(14,28,38,0.86) 45%,
            rgba(14,28,38,0.18) 100%
        );
}}

.hero-content {{
    position: absolute;
    top: 50%;
    left: 7%;

    transform: translateY(-50%);

    max-width: 580px;
}}

.hero-number {{
    font-size: 70px;
    font-weight: 800;
    color: #A4D080 !important;
    line-height: 1;
}}

.hero-title {{
    font-size: 46px;
    font-weight: 800;
    color: #FFFFFF !important;

    margin-top: 12px;
    line-height: 1.1;
}}

.hero-text {{
    font-size: 17px;
    color: #E8EDDE !important;

    margin-top: 20px;
    line-height: 1.7;
}}

.hero-badge {{
    display: inline-block;

    margin-top: 24px;

    padding: 10px 22px;

    border-radius: 30px;

    background: #6E8040;

    color: #FFFFFF !important;

    font-size: 14px;
    font-weight: 700;
}}


/* =========================================================
CARDS
========================================================= */

.info-card {{
    background: #FFFFFF;

    border-radius: 22px;

    padding: 28px;

    min-height: 170px;

    border:
        1px solid rgba(111,128,63,0.30);

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}}

.card-icon {{
    font-size: 32px;
}}

.card-number {{
    font-size: 34px;
    font-weight: 800;

    color: #26311F !important;

    margin-top: 10px;
}}

.card-label {{
    font-size: 14px;
    font-weight: 700;

    color: #566248 !important;

    margin-top: 5px;
}}


/* =========================================================
CARD ESCURO
========================================================= */

.dark-card {{
    background:
        linear-gradient(
            135deg,
            #152631,
            #233C48
        );

    border-radius: 24px;

    padding: 30px;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.16);
}}

.dark-card h2 {{
    color: #FFFFFF !important;
    margin-top: 0;
}}

.dark-card p {{
    color: #E2E9DA !important;
    line-height: 1.7;
}}


/* =========================================================
FORMULÁRIO
========================================================= */

[data-testid="stForm"] {{
    background:
        rgba(255,255,255,0.85);

    padding: 30px;

    border-radius: 25px;

    border:
        1px solid #B8C391;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.08);
}}


/* =========================================================
LABELS DOS CAMPOS
========================================================= */

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {{
    color: #26311F !important;

    opacity: 1 !important;

    font-size: 15px !important;

    font-weight: 700 !important;
}}


/* =========================================================
INPUTS
========================================================= */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {{
    background-color: #FFFFFF !important;

    color: #202820 !important;

    -webkit-text-fill-color:
        #202820 !important;

    border:
        2px solid #7C8956 !important;

    border-radius: 12px !important;

    font-size: 16px !important;

    font-weight: 500 !important;
}}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {{
    border:
        2px solid #556B2F !important;

    box-shadow:
        0 0 0 3px rgba(85,107,47,0.15) !important;
}}

input::placeholder,
textarea::placeholder {{
    color: #6A7060 !important;
    opacity: 1 !important;
}}


/* =========================================================
SELECTBOX - CORREÇÃO DEFINITIVA
========================================================= */

/* Caixa principal */

[data-baseweb="select"] > div {{
    background-color: #2F323C !important;

    border:
        2px solid #687548 !important;

    border-radius: 12px !important;
}}


/* TEXTO DO VEÍCULO SELECIONADO */

[data-baseweb="select"] > div * {{
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;

    opacity: 1 !important;
}}


/* Input interno */

[data-baseweb="select"] input {{
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}}


/* Valor selecionado */

[data-baseweb="select"] [class*="singleValue"] {{
    color: #FFFFFF !important;
}}


/* Seta */

[data-baseweb="select"] svg {{
    fill: #FFFFFF !important;
    color: #FFFFFF !important;
}}


/* Hover */

[data-baseweb="select"] > div:hover {{
    border-color: #A4B66A !important;
}}


/* =========================================================
MENU ABERTO DO SELECTBOX
========================================================= */

[data-baseweb="popover"] {{
    background-color: #2F323C !important;
}}

[data-baseweb="menu"] {{
    background-color: #2F323C !important;
}}

[data-baseweb="menu"] div {{
    color: #FFFFFF !important;
}}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNÇÕES DE PERSISTÊNCIA DOS DADOS (CSV)
# =========================================================

def carregar_dados():
    if os.path.exists(ARQUIVO):
        try:
            return pd.read_csv(ARQUIVO)
        except Exception:
            return pd.DataFrame(columns=["Marca", "Modelo", "Ano", "Placa", "Preço"])
    return pd.DataFrame(columns=["Marca", "Modelo", "Ano", "Placa", "Preço"])

def salvar_dados(df):
    df.to_csv(ARQUIVO, index=False)


# =========================================================
# LÓGICA E CONTEÚDO DO APLICATIVO
# =========================================================

df_carros = carregar_dados()
total_veiculos = len(df_carros)

# --- SIDEBAR BAR ---
with st.sidebar:
    st.markdown('<p class="logo-title">🚗 AutoCadastro</p>', unsafe_allow_html=True)
    st.markdown('<p class="logo-subtitle">SISTEMA PRO v2.0</p>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### Navegação Rápida")
    st.info("Utilize o painel principal para cadastrar novos veículos na frota ou visualizar os registros ativos.")

# --- HERO HEADER ---
st.markdown(f"""
<div class="hero-container">
    <div class="hero-overlay"></div>
    <div class="hero-content">
        <div class="hero-number">{total_veiculos}</div>
        <div class="hero-title">Veículos na Frota Ativa</div>
