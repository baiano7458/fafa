import streamlit as st
import sqlite3
import requests
import hashlib
import streamlit.components.v1 as components

def registrar_acesso(nome_usuario):
    payload = {"usuario": nome_usuario}
    try:
        requests.post("http://192.168.15.9:5000/registrar_acesso", json=payload)
    except:
        pass


def conectar():
    return sqlite3.connect("usuarios.db")

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def registrar_usuario(nome, email, senha):
    conn = conectar()
    c = conn.cursor()
    try:
        c.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                (nome, email, hash_senha(senha)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def autenticar_usuario(email, senha):
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", 
            (email, hash_senha(senha)))
    user = c.fetchone()
    conn.close()
    return user

# ========= Interface do Streamlit =========

st.set_page_config(page_title="App com Login", layout="centered")
criar_tabela()

st.title("Explicação do Meu Trabalho")
st.write("Para ver o conteúdo completo e jogar o game, você precisa se registrar e fazer login.")

if "logado" not in st.session_state:
    st.session_state.logado = False

# ============ Se logado ============

if st.session_state.logado:
    st.success(f"Bem-vindo(a), {st.session_state.nome_usuario}!")
    st.header("Explicação do Projeto")

    st.write("Boa tarde! Meu nome é Guilherme sou dupla do Pedro e a gente fez um jogo com base no que “ensinam” na área de instrumentação que seria a automação de maquinas e seus objetivos, nosso jogo mostra como uma maquina é automatizada para que saiba diferenciar caixas danificadas e caixas em boas condições, e para deixar mais interativo fizemos como se você fosse a garra, a gente poderia ter feito facilmente uma “animação” da garra escolhendo a caixa boa e colocando na esteira e a caixa ruim no lixo mas para ter mais imersão decidimos fazer assim. ")

    st.write("Lembrando que o jogo é apenas para computador")
    
    st.link_button("⬇️ Baixar Jogo do Robô", "https://raw.githubusercontent.com/baiano7458/fafa/refs/heads/main/jogo_final.zip")
    if st.button("Sair"):
        st.session_state.logado = False

        st.rerun()


# ============ Registro ============

else:
    st.title("Bem-vindo ao site")

    aba = st.radio("Escolha uma opção", ["Login", "Registrar"])

    if aba == "Registrar":
        with st.form("form_registro"):
            nome = st.text_input("Nome completo")
            email = st.text_input("Email")
            senha = st.text_input("Senha", type="password")
            confirmar = st.text_input("Confirmar senha", type="password")

            botao_reg = st.form_submit_button("Registrar")

        if botao_reg:
            if not nome or not email or not senha:
                st.error("Preencha todos os campos.")
            elif senha != confirmar:
                st.warning("As senhas não coincidem.")
            else:
                ok = registrar_usuario(nome, email, senha)
                if ok:
                    st.success("Registro feito com sucesso! Vá para a aba Login.")
                else:
                    st.error("Esse email já está cadastrado.")

    # ============ Login ============
    else:
        with st.form("form_login"):
            email_login = st.text_input("Email")
            senha_login = st.text_input("Senha", type="password")
            botao_login = st.form_submit_button("Entrar")

        if botao_login:
            usuario = autenticar_usuario(email_login, senha_login)
            if usuario:
                st.session_state.logado = True
                st.session_state.nome_usuario = usuario[1]
                registrar_acesso(usuario[1])  # 👈 registra o acesso na VM
                st.rerun()

            else:
                st.error("Email ou senha incorretos.")
