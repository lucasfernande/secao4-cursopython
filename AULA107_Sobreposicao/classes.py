class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = __class__.__name__

    def falar(self):
        print(f'{self.nome_classe} está falando')

class Cliente(Pessoa): # um cliente É uma pessoa
    def falar(self):
        print(f'{__class__.__name__} está falando')

class ClienteVIP(Cliente):
    def __init__(self, nome, sobrenome, idade):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome # criando um atributo APENAS da classe ClienteVIP

    def falar(self):
        super().falar() # chamando falar() da classe pai (Cliente)
        print(f'{__class__.__name__} está falando')