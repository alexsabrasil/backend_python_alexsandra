"""
Exercício 5

Utilize polimorfismo criando um método apresentar() em Professor e Estudante que funciona de
forma diferente em cada classe.

"""

print("\n" + "="*60)
print("EXERCÍCIO 5 - POLIMORFISMO")
print("="*60)

from exe1 import Pessoa

class ProfessorPolimorfismo(Pessoa):
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.salario = salario

    # Método apresentar() específico para Professor
    def apresentar(self):
        return f"🎓 Professor {self.nome}, {self.idade} anos - Ensina {self.disciplina}"

class EstudantePolimorfismo(Pessoa):
    def __init__(self, nome, idade, curso, matricula):
        super().__init__(nome, idade)
        self.curso = curso
        self.matricula = matricula
    
     # Método apresentar() específico para Estudante
    def apresentar(self):
        return f"📚 Estudante {self.nome}, {self.idade} anos - Curso: {self.curso} (Mat: {self.matricula})"
    
# Criando objetos das duas classes
professor_poli = ProfessorPolimorfismo("Dr. Silva", 42, "Física", 6000.00)
estudante_poli = EstudantePolimorfismo("Bruna", 19, "Medicina", "2024005")

# POLIMORFISMO EM AÇÃO!
# O mesmo método "apresentar()" se comporta diferente em cada classe
print("Demonstração do Polimorfismo:")
print(professor_poli.apresentar())  # Chama o método da classe Professor
print(estudante_poli.apresentar())  # Chama o método da classe Estudante    


"""
#print("\n" + "-"*50)
print("POLIMORFISMO COM LISTA - Exemplo Avançado")
print("-"*50)

# Criando uma lista com objetos de classes diferentes
pessoas = [
    ProfessorPolimorfismo("Ana Costa", 35, "Química", 5500.00),
    EstudantePolimorfismo("Pedro", 21, "Engenharia", "2023010"),
    ProfessorPolimorfismo("João Santos", 50, "História", 4800.00),
    EstudantePolimorfismo("Clara", 18, "Psicologia", "2024020")
]

# POLIMORFISMO: mesmo comando, comportamentos diferentes!
print("Lista de pessoas na escola:")
for pessoa in pessoas:
    # Python automaticamente chama o método correto para cada classe
    print(f"- {pessoa.apresentar()}")

print("\n" + "-"*50)
print("FUNÇÃO QUE USA POLIMORFISMO")
print("-"*50)

def exibir_informacoes(pessoa):
    
    Esta função funciona com qualquer objeto que tenha o método apresentar()
    Isso é POLIMORFISMO! Não importa se é Professor ou Estudante
    
    print(f"Informações: {pessoa.apresentar()}")
    print(f"Tipo do objeto: {type(pessoa).__name__}")
    print()

# Testando a função polimórfica
print("Função polimórfica em ação:")
exibir_informacoes(professor_poli)
exibir_informacoes(estudante_poli)

print("\n" + "="*60)
print("RESUMO DOS CONCEITOS APRENDIDOS")
print("="*60)
print("1. CLASSE: Molde/modelo para criar objetos")
print("2. OBJETO: Instância de uma classe")
print("3. HERANÇA: Uma classe pode herdar de outra (reutilizar código)")
print("4. ENCAPSULAMENTO: Controlar acesso aos dados (__privado)")
print("5. POLIMORFISMO: Mesmo método, comportamentos diferentes")
print("6. SELF: Referência ao objeto atual")
print("7. __INIT__: Método construtor (executado ao criar objeto)")
print("8. SUPER(): Chama métodos da classe pai")"""