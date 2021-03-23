from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.detalhar()

    def detalhar(self):
        print(f'Novo saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor): pass


class CP(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhar()


class CC(Conta):
    def __init__(self, agencia, numero, saldo, limite=100):
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhar()