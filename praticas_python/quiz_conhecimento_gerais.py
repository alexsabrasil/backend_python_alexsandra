# Exercício 4 - Quiz
perguntas = [
    {"pergunta": "1) Capital do Brasil?",
     "opcoes": ["1- São Paulo", "2- Brasília", "3- Rio de Janeiro"],
     "correta": 2},
    {"pergunta": "2) Planeta conhecido como planeta vermelho?",
     "opcoes": ["1- Marte", "2- Júpiter", "3- Vênus"],
     "correta": 1},
    {"pergunta": "3) Quem escreveu Dom Quixote?",
     "opcoes": ["1- Machado de Assis", "2- Cervantes", "3- Shakespeare"],
     "correta": 2},
    {"pergunta": "4) Qual o maior oceano?",
     "opcoes": ["1- Atlântico", "2- Pacífico", "3- Índico"],
     "correta": 2},
    {"pergunta": "5) Qual a cor da clorofila?",
     "opcoes": ["1- Verde", "2- Azul", "3- Amarela"],
     "correta": 1},
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
