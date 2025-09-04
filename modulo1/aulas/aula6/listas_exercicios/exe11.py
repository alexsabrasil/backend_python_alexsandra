"""
Exercício 11: Cálculo de média e aprovação Peça duas notas, calcule a média e
informe se o aluno está Aprovado, em Recuperação ou Reprovado.

"""
# Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = (nota1 + nota2) / 2

# Estrutura condicional
if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# Saída
print(f"A média do aluno foi {media:.2f} e ele está {situacao}.")
