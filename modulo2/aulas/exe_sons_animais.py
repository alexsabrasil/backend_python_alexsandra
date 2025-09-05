# Classes diferentes com o mesmo método
class Cachorro:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        return f"{self.nome} faz: Au au!"

class Gato:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        return f"{self.nome} faz: Miau!"

class Pato:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        return f"{self.nome} faz: Quack!"

class Vaca:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        return f"{self.nome} faz: Muuuu!"

# Criando uma lista com diferentes animais
animais = [
    Cachorro("Rex"),
    Gato("Mimi"),
    Pato("Donald"),
    Vaca("Mimosa")
]

# POLIMORFISMO EM AÇÃO!
# O mesmo código funciona para todos os animais
print("🐾 Hora do show dos animais! 🐾")
for animal in animais:
    print(animal.fazer_som())  # Mesmo método, comportamentos diferentes!

print("\n" + "="*40)

# Outro exemplo: função que aceita qualquer animal
def apresentar_animal(animal):
    print(f"Este é um animal especial!")
    print(animal.fazer_som())
    print("-" * 20)

# A função funciona com qualquer animal!
rex = Cachorro("Rex")
mimi = Gato("Mimi")

apresentar_animal(rex)   # Funciona com cachorro
apresentar_animal(mimi)  # Funciona com gato