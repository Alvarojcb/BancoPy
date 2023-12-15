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

    def solicitar_emprestimo(self, valor):
        limite_emprestimo = 2 * self.saldo  # Exemplo: Limite de empréstimo de 2 vezes o saldo
        if valor <= limite_emprestimo:
            print(f"Solicitação de empréstimo de R${valor} aprovada!")
            self.saldo += valor
        else:
            print(f"Solicitação de empréstimo de R${valor} negada. Limite excedido.")

# Exemplo de Uso:
conta_corrente = ContaCorrente(numero_conta=1, titular="João", saldo=1000.0, limite=500.0)

print(conta_corrente)
conta_corrente.depositar(200.0)
conta_corrente.sacar(1500.0)
print(conta_corrente)

conta_corrente.solicitar_emprestimo(800.0)
conta_corrente.solicitar_emprestimo(1500.0)
print(conta_corrente)
