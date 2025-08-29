# Exercício 1 - Torneio de Futebol
vitorias = 0
empates = 0
derrotas = 0

for jogo in range(1, 6):  # 5 partidas
    gols_selecao = int(input(f"Gols da Seleção no jogo {jogo}: "))
    gols_adversario = int(input(f"Gols do adversário no jogo {jogo}: "))

    if gols_selecao > gols_adversario:
        vitorias += 1
    elif gols_selecao == gols_adversario:
        empates += 1
    else:
        derrotas += 1

print("\n=== Torneio de Futebol ===")
print(f"Vitórias: {vitorias}")
print(f"Empates: {empates}")
print(f"Derrotas: {derrotas}")
