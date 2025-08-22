"""""
Exercício 4: Tabuada com for Peça um número e mostre sua tabuada de 1 a 10
usando for.
"""
n = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")