# controle.py

class SistemaController:
    def __init__(self):
        self.clientes = []
        self.compras = []

    # Clientes
    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        return self.clientes

    # Compras
    def adicionar_compra(self, compra):
        self.compras.append(compra)

    def listar_compras(self):
        return self.compras
