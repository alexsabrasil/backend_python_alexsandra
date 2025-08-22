"""
Exercício 15: Função para calcular fatorial Crie uma função que calcule o fatorial de
um número.

"""
def fatorial(n: int) -> int:
    """
    Calcula o fatorial de um número n (n!).
    Retorna 1 se n for 0.
    """
    if n < 0:
        return None  # fatorial não existe para números negativos

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i  # resultado = resultado * i
    return resultado


# Programa principal
num = int(input("Digite um número para calcular o fatorial: "))
fat = fatorial(num)

if fat is not None:
    print(f"O fatorial de {num} é {fat}.")
else:
    print("Fatorial não definido para números negativos.")
