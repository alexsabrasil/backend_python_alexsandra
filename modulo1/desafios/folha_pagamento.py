"""
Nova implementação. 
● Adicionar a variável nome do funcionário 
● Pesquisar sobre alíquota IR e INSS 
● Implementar o cálculo do IR e do INSS 
● Implementar as restrições nos campos, estes não podem estar vazios ou em branco. 
● Criar as funções (cadastrar, excluir, alterar, listar) 
● O programa deve funcionar tantas vezes quanto for necessário. 

Sistema Folha de Pagamento 
● O programa deve oferecer uma opção para o usuário listar todos os funcionários cadastrados.
● O programa deve disponibilizar uma opção para o usuário sair do Sistema. 
● Ao final, exibir a mensagem: Programa finalizado com sucesso!!!
"""


# Sistema Folha de Pagamento

funcionarios = []  # lista para armazenar os funcionários


def validar_campo(valor, nome_campo):
    if not valor.strip():
        raise ValueError(f"⚠️ O campo '{nome_campo}' não pode estar vazio!")
    return valor


def calcular_inss(salario_bruto):
    if salario_bruto <= 1412.00:
        return salario_bruto * 0.075
    elif salario_bruto <= 2666.68:
        return salario_bruto * 0.09
    elif salario_bruto <= 4000.03:
        return salario_bruto * 0.12
    else:
        return salario_bruto * 0.14


def calcular_ir(salario_bruto):
    if salario_bruto <= 2259.20:
        return 0
    elif salario_bruto <= 2826.65:
        return salario_bruto * 0.075
    elif salario_bruto <= 3751.05:
        return salario_bruto * 0.15
    elif salario_bruto <= 4664.68:
        return salario_bruto * 0.225
    else:
        return salario_bruto * 0.275


def cadastrar_funcionario():
    try:
        nome = validar_campo(input("Digite o nome do funcionário: "), "Nome")
        valor_hora = float(validar_campo(input("Digite o valor da hora (R$): "), "Valor da hora"))
        horas_trabalhadas = float(validar_campo(input("Digite a quantidade de horas trabalhadas: "), "Horas trabalhadas"))

        salario_bruto = valor_hora * horas_trabalhadas
        inss = calcular_inss(salario_bruto)
        ir = calcular_ir(salario_bruto)
        sindicato = salario_bruto * 0.05
        salario_liquido = salario_bruto - (inss + ir + sindicato)

        funcionario = {
            "nome": nome,
            "salario_bruto": salario_bruto,
            "inss": inss,
            "ir": ir,
            "sindicato": sindicato,
            "salario_liquido": salario_liquido
        }

        funcionarios.append(funcionario)
        print(f"\n✅ Funcionário {nome} cadastrado com sucesso!\n")

    except ValueError as e:
        print(e)


def listar_funcionarios():
    if not funcionarios:
        print("\n⚠️ Nenhum funcionário cadastrado.\n")
        return

    for i, f in enumerate(funcionarios, 1):
        print(f"\n=== Funcionário {i} - {f['nome']} ===")
        print(f"(+) Salário Bruto    : R$ {f['salario_bruto']:.2f}")
        print(f"(-) IR               : R$ {f['ir']:.2f}")
        print(f"(-) INSS             : R$ {f['inss']:.2f}")
        print(f"(-) Sindicato (5%)   : R$ {f['sindicato']:.2f}")
        print(f"(=) Salário Líquido  : R$ {f['salario_liquido']:.2f}")
        print("=" * 35)


def alterar_funcionario():
    listar_funcionarios()
    if not funcionarios:
        return

    try:
        indice = int(input("Digite o número do funcionário para alterar: ")) - 1
        if 0 <= indice < len(funcionarios):
            funcionarios.pop(indice)
            print("⚠️ Insira os novos dados do funcionário:")
            cadastrar_funcionario()
        else:
            print("⚠️ Funcionário não encontrado.")
    except ValueError:
        print("⚠️ Entrada inválida.")


def excluir_funcionario():
    listar_funcionarios()
    if not funcionarios:
        return

    try:
        indice = int(input("Digite o número do funcionário para excluir: ")) - 1
        if 0 <= indice < len(funcionarios):
            removido = funcionarios.pop(indice)
            print(f"\n🗑️  Funcionário: {removido['nome']} excluído com sucesso!\n")
        else:
            print("⚠️ Funcionário não encontrado.")
    except ValueError:
        print("⚠️ Entrada inválida.")


# Programa principal
while True:
    print("\n=== SISTEMA FOLHA DE PAGAMENTO ===")
    print("1 - Cadastrar funcionário")
    print("2 - Alterar funcionário")
    print("3 - Excluir funcionário")
    print("4 - Listar funcionários")
    print("5 - Sair")
    opcao = input("Digite sua opção: ")

    if opcao == "1":
        cadastrar_funcionario()
    elif opcao == "2":
        alterar_funcionario()
    elif opcao == "3":
        excluir_funcionario()
    elif opcao == "4":
        listar_funcionarios()
    elif opcao == "5":
        print("\n✅ Programa finalizado com sucesso!!!\n")
        break
    else:
        print("⚠️ Opção inválida, tente novamente!")
