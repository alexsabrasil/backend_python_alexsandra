# Mini sistema interativo com tipos de dados + salvamento em arquivo

respostas = {
    "nome": None,
    "idade": None,
    "idade_futura": None,
    "preco": None,
    "preco_desconto": None,
    "matriculado": None
}

def menu():
    print("\n===== MENU INTERATIVO =====")
    print("1. Digitar nome (string)")
    print("2. Digitar idade (int)")
    print("3. Digitar preço do produto (float)")
    print("4. Está matriculado? (boolean)")
    print("5. Sair e salvar respostas")
    print("===========================\n")

while True:
    menu()
    opcao = input("Escolha uma opção (1 a 5): ")

    if opcao == "1":
        nome = input("Digite seu nome: ")
        respostas["nome"] = nome
        print(f"🔹 Olá, {nome}! Seja bem-vindo(a) 😊")

    elif opcao == "2":
        idade = int(input("Digite sua idade: "))
        respostas["idade"] = idade
        respostas["idade_futura"] = idade + 10
        print(f"🔸 Daqui a 10 anos, você terá {respostas['idade_futura']} anos.")

    elif opcao == "3":
        preco = float(input("Digite o preço do produto (R$): "))
        desconto = preco * 0.10
        preco_com_desconto = preco - desconto
        respostas["preco"] = preco
        respostas["preco_desconto"] = preco_com_desconto
        print(f"🔹 O valor com 10% de desconto é: R$ {preco_com_desconto:.2f}")

    elif opcao == "4":
        resposta = input("Você está matriculado? (sim/não): ").strip().lower()
        matriculado = True if resposta == "sim" else False
        respostas["matriculado"] = matriculado
        print(f"🔸 Status de matrícula: {matriculado}")

    elif opcao == "5":
        print("\n📁 Salvando suas respostas no arquivo respostas.txt...\n")
        with open("respostas.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("=== RESPOSTAS DO USUÁRIO ===\n")
            if respostas["nome"]:
                arquivo.write(f"Nome: {respostas['nome']}\n")
            if respostas["idade"]:
                arquivo.write(f"Idade: {respostas['idade']}\n")
                arquivo.write(f"Idade daqui a 10 anos: {respostas['idade_futura']}\n")
            if respostas["preco"]:
                arquivo.write(f"Preço original: R$ {respostas['preco']:.2f}\n")
                arquivo.write(f"Preço com 10% de desconto: R$ {respostas['preco_desconto']:.2f}\n")
            if respostas["matriculado"] is not None:
                arquivo.write(f"Matriculado: {respostas['matriculado']}\n")
        print("✅ Respostas salvas com sucesso. Programa encerrado!\n")
        break

    else:
        print("⚠️ Opção inválida. Tente novamente.")