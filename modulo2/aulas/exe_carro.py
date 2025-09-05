class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    # Metódo: Ação que o carro pode fazer (COMPORTAMENTO)
    def ligar(self):
        print(f"O {self.marca} {self.modelo} está ligado!")
    
    def acelerar(self):
        print(f"Vrum! O {self.modelo} {self.cor} está acelerando! ")
    
# Criando Objeto (INSTÂNCIAS) da classe Carro
meu_carro = Carro("Ford", "Fiesta", "Preto")
carro_vizinho = Carro("Fiat", "Uno", "Azul")

# Testando os objetos
print(f"Meu carro: {meu_carro.marca} {meu_carro.modelo} {meu_carro.cor}")
print(f"Carro do vizinho:  {carro_vizinho.marca} {carro_vizinho.modelo} {meu_carro.cor}")

# Chamando o (MÉTODO)
meu_carro.ligar()
carro_vizinho.acelerar()




    