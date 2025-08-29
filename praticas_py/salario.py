import os

# Função para limpar a tela (compatível com Windows, Linux, Mac)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para formatar valores em Real (R$)
def format_real(valor):
    s = f"{valor:,.2f}"            # ex: "1,234.56"
    s = s.replace(',', 'X').replace('.', ',').replace('X', '.')
    return f"R$ {s}"

# Programa principal
def main():
    while True:
        limpar_tela()
        print("="*40)
        print(" CÁLCULO DE SALÁRIO COM DESCONTOS ")
        print("="*40)
        print("1 - Calcular salário")
        print("0 - Sair")
        print("="*40)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            try:
                valor_hora = float(input("Informe o valor recebido por hora (ex: 25.50): ").replace(',', '.'))
                horas = float(input("Informe a quantidade de horas trabalhadas no mês (ex: 160): ").replace(',', '.'))
            except ValueError:
                print("\n⚠️ Entrada inválida! Use apenas números.\n")
                input("Pressione ENTER para continuar...")
                continue
            
            # Cálculos
            salario_bruto = valor_hora * horas
            ir = salario_bruto * 0.11
            inss = salario_bruto * 0.09
            sindicato = salario_bruto * 0.04
            total_descontos = ir + inss + sindicato
            salario_liquido = salario_bruto - total_descontos
            
            limpar_tela()
            print("="*40)
            print(" RELATÓRIO DE SALÁRIO ")
            print("="*40)
            print(f"+ Salário Bruto   : {format_real(salario_bruto)}")
            print(f"- IR (11%)        : {format_real(ir)}")
            print(f"- INSS (9%)       : {format_real(inss)}")
            print(f"- Sindicato (4%)  : {format_real(sindicato)}")
            print("-"*40)
            print(f"= Salário Líquido : {format_real(salario_liquido)}")
            print("="*40)
            
            input("\nPressione ENTER para voltar ao menu...")
        
        elif opcao == "0":
            limpar_tela()
            print("Saindo do programa... até logo! 👋")
            break
        else:
            print("\n⚠️ Opção inválida! Tente novamente.\n")
            input("Pressione ENTER para continuar...")

# Executa o programa
if __name__ == "__main__":
    main()
