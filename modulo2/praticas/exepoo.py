# Exercício 1
print("="*60)
print("Exercício 1 - Crie a classe Pessoa com os atributos nome e idade. Instancie duas pessoas diferentes. \
Exiba seus dados. ")
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

# Exercício 2
print("\n" + "="*60)
print("Exercício 2 - Crie a classe Professor herdando de Pessoa. Atributos adicionais: disciplina, salario. \
Método: apresentar_professor() que exibe nome, idade e disciplina.")
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

# Exercício 3
print("\n" + "="*60)
print("EXERCÍCIO 3 - Crie a classe Estudante herdando de Pessoa. " \
"Atributos adicionais: curso, matricula. Método: apresentar_estudante() que exibe nome, idade e curso.")
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

# Exercício 4
print("\n" + "="*60)
print("EXERCÍCIO 4 - Implemente encapsulamento para o salário do professor, permitindo apenas alteração através de \
um método ajustar_salario(valor).")
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

print(f"Salário inicial: R$ {professor2.obter_salario():.2f}")

# Teste de encapsulamento rigoroso
try:
    print(professor2.__salario)  # Isso DEVE falhar!
except AttributeError as e:
    print(f"✅ Encapsulamento funcionando! Erro: {e}") 

# Exercício 5
print("\n" + "="*60)
print("EXERCÍCIO 5 - Utilize polimorfismo criando um método apresentar() em Professor e Estudante \
que funciona de forma diferente em cada classe.")
print("="*60)

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
professor_poli = ProfessorPolimorfismo("Dra. Silva", 48, "Física", 6000.00)
estudante_poli = EstudantePolimorfismo("Bruna", 39, "Medicina", "2025005")

pessoas = [professor_poli, estudante_poli]
print("\nDemonstração REAL do polimorfismo:")
for pessoa in pessoas:
    print(pessoa.apresentar())