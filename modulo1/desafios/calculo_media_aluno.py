# Passo 1: Pedir as três notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Passo 2: Calcular a média aritmética
media = (nota1 + nota2 + nota3) / 3

# Passo 3: Verificar a situação do aluno com condicionais
if media >= 7.0:
    situacao = "Aprovado"
elif media >= 3.0:
    situacao = "Em Recuperação"
else:
    situacao = "Reprovado"

# Passo 4: Exibir o resultado com f-string para formatar a saída de forma clara
print(f"A média do aluno é {media:.2f}. Situação: {situacao}")