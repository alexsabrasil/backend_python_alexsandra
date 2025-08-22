"""
Exercício 14: Função para verificar número primo Crie uma função que receba um
número e retorne se ele é primo.

"""

def eh_primo(numero: int) -> bool:
    """
    Retorna True se o número for primo, False caso contrário.
    """
    if numero <= 1:
        return False  # números menores ou iguais a 1 não são primos
    
    # verifica se algum número de 2 até sqrt(numero) divide o número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:  # se dividir exatamente
            return False
    return True  # se não encontrou divisor, é primo


# Programa principal
n = int(input("Digite um número: "))

if eh_primo(n):
    print(f"{n} é primo.")
else:
    print(f"{n} NÃO é primo.")
