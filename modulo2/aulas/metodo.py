class Pessoa:
    # Construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    # Método
    def apresentar(self):
        print(f"Nome: {self.nome} - idade {self.idade}")

p1 = Pessoa('Regina', 34)
p1.apresentar()