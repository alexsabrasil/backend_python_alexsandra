# Exercício 2 - Jogo da Adivinhação
numero_secreto = random.randint(1, 20)
tentativas = 5

for tentativa in range(1, tentativas + 1):
    palpite = int(input("Adivinhe o número (1 a 20): "))

    if palpite == numero_secreto:
        print("Você acertou!")
        break
    elif palpite < numero_secreto:
        print("Muito baixo!")
    else:
        print("Muito alto!")

else:
    # Só entra aqui se o laço não for interrompido por 'break'
    print(f"Game over! O número era {numero_secreto}")
