class Livro:
    def __init__(self, isbn: str, titulo: str):
        self.isbn = isbn
        self.titulo = titulo

    def __repr__(self):
        return f"Livro(isbn={self.isbn!r}, titulo={self.titulo!r})"