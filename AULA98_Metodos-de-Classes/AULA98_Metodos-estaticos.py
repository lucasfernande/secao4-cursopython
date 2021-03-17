from datetime import datetime
from random import randint

class Pessoa:
    ano = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade):
         self.nome = nome
         self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nasc): # este método se refere a classe, e não a instância
        idade = cls.ano - ano_nasc
        return cls(nome, idade) # retorna a própria classe com base nos parâmetros desse método

    @staticmethod
    def gerarId():
        id = randint(10000, 99999)
        return id

print(Pessoa.gerarId()) # metodos estaticos não precisam nem da instância nem da classe para serem executadas
