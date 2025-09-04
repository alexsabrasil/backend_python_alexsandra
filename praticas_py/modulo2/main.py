"""
Exercício 4
Implemente encapsulamento para o salário do professor, 
permitindo apenas alteração através de um método ajustar_salario(valor).
"""
# main.py
from professor import Professor
from estudante import Estudante

# Criando um professor
prof = Professor("Carla", 40, "Matemática", 5000.00)
prof.apresentar_professor()
print("Salário inicial:", prof.ver_salario())
prof.ajustar_salario(5200.00)
print("Salário após ajuste:", prof.ver_salario())
print("-" * 40)

# Criando um estudante
aluno = Estudante("Diana", 22, "Engenharia de Software", "2025A123")
aluno.apresentar_estudante()
