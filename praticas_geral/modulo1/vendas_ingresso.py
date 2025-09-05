# Exercício 3 - Venda de Ingressos
pessoas = int(input("Quantas pessoas vão ao show? "))
total = 0

for i in range(1, pessoas + 1):
    idade = int(input(f"Idade da pessoa {i}: "))
    if idade <= 12:
        print("Entrada grátis")
    elif 13 <= idade <= 17:
        print("Meia entrada (R$ 10)")
        total += 10
    else:
        print("Ingresso inteiro (R$ 20)")
        total += 20
    print()

print(f"Total arrecadado: R$ {total}")
