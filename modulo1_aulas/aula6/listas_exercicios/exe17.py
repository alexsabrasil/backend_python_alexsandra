"""
Exercício 17: Palíndromo (string invertida) Crie uma função que verifique se uma
palavra é um palíndromo

"""
def eh_palindromo(palavra: str) -> bool:
    """
    Verifica se uma palavra é um palíndromo.
    Retorna True se for, False caso contrário.
    """
    palavra = palavra.lower()  # ignora maiúsculas/minúsculas
    return palavra == palavra[::-1]  # compara com a string invertida


# Programa principal
entrada = input("Digite uma palavra: ")

if eh_palindromo(entrada):
    print(f'"{entrada}" é um palíndromo.')
else:
    print(f'"{entrada}" NÃO é um palíndromo.')