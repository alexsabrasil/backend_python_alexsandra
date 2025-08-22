"""
Exercício 18: Substituir palavras em frase Peça uma frase e substitua uma palavra
específica por outra.

"""
def substituir_palavra(frase: str, palavra_antiga: str, palavra_nova: str) -> str:
    """
    Substitui todas as ocorrências de 'palavra_antiga' por 'palavra_nova' na frase.
    """
    return frase.replace(palavra_antiga, palavra_nova)


# Programa principal
frase = input("Digite uma frase: ")
palavra_antiga = input("Digite a palavra que deseja substituir: ")
palavra_nova = input("Digite a nova palavra: ")

frase_modificada = substituir_palavra(frase, palavra_antiga, palavra_nova)
print("Frase modificada:", frase_modificada)