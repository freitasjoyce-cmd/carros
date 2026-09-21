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
# CSS - CORRIGIDO E SEM INTERPOLAÇÃO DE VARIÁVEIS DO PYTHON
# =========================================================

st.markdown("""
<style>

@import url(
'https://googleapis.com'
);

/* =========================================================
FONTE
========================================================= */

html,
body,
[class*="css"] {
    font-family: 'Poppins', sans-serif;
}


/* =========================================================
FUNDO PRINCIPAL
========================================================= */

.stApp {
    background:
        linear-gradient(
            135deg,
            #F0F0E5 0%,
            #E1E4C8 50%,
            #D4DCB5 100%
        );
}


/* =========================================================
ÁREA PRINCIPAL
========================================================= */

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #162630,
            #223944
        );

    border-right:
        2px solid #77864B;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}


/* =========================================================
LOGO
========================================================= */

.logo-title {
    font-size: 28px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-bottom: 5px;
}

.logo-subtitle {
    font-size: 11px;
    font-weight: 700;
    color: #BFCB9C !important;
    letter-spacing: 1px;
}


/* =========================================================
TÍTULOS
========================================================= */

.page-title {
    font-size: 38px;
    font-weight: 800;
    color: #26311F !important;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 17px;
    color: #46513B !important;
    margin-bottom: 30px;
}


/* =========================================================
HERO
========================================================= */

.hero-container {
    position: relative;
    height: 320px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;
    background: linear-gradient(135deg, #152631 0%, #233C48 100%);
    box-shadow: 0 15px 35px rgba(0,0,0,0.22);
}

.hero-content {
    position: absolute;
    top: 50%;
    left: 7%;
    transform: translateY(-50%);
    max-width: 700px;
}

.hero-number {
    font-size: 70px;
    font-weight: 800;
    color: #A4D080 !important;
    line-height: 1;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-top: 12px;
    line-height: 1.1;
}

.hero-text {
    font-size: 17px;
    color: #E8EDDE !important;
    margin-top: 20px;
    line-height: 1.7;
}


/* =========================================================
FORMULÁRIO
========================================================= */

[data-testid="stForm"] {
    background: rgba(255,255,255,0.85);
    padding: 30px;
    border-radius: 25px;
    border: 1px solid #B8C391;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span {
    color: #26311F !important;
    font-size: 15px !important;
    font-weight: 700 !important;
}

.stTextInput input, .stNumberInput input {
    background-color: #FFFFFF !important;
    color: #202820 !important;
    border: 2px solid #7C8956 !important;
    border-radius: 12px !important;
}

/* =========================================================
SELECTBOX - COMPATÍVEL COM NUVEM
========================================================= */
[data-baseweb="select"] > div {
    background-color: #2F323C !important;
    border: 2px solid #687548 !important;
    border-radius: 12px !important;
}
[data-baseweb="select"] > div * {
    color: #FFFFFF !important;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# SISTEMA DE MEMÓRIA ROBUSTO (MISTO: CSV + SESSION STATE)
# =========================================================

# Inicializa a memória se não existir
if "banco_veiculos" not in st.session_state:
    colunas = ["Marca", "Modelo", "Ano", "Placa", "Preço"]
    
    # Tenta ler do CSV primeiro se ele existir
    if os.path.exists(ARQUIVO):
        try:
            st.session_state.banco_veiculos = pd.read_csv(ARQUIVO)
        except Exception:
            st.session_state.banco_veiculos = pd.DataFrame(columns=colunas)
    else:
        st.session_state.banco_veiculos = pd.DataFrame(columns=colunas)

# Recupera os dados salvos da memória
df_carros = st.session_state.banco_veiculos
total_veiculos = len(df_carros)


# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<p class="logo-title">🚗 AutoCadastro</p>', unsafe_allow_html=True)
    st.markdown('<p class="logo-subtitle">SISTEMA PRO v2.0</p>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### Navegação Rápida")
    st.info("Utilize o painel principal para cadastrar novos veículos na frota.")


# --- HERO HEADER ---
st.markdown(f"""
<div class="hero-container">
    <div class="hero-content">
        <div class="hero-number">{total_veiculos}</div>
        <div class="hero-title">Veículos na Frota Ativa</div>
        <div class="hero-text">Gerencie o inventário da sua concessionária de forma ágil, integrada e com atualização em tempo real utilizando nossa plataforma profissional.</div>
    </div>
</div>
""", unsafe_allow_html=True)


# --- CORPO PRINCIPAL ---
st.markdown('<p class="page-title">Cadastro Corporativo de Veículos</p>', unsafe_allow_html=True)
st.markdown('<p class="page-subtitle">Preencha as informações técnicas do automóvel para registrar a entrada no sistema.</p>', unsafe_allow_html=True)


# --- FORMULÁRIO DE CADASTRO ---
with st.form("cadastro_carro"):
    col1, col2 = st.columns(2)
    
    with col1:
        marca = st.text_input("Marca do Veículo", placeholder="Ex: Toyota, BMW, Chevrolet")
        modelo = st.text_input("Modelo", placeholder="Ex: Corolla Cross, X5, Onix")
        ano = st.number_input("Ano de Fabricação", min_value=1900, max_value=2030, value=2026)
        
    with col2:
        placa = st.text_input("Placa do Veículo", placeholder="Ex: ABC1D23")
        preco = st.number_input("Preço de Avaliação (R$)", min_value=0.0, format="%.2f")
        tipo_categoria = st.selectbox("Categoria Operacional", ["Premium", "Sedan", "SUV", "Hatch", "Comercial"])
        
    submit = st.form_submit_button("Confirmar Registro no Sistema")


# --- LÓGICA DE CADASTRO ---
if submit:
    if marca and modelo and placa:
        # Novo registro formatado
        novo_carro = pd.DataFrame([{
            "Marca": marca,
            "Modelo": modelo,
            "Ano": ano,
            "Placa": placa.upper(),
            "Preço": preco
        }])
        
        # Atualiza a tabela na memória do Streamlit
        st.session_state.banco_veiculos = pd.concat([df_carros, novo_carro], ignore_index=True)
        
        # Tenta também salvar no CSV de backup local
        try:
            st.session_state.banco_veiculos.to_csv(ARQUIVO, index=False)
        except Exception:
            pass # Ignora silenciosamente se o servidor online travar a escrita física
            
        st.success(f"Sucesso! O veículo **{marca} {modelo}** foi integrado ao inventário.")
        st.rerun()
    else:
        st.error("Erro ao cadastrar: Preencha os campos obrigatórios (Marca, Modelo e Placa).")


# --- LISTAGEM DE VEÍCULOS ---
st.markdown("---")
st.markdown("### 📋 Registros Atuais no Sistema")

if not df_carros.empty:
    st.dataframe(df_carros, use_container_width=True)
else:
    st.info("Nenhum veículo cadastrado no momento. Utilize o formulário acima para inserir o primeiro registro.")
