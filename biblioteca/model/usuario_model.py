class Usuario:
    def __init__(self, cpf: str, nome: str):
        self.cpf = cpf
        self.nome = nome

    def __repr__(self):
        return f"Usuario(cpf={self.cpf!r}, nome={self.nome!r})"