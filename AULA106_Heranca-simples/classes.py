class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cliente(Pessoa): # um cliente É uma pessoa
    pass

class Aluno(Pessoa): # um aluno É uma pessoa
    pass