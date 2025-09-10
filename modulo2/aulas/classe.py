
"""
# Definir a classe Pessoa
class Pessoa:
    pass


# Criar um objeto a partir da classe Pessoa
pessoa = Pessoa()
pessoa2 = Pessoa()
print(pessoa)
print(pessoa2)"""

# Classe: 
# Definir a classe Pessoa
class Pessoa:
    def __init__(self, nome,idade,cidade):
        self.nome = nome # Público
        self._idade = idade # Protegido Protected
        self._cidade = cidade # Privada Private

# Criar um ambiente a partir da classe Pessoa
pessoa = Pessoa("Silvia", 23 "Recife")
estudante = Pessoa("")

print(f"")