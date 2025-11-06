from model.usuario_model import Usuario
from service.usuario_service import salvar_usuario, listar_usuarios

def cadastrar_usuario(cpf: str, nome: str) -> str:
    # validação simples de CPF: só remover espaços e checar comprimento mínimo
    cpf_clean = cpf.replace(".", "").replace("-", "").strip()
    if not cpf_clean or not nome:
        return "CPF e nome são obrigatórios."
    if len(cpf_clean) < 11:
        return "CPF inválido (menos de 11 dígitos)."
    usuario = Usuario(cpf=cpf_clean, nome=nome.strip())
    return salvar_usuario(usuario)

def obter_usuarios():
    return listar_usuarios()