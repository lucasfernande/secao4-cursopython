class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome # o nome da classe recebe o nome passado como parâmetro
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo: # verificando se a pessoa já está comendo
            print(f'{self.nome} já está comendo')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def terminarComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} terminou de comer')
        self.comendo = False