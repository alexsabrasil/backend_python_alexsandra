# Exercício 5 - Competição
candidatos = 3
avaliadores = 3
pontuacoes = [0] * candidatos

for av in range(1, avaliadores + 1):
    for c in range(1, candidatos + 1):
        nota = float(input(f"Nota do avaliador {av} para o candidato {c}: "))
        pontuacoes[c - 1] += nota
    print()

print("Pontuação final:")
for idx, total in enumerate(pontuacoes, start=1):
    if float(total).is_integer():
        print(f"Candidato {idx}: {int(total)}")
    else:
        print(f"Candidato {idx}: {total}")

maximo = max(pontuacoes)
vencedores = [i + 1 for i, p in enumerate(pontuacoes) if p == maximo]

if len(vencedores) == 1:
    print(f"Candidato {vencedores[0]} é o campeão!")
else:
    print("Empate! Disputa acirrada")
