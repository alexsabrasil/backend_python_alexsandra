"""
Exercício 12: Soma dos números de 1 a 100 (for) Some todos os números de 1 a
100 usando for.

"""
soma = 0  # acumulador

for numero in range(1, 101):  # vai de 1 até 100
    soma += numero  # soma = soma + numero

print("A soma dos números de 1 a 100 é:", soma)