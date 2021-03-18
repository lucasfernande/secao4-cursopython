"""
public, protected e private não existem em python

_ um underline, protected ou private (ainda pode ser acessado fora da classe)
__ dois underline, private (pode ser acessado com _NOMEDACLASSE__nomeatributo)

"""

class BD:
    def __init__(self):
        self.__dados = {} # dicionario simulando um banco de dados

    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(f'{id} - {nome}')

    def insert_cliente(self, id, nome):
        if not 'clientes' in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def remove_cliente(self, id):
        del self.__dados['clientes'][id]

    @property
    def dados(self):
        return self.__dados

bd = BD()
bd.insert_cliente(1, 'Otávio')
bd.insert_cliente(2, 'Renata')

bd.__dados = 'Outro valor' # a variavel dados não está sendo acessada e sim criada novamente
print(bd.__dados)
bd.listar_clientes() # a lista de clientes continua funcionando

print(bd._BD__dados) # acessando um valor private

print(bd.dados) # acessando o atributo dados através do getter

