from datetime import datetime

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


# p1 = Pessoa('João', 28)
p1 = Pessoa.por_ano_nascimento('João', 1993)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
