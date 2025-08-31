"""
Exercício 16: Contar palavras em uma frase (função de string) Peça uma frase e
mostre quantas palavras ela possui.

"""
def contar_palavras(frase: str) -> int:
    """
    Recebe uma frase e retorna a quantidade de palavras.
    """
    # split() separa a frase nos espaços
    palavras = frase.split()
    return len(palavras)


# Programa principal
entrada = input("Digite uma frase: ")
quantidade = contar_palavras(entrada)
print(f"A frase digitada possui {quantidade} palavras.")