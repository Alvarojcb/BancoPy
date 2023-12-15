from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, numero_conta, titular, saldo=0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    def consultar_saldo(self):
        return self.saldo

    def __str__(self):
        return f"Conta: {self.numero_conta}, Titular: {self.titular}, Saldo: {self.saldo}"

class ContaCorrente(Conta):
    def __init__(self, numero_conta, titular, saldo=0.0, limite=1000.0):
        super().__init__(numero_conta, titular, saldo)
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

class ContaPoupanca(Conta):
    def __init__(self, numero_conta, titular, saldo=0.0, taxa_juros=0.01):
        super().__init__(numero_conta, titular, saldo)
        self.taxa_juros = taxa_juros

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def aplicar_juros(self):
        self.saldo += self.saldo * self.taxa_juros

# Exemplo de Uso:
conta_corrente = ContaCorrente(numero_conta=1, titular="João", saldo=1000.0, limite=500.0)
conta_poupanca = ContaPoupanca(numero_conta=2, titular="Maria", saldo=500.0, taxa_juros=0.02)

print(conta_corrente)
conta_corrente.depositar(200.0)
conta_corrente.sacar(1500.0)
print(conta_corrente)

print(conta_poupanca)
conta_poupanca.depositar(300.0)
conta_poupanca.sacar(100.0)
conta_poupanca.aplicar_juros()
print(conta_poupanca)
