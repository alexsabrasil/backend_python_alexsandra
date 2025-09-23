class Cliente:
    def __init__(self, id_cliente, nome):
        self.id_cliente = id_cliente
        self.nome = nome

    def __str__(self):
        return f"Cliente(id={self.id_cliente}, nome={self.nome})"


class Produto:
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco  # preço atual do produto

    def __str__(self):
        return f"Produto(id={self.id_produto}, nome={self.nome}, preço={self.preco:.2f})"


class ItensCompra:
    def __init__(self, produto, quantidade, preco_unitario):
        self.produto = produto  # composição (cada item está ligado a um produto)
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario  # preço no momento da compra

    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return (f"{self.quantidade}x {self.produto.nome} "
                f"(R${self.preco_unitario:.2f} cada) - Subtotal: R${self.subtotal():.2f}")


class Compra:
    def __init__(self, id_compra, data_compra, cliente):
        self.id_compra = id_compra
        self.data_compra = data_compra
        self.cliente = cliente  # agregação (compra depende de um cliente)
        self.itens = []  # composição (itens pertencem à compra)

    def adicionar_item(self, produto, quantidade):
        # O preço unitário deve ser "congelado" no momento da compra
        item = ItensCompra(produto, quantidade, produto.preco)
        self.itens.append(item)

    def total(self):
        return sum(item.subtotal() for item in self.itens)

    def __str__(self):
        itens_str = "\n  ".join(str(item) for item in self.itens)
        return (f"Compra(id={self.id_compra}, data={self.data_compra}, cliente={self.cliente.nome})\n"
                f"Itens:\n  {itens_str}\nTotal: R${self.total():.2f}")

# Criando cliente
c1 = Cliente(1, "Alê Tavares")

# Criando produtos
p1 = Produto(101, "Rosa Vermelha", 5.0)
p2 = Produto(102, "Orquídea", 20.0)

# Criando compra
compra1 = Compra(1, "2025-09-23", c1)

# Adicionando itens
compra1.adicionar_item(p1, 3)  # 3 rosas
compra1.adicionar_item(p2, 1)  # 1 orquídea

print(compra1)