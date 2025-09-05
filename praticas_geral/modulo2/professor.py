"""
Exercício 2
Crie a classe Professor herdando de Pessoa.
- Atributos adicionais: disciplina, salario.
- Método: apresentar_professor() que exibe nome, idade e disciplina.
"""
# professor.py
from pessoa import Pessoa   # Importa a classe base Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, salario_inicial):
        super().__init__(nome, idade)

        self.disciplina = disciplina
        self.__salario = salario_inicial   # atributo encapsulado

    def apresentar_professor(self):
        print(f"Professor: {self.nome}, {self.idade} anos — Disciplina: {self.disciplina}")

    def ajustar_salario(self, valor):
        if valor >= 0:
            self.__salario = valor
        else:
            print("Valor inválido. O salário deve ser >= 0.")

    def ver_salario(self):
        return self.__salario
