
def exercicio1_torneio():
    print("=== Exercício 1: Torneio de Futebol ===")
    vitorias = empates = derrotas = 0
    for jogo in range(1, 6):  # 5 partidas
        gols_selecao = int(input(f"Gols da Seleção no jogo {jogo}: "))
        gols_adversario = int(input(f"Gols do adversário no jogo {jogo}: "))
        if gols_selecao > gols_adversario:
            vitorias += 1
        elif gols_selecao == gols_adversario:
            empates += 1
        else:
            derrotas += 1
        print()  # linha em branco para ficar igual ao exemplo
    print("=== Torneio de Futebol ===")
    print(f"Vitórias: {vitorias}")
    print(f"Empates: {empates}")
    print(f"Derrotas: {derrotas}")

def exercicio2_adivinhacao():
    print("=== Exercício 2: Jogo da Adivinhação ===")
    numero_secreto = random.randint(1, 20)
    tentativas = 5
    for tentativa in range(1, tentativas + 1):
        palpite = int(input("Adivinhe o número (1 a 20): "))
        if palpite == numero_secreto:
            print("Você acertou!")
            return
        elif palpite < numero_secreto:
            print("Muito baixo!")
        else:
            print("Muito alto!")
        print()
    print(f"Game over! O número era {numero_secreto}")

def exercicio3_ingressos():
    print("=== Exercício 3: Venda de Ingressos ===")
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

def exercicio4_quiz():
    print("=== Exercício 4: Quiz de Conhecimentos Gerais ===")
    perguntas = [
        {
            "pergunta": "1) Capital do Brasil?",
            "opcoes": ["1- São Paulo", "2- Brasília", "3- Rio de Janeiro"],
            "correta": 2
        },
        {
            "pergunta": "2) Planeta conhecido como planeta vermelho?",
            "opcoes": ["1- Marte", "2- Júpiter", "3- Vênus"],
            "correta": 1
        },
        {
            "pergunta": "3) Quem escreveu Dom Quixote?",
            "opcoes": ["1- Machado de Assis", "2- Cervantes", "3- Shakespeare"],
            "correta": 2
        },
        {
            "pergunta": "4) Qual o maior oceano?",
            "opcoes": ["1- Atlântico", "2- Pacífico", "3- Índico"],
            "correta": 2
        },
        {
            "pergunta": "5) Qual a cor da clorofila?",
            "opcoes": ["1- Verde", "2- Azul", "3- Amarela"],
            "correta": 1
        },
    ]
    pontos = 0
    for q in perguntas:
        print(q["pergunta"])
        print("  " + "  ".join(q["opcoes"]))
        resp = int(input("Sua resposta: "))
        if resp == q["correta"]:
            pontos += 1
        print()
    print(f"Pontuação final: {pontos}/5")
    if pontos == 5:
        print("Gênio!")
    elif pontos >= 3:
        print("Mandou bem!")
    elif pontos >= 1:
        print("Precisa estudar mais")
    else:
        print("Zerou o quiz")

def exercicio5_competicao():
    print("=== Exercício 5: Competição entre Candidatos ===")
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
        # Mostra sem .0 quando for inteiro
        if total.is_integer():
            print(f"Candidato {idx}: {int(total)}")
        else:
            print(f"Candidato {idx}: {total}")

    maximo = max(pontuacoes)
    vencedores = [i + 1 for i, p in enumerate(pontuacoes) if p == maximo]

    if len(vencedores) == 1:
        print(f"Candidato {vencedores[0]} é o campeão!")
    else:
        print("Empate! Disputa acirrada")

def exercicio6_situacao_aluno():
    print("=== Exercício 6: Situação do Aluno ===")
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    if nota >= 7:
        situacao = "APROVADO(A)"
    elif nota >= 5:
        situacao = "EM REPOSIÇÃO"
    else:
        situacao = "REPROVADO(A)"
    print(f"{nome} está {situacao}!")

def menu():
    while True:
        print("\n=== MENU LISTA 1 ===")
        print("1 - Torneio de Futebol")
        print("2 - Jogo da Adivinhação")
        print("3 - Venda de Ingressos")
        print("4 - Quiz de Conhecimentos Gerais")
        print("5 - Competição entre Candidatos")
        print("6 - Situação do Aluno")
        print("0 - Sair")
        opc = input("Escolha uma opção: ").strip()
        print()
        if opc == "1":
            exercicio1_torneio()
        elif opc == "2":
            exercicio2_adivinhacao()
        elif opc == "3":
            exercicio3_ingressos()
        elif opc == "4":
            exercicio4_quiz()
        elif opc == "5":
            exercicio5_competicao()
        elif opc == "6":
            exercicio6_situacao_aluno()
        elif opc == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

