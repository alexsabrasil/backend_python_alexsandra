# Classe PAI (superclasse)
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    
    def dormir(self):
        return f"{self.nome} está dormindo."

# Classe FILHA 1 (subclasse)
class Estudante(Pessoa):  # Herda de Pessoa
    def __init__(self, nome, idade, matricula, curso):
        # super() chama o construtor da classe pai
        super().__init__(nome, idade)
        # Adiciona atributos específicos do estudante
        self.matricula = matricula
        self.curso = curso
    
    def estudar(self):
        return f"{self.nome} está estudando {self.curso}!"
    
    def fazer_prova(self):
        return f"{self.nome} está fazendo uma prova!"

# Classe FILHA 2 (subclasse)
class Professor(Pessoa):  # Herda de Pessoa
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.salario = salario
    
    def ensinar(self):
        return f"Professor {self.nome} está ensinando {self.disciplina}!"
    
    def corrigir_provas(self):
        return f"{self.nome} está corrigindo provas de {self.disciplina}."

# Testando a herança
# Criando objetos
joao = Estudante("João", 20, "2024001", "Programação")
maria = Professor("Maria", 35, "Python", 5000)

# Métodos herdados da classe Pessoa
print(joao.apresentar())    # Método da classe pai
print(maria.apresentar())   # Método da classe pai

print("---")

# Métodos específicos de cada classe
print(joao.estudar())       # Método da classe Estudante
print(joao.fazer_prova())   # Método da classe Estudante

print(maria.ensinar())      # Método da classe Professor
print(maria.corrigir_provas())  # Método da classe Professor

print("---")

# Ambos podem dormir (método herdado)
print(joao.dormir())
print(maria.dormir())