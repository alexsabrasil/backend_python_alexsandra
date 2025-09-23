# cliente.py - construtor
class Cliente:
    def __init__(self, id_cliente, nome):
        self.id_cliente = id_cliente
        self.nome = nome

    def __str__(self):
        return f"Cliente {self.id_cliente} = {self.nome}"


# Uso
if __name__ == "__main__":
    c1 = Cliente(1, "Maria Torres")
    c2 = Cliente(2, "João Gomes")

    print(c1)
    print(c2)
