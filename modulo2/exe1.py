"""Exercício 1
- Crie a classe Pessoa com os atributos nome e idade. 
- Instancie duas pessoas diferentes
- Exiba seus dados."""

print("="*60)
print("Exercício 1 - Classe Pessoa")
print("="*60)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
# Intanciando duas pessoas diferentes
pessoa1 = Pessoa("Ricardo", 50)
pessoa2 = Pessoa("Noemia", 48)

# Exibindo os dados
print(f"Pessoa 1: Nome = {pessoa1.nome}, idade = {pessoa1.idade}")
print(f"Pessoa 2: Nome = {pessoa2.nome}, idade = {pessoa2.idade}")