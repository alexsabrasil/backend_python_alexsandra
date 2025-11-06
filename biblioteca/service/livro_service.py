from dados.database import executar, consultar
from model.livro_model import Livro
from typing import List

def salvar_livro(livro: Livro) -> str:
    try:
        executar("INSERT INTO livros (isbn, titulo) VALUES (?, ?);", (livro.isbn, livro.titulo))
        return "Livro cadastrado com sucesso."
    except Exception as e:
        # tratamento simples; em app real logar o erro
        return f"Erro ao cadastrar livro: {str(e)}"

def listar_livros() -> List[Livro]:
    rows = consultar("SELECT isbn, titulo FROM livros ORDER BY id DESC;")
    livros = [Livro(isbn=row[0], titulo=row[1]) for row in rows]
    return livros