class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.contas = []
        self.clientes = []

    def insert_conta(self, conta):
        self.contas.append(conta)

    def insert_cliente(self, cliente):
        self.clientes.append(cliente)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente.conta not in self.contas:
            return False

        if cliente.conta.agencia not in self.agencias:
            return False

        return True