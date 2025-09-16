class Pessoa:
    # Construtor
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.__cidade = cidade


    # Método
    def get_apresentar(self):
        print(f"Nome: {self.nome} - idade {self.idade} - Cidade {self.__cidade}")

p1 = Pessoa('Regina', 34, "Olinda")
p1.get_apresentar()