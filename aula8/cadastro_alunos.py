# Lista que vai armazenar os alunos
alunos = []

while True:
    # Cria um dicionário para cada aluno
    aluno = {}

    # Entrada de dados
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    # Guarda os dados no dicionário
    aluno["nome"] = nome
    aluno["idade"] = idade

    # Adiciona o dicionário na lista
    alunos.append(aluno)

    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
    if continuar == "n":
        break

# Exibe a lista completa
print("\n📋 Lista de alunos cadastrados:")
for i, aluno in enumerate(alunos, start=1):
    print(f"{i}. Nome: {aluno['nome']}, Idade: {aluno['idade']}")