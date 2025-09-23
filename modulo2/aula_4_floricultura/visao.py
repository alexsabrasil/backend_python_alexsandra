# visao.py
from modelo import Cliente, Compra
from controle import SistemaController

def main():
    sistema = SistemaController()

    # Criando clientes
    c1 = Cliente(1, "Maria Silva")
    c2 = Cliente(2, "João Gomes")

    sistema.adicionar_cliente(c1)
    sistema.adicionar_cliente(c2)

    # Criando compras
    compra1 = Compra(101, "2025-09-15", "Notebook", 1, 3500.00, 1)
    compra2 = Compra(102, "2025-09-16", "Mouse", 2, 150.00, 2)

    sistema.adicionar_compra(compra1)
    sistema.adicionar_compra(compra2)

    # Exibindo resultados
    print("--- CLIENTES ---")
    for cliente in sistema.listar_clientes():
        print(cliente)

    print("\n--- COMPRAS ---")
    for compra in sistema.listar_compras():
        print(compra)

if __name__ == "__main__":
    main()

