from dados.database import executar, consultar
from model.usuario_model import Usuario
from typing import List

def salvar_usuario(usuario: Usuario) -> str:
    try:
        executar("INSERT INTO usuarios (cpf, nome) VALUES (?, ?);", (usuario.cpf, usuario.nome))
        return "Usuário cadastrado com sucesso."
    except Exception as e:
        return f"Erro ao cadastrar usuário: {str(e)}"

def listar_usuarios() -> List[Usuario]:
    rows = consultar("SELECT cpf, nome FROM usuarios ORDER BY id DESC;")
    usuarios = [Usuario(cpf=row[0], nome=row[1]) for row in rows]
    return usuarios