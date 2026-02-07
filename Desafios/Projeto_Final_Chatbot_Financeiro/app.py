import streamlit as st
from ai.ollama_client import perguntar_ao_modelo
from services.simulators import juros_compostos, simular_cdi, simular_financiamento
from db.models import (
    create_user, get_user, get_user_by_name, save_message, verify_password,
    get_conversation_history, save_simulation, get_simulations
)

st.set_page_config(page_title="CFI", page_icon="💰", layout="wide")
st.title("Chatbot Financeiro Inteligente - CFI")

# -------- LOGIN / PERFIL --------
if "user_id" not in st.session_state:
    st.subheader("👤 Login ou criação de perfil")

    nome = st.text_input("Nome")
    senha = st.text_input("Senha", type="password")
    objetivo = st.text_input("Objetivo financeiro (opcional)")
    renda = st.number_input("Renda mensal (R$)", min_value=0.0, step=500.0)
    risco = st.selectbox("Perfil de risco", ["Conservador", "Moderado", "Arrojado"])

    if st.button("Entrar"):
        if nome.strip() == "" or senha.strip() == "":
            st.error("Por favor, informe nome e senha.")
        else:
            user_existente = get_user_by_name(nome)

            if user_existente:
                if verify_password(senha, user_existente["senha_hash"]):
                    st.session_state.user_id = user_existente["id"]
                    st.success("Login realizado com sucesso!")
                    st.rerun()
                else:
                    st.error("Senha incorreta.")
            else:
                user_id = create_user(nome, objetivo, renda, risco, senha)
                st.session_state.user_id = user_id
                st.success("Perfil criado com sucesso!")
                st.rerun()

    st.stop()



user = get_user(st.session_state.user_id)

# -------- CARREGAR HISTÓRICO --------
if "messages" not in st.session_state:
    history = get_conversation_history(st.session_state.user_id)
    st.session_state.messages = [
        {"role": "system", "content": "Você é um assistente financeiro educacional, claro, seguro e responsável."}
    ]
    for msg in history:
        st.session_state.messages.append({"role": msg["role"], "content": msg["message"]})

tab1, tab2, tab3, tab4 = st.tabs(["💬 Chat", "📈 Simulações", "📚 Produtos", "📜 Histórico"])

# -------- CHAT --------
with tab1:
    st.subheader("Conversa com o assistente")

    for msg in st.session_state.messages[1:]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Digite sua pergunta financeira...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        save_message(st.session_state.user_id, "user", user_input)

        resposta = perguntar_ao_modelo(st.session_state.messages)

        st.session_state.messages.append({"role": "assistant", "content": resposta})
        save_message(st.session_state.user_id, "assistant", resposta)

        with st.chat_message("assistant"):
            st.markdown(resposta)

# -------- SIMULAÇÕES --------
with tab2:
    st.subheader("Simulações financeiras")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 💰 Simulação de CDI")
        valor = st.number_input("Valor investido (R$)", min_value=0.0, step=100.0)
        taxa = st.number_input("Taxa anual (%)", min_value=0.0, step=0.1)
        meses = st.number_input("Período (meses)", min_value=1, step=1)

        if st.button("Simular CDI"):
            resultado = simular_cdi(valor, taxa / 100, meses)
            st.success(f"Valor final estimado: R$ {resultado:,.2f}")
            save_simulation(st.session_state.user_id, "CDI", {"valor": valor, "taxa": taxa, "meses": meses}, resultado)

    with col2:
        st.markdown("### 📈 Juros compostos")
        valor_j = st.number_input("Valor inicial (R$)", min_value=0.0, step=100.0, key="valor_j")
        taxa_j = st.number_input("Taxa mensal (%)", min_value=0.0, step=0.1, key="taxa_j")
        meses_j = st.number_input("Meses", min_value=1, step=1, key="meses_j")

        if st.button("Calcular juros"):
            resultado = juros_compostos(valor_j, taxa_j / 100, meses_j)
            st.success(f"Valor final com juros: R$ {resultado:,.2f}")
            save_simulation(st.session_state.user_id, "Juros Compostos", {"valor": valor_j, "taxa": taxa_j, "meses": meses_j}, resultado)

    st.markdown("---")
    st.markdown("### 🏠 Simulação de financiamento")
    valor_f = st.number_input("Valor do bem (R$)", min_value=0.0, step=1000.0)
    taxa_f = st.number_input("Taxa mensal (%)", min_value=0.0, step=0.1)
    meses_f = st.number_input("Número de parcelas", min_value=1, step=1)

    if st.button("Simular financiamento"):
        parcela = simular_financiamento(valor_f, taxa_f, meses_f)
        st.success(f"Parcela estimada: R$ {parcela:,.2f}")
        save_simulation(st.session_state.user_id, "Financiamento", {"valor": valor_f, "taxa": taxa_f, "meses": meses_f}, parcela)

# -------- PRODUTOS --------
with tab3:
    st.subheader("Educação financeira")

    produto = st.selectbox(
        "Selecione um produto financeiro:",
        ["Conta digital", "Cartão de crédito", "CDB", "Tesouro Direto", "Fundos de investimento", "Previdência privada"]
    )

    if st.button("Explicar produto"):
        pergunta = f"Explique de forma simples, clara e responsável o que é {produto}, suas vantagens, riscos e para quem é indicado."
        st.session_state.messages.append({"role": "user", "content": pergunta})
        save_message(st.session_state.user_id, "user", pergunta)

        resposta = perguntar_ao_modelo(st.session_state.messages)

        st.session_state.messages.append({"role": "assistant", "content": resposta})
        save_message(st.session_state.user_id, "assistant", resposta)
        st.info(resposta)

# -------- HISTÓRICO --------
with tab4:
    st.subheader("📜 Histórico de simulações")

    sims = get_simulations(st.session_state.user_id)

    if sims:
        for sim in sims:
            st.markdown(f"""
            **Tipo:** {sim['tipo']}  
            **Parâmetros:** {sim['parametros']}  
            **Resultado:** R$ {sim['resultado']:,.2f}  
            **Data:** {sim['created_at']}
            ---
            """)
    else:
        st.info("Nenhuma simulação salva ainda.")
