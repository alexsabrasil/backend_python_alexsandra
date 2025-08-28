# Função reuso
def calcula_media(n, m):
    return (n+m) / 2

# Entrada
nome_estudante = (input("Digite o nome do estudante:  "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


# Processamento
#media = (nota1 + nota2) / 2
media = calcula_media(nota1 + nota2)


# Saída
print('O nome do estudante eh:  ' , nome_estudante)
print('A média do estudante eh:  ' , media)

# Contador = 1

# Enquanto 
#While 

