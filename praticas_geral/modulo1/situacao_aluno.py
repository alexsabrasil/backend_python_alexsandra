# Exercício 6 - Situação do Aluno
nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    situacao = "APROVADO(A)"
elif nota >= 5:
    situacao = "EM REPOSIÇÃO"
else:
    situacao = "REPROVADO(A)"

print(f"{nome} está {situacao}!")
