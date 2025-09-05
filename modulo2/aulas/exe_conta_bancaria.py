class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular          # Público: qualquer um vê
        self._senha = "1234"           # Protegido: convenção "não mexer"
        self.__saldo = saldo_inicial   # Privado: bem escondido
    
    # Método público para depositar
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            print(f"Novo saldo: R$ {self.__saldo:.2f}")
        else:
            print("Valor inválido para depósito!")
    
    # Método público para sacar
    def sacar(self, valor, senha):
        if senha != self._senha:
            print("Senha incorreta!")
            return
        
        if valor > self.__saldo:
            print("Saldo insuficiente!")
            return
        
        if valor <= 0:
            print("Valor inválido!")
            return
        
        self.__saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado!")
        print(f"Saldo restante: R$ {self.__saldo:.2f}")
    
    # Método público para ver saldo
    def consultar_saldo(self, senha):
        if senha == self._senha:
            return f"Saldo atual: R$ {self.__saldo:.2f}"
        else:
            return "Senha incorreta!"

# Testando o encapsulamento
conta = ContaBancaria("Ana", 1000)

# Acesso público (OK)
print(f"Titular: {conta.titular}")

# Tentativas de acesso aos dados protegidos
print(conta.consultar_saldo("1234"))  # Correto
print(conta.consultar_saldo("4321"))  # Senha errada

# Operações seguras
conta.depositar(500)
conta.sacar(200, "1234")
conta.sacar(2000, "1234")  # Saldo insuficiente

# Tentativa de acesso direto (não recomendado)
# print(conta.__saldo)  # Isso geraria erro!