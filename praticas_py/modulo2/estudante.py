"""Exercício 3
Crie a classe Estudante herdando de Pessoa.
- Atributos adicionais: curso, matricula.
- Método: apresentar_estudante() que exibe nome, idade e curso."""

# estudante.py
from pessoa import Pessoa   # Importa a classe base

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso, matricula):
        super().__init__(nome, idade)
        self.curso = curso
        self.matricula = matricula

    def apresentar_estudante(self):
        print(f"Estudante: {self.nome}, {self.idade} anos — Curso: {self.curso}")
