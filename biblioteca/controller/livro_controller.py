from model.livro_model import Livro
from service.livro_service import salvar_livro, listar_livros

def cadastrar_livro(isbn: str, titulo: str) -> str:
    # validações simples
    if not isbn or not titulo:
        return "ISBN e título são obrigatórios."
    livro = Livro(isbn=isbn.strip(), titulo=titulo.strip())
    return salvar_livro(livro)

def obter_livros():
    return listar_livros()