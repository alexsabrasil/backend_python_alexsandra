import streamlit as st
from dados.database import criar_tabela
from controller.livro_controller import cadastrar_livro, obter_livros
from controller.usuario_controller import cadastrar_usuario, obter_usuarios

#st.title("Olá pessoal!!!")
# st.write("Teste de conexão")
# Adicione isso para debug
# st.success("Streamlit está funcionando!")

# Criar tabela na inicialização
criar_tabela()

st.title("Cadastro de livros")

st.subheader("Adicionar novo livro")
with st.form("form_livro"):
    isbn = st.text_input("ISBN")
    titulo = st.text_input("Título")
    submitted = st.form_submit_button("Cadastrar livro")
    if submitted:
        mensagem = cadastrar_livro(isbn, titulo)
        if mensagem.startswith("Erro"):
            st.error(mensagem)
        else:
            st.success(mensagem)

st.markdown("---")
st.subheader("Livros cadastrados")
livros = obter_livros()
if livros:
    for l in livros:
        st.write(f"ISBN: {l.isbn}  •  Título: {l.titulo}")
else:
    st.write("Nenhum livro cadastrado ainda.")

st.markdown("##")

st.subheader("Adicionar novo usuário (desafio)")
with st.form("form_usuario"):
    cpf = st.text_input("CPF (somente números)")
    nome = st.text_input("Nome")
    submitted_user = st.form_submit_button("Cadastrar usuário")
    if submitted_user:
        mensagem = cadastrar_usuario(cpf, nome)
        if mensagem.startswith("Erro"):
            st.error(mensagem)
        else:
            st.success(mensagem)

st.markdown("---")
st.subheader("Usuários cadastrados")
usuarios = obter_usuarios()
if usuarios:
    for u in usuarios:
        st.write(f"CPF: {u.cpf}  •  Nome: {u.nome}")
else:
    st.write("Nenhum usuário cadastrado ainda.")