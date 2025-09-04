"""
Exercício 2

Crie a classe Professor herdando de Pessoa.
- Atributos adicionais: disciplina, salario.
- Método: apresentar_professor() que exibe nome, idade e disciplina.
"""
from exe1 import Pessoa

print("\n" + "="*60)
print("Exercício 2 - Classe Professor (Herança)")
print("="*60)

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.salario = salario

# Criando o método especifico classe Professor
    def apresentar_professor(self):
        print(f"Professor: {self.nome}, {self.idade} anos, ensina {self.disciplina} ")

# Criando um professor
professor1 = Professor("Ricardo", 55, "Matemática", 5000.00)

# Testando
professor1.apresentar_professor()

print(f"Nome do professor: {professor1.nome}")
print(f"Salário: R$ {professor1.salario}")