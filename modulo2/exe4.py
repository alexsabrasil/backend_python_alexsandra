"""
Exercício 4
Implemente encapsulamento para o salário do professor, permitindo apenas alteração através de
um método ajustar_salario(valor).
"""
from exe1 import Pessoa

print("\n" + "="*60)
print("EXERCÍCIO 4 - ENCAPSULAMENTO")
print("="*60)

# EXERCÍCIO 4: Implementar encapsulamento para o salário
class ProfessorComEncapsulamento(Pessoa):
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.__salario = salario  # Atributo privado
    
    def apresentar_professor(self):
        print(f"Professor: {self.nome}, {self.idade} anos, ensina {self.disciplina}")
    
    # Método para ALTERAR o salário (única forma permitida)
    def ajustar_salario(self, novo_valor):
        if novo_valor > 0:  # Validação simples
            self.__salario = novo_valor
            print(f"Salário ajustado para R$ {self.__salario}")
        else:
            print("Erro: Salário deve ser maior que zero!")
    
    # Método para CONSULTAR o salário (getter)
    def obter_salario(self):
        return self.__salario
    
   # Testando o encapsulamento
professor2 = ProfessorComEncapsulamento("Roberto", 38, "Python", 4500.00)

print(f"Salário inicial: R$ {professor2.obter_salario()}")

# Tentando acessar diretamente (NÃO FUNCIONARÁ como esperado)
# print(professor2.__salario)  # Isso geraria um erro!

# Forma CORRETA de alterar o salário
professor2.ajustar_salario(5200.00)
print(f"Novo salário: R$ {professor2.obter_salario()}")

# Testando validação
professor2.ajustar_salario(-1000)  # Deve dar erro 