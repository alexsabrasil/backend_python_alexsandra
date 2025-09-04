"""
Exercício 3
Crie a classe Estudante herdando de Pessoa.
- Atributos adicionais: curso, matricula.
- Método: apresentar_estudante() que exibe nome, idade e curso.

"""
from exe1 import Pessoa

print("\n" + "="*60)
print("EXERCÍCIO 3 - Classe Estudante (Herança)")
print("="*60)

# EXERCÍCIO 3: Criar classe Estudante que herda de Pessoa
class Estudante(Pessoa):  # Estudante HERDA de Pessoa
    def __init__(self, nome, idade, curso, matricula):
        # Chama o construtor da classe pai (Pessoa)
        super().__init__(nome, idade)
        # Adiciona os atributos específicos do Estudante
        self.curso = curso
        self.matricula = matricula
    
    # Método específico da classe Estudante
    def apresentar_estudante(self):
        print(f"Estudante: {self.nome}, {self.idade} anos, curso de {self.curso}")

# Criando um estudante
estudante1 = Estudante("Ana", 20, "Engenharia", "2023001")

# Testando o método
estudante1.apresentar_estudante()

# O estudante também herda os atributos da classe Pessoa
print(f"Nome do estudante: {estudante1.nome}")
print(f"Matrícula: {estudante1.matricula}")