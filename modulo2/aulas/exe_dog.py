class Dog:
    def __init__(self, nome, raca, idade): # Construtor com atributos
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.energia = 100
    # Métodos (ações prováveis)
    def latir(self):
        print(f"{self.nome} faz: Au au!")

    def correr(self):
        if self.energia > 20:
            print(f"{self.nome} está correndo!")
            self.energia -= 20 # Gasta energia ao correr
        else:
            print(f"{self.nome} está muito cansada para correr.")

    def dormir(self):
        print(f"{self.nome} está dormindo... Zzz")
        self.energia = 100
    
    def status(self):
        print(f"Nome: {self.nome}")
        print(f"Raça: {self.raca}")
        print(f"Idade: {self.idade} anos")
        print(f"Energia: {self.energia}%")

# Criando um cachorro
meu_dog = Dog("Mel", "Vira-Lata", 14)

# Testando atributos e métodos
meu_dog.status()
print("---")
meu_dog.latir()
meu_dog.correr()
meu_dog.correr()
meu_dog.correr()
meu_dog.correr()
meu_dog.correr() # Vai ficar cansado
meu_dog.correr() # Não consegue mais correr
print("---")
meu_dog.dormir()
meu_dog.status()