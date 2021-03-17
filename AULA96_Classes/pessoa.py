class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome # o nome da classe recebe o nome passado como parâmetro
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'Não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} já está falando')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def pararFalar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.comendo: # verificando se a pessoa já está comendo
            print(f'{self.nome} já está comendo')
            return

        if self.falando:
            print(f'Não pode falar comendo')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def terminarComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} terminou de comer')
        self.comendo = False