# Definir a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome          # Público
        self._idade = idade       # Protegido (por convenção)
        self.__cidade = cidade    # Privado (por convenção)

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self._idade}")
        print(f"Cidade: {self.__cidade}")

    def get_cidade(self):
        return self.__cidade

    def set_cidade(self, nova_cidade):
        self.__cidade = nova_cidade

# Criar objetos da classe Pessoa
pessoa1 = Pessoa("Silvia", 23, "Recife")
pessoa2 = Pessoa("Bruna", 21, "São Paulo")

# Usar o método mostrar_dados()
print("Pessoa 1:")
pessoa1.mostrar_dados()

print("\nPessoa 2:")
pessoa2.mostrar_dados()

# Acessar cidade através do getter
print("\nCidade de pessoa1 (via getter):", pessoa1.get_cidade())

# Alterar a cidade usando o setter
pessoa1.set_cidade("Fortaleza")
print("Cidade de pessoa1 após alteração:", pessoa1.get_cidade())
