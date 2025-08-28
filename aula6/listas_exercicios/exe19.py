# Função reuso
def calcula_media(n, m):
    return (n+m) / 2

sair = 1
while sair == 1:

    # Entrada
    nome_estudante = (input("Digite o nome do estudante:  "))
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))


    # Processamento
    media = calcula_media(nota1, nota2)  # Passando as notas separadas


    # Saída
    print('O nome do estudante eh:', nome_estudante)
    print('A média do estudante eh:', media)

    # Opção de sair ou continuar
    sair = input('Digite C para continuar e S para sair: ').upper()  # Garantir que seja 'C' ou 'S'
    if sair == 'S':
        break



