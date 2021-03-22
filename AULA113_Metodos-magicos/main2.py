class A:
    def __init__(self):
        print('INIT')

    def __call__(self, *args, **kwargs):  # o método call faz a classe se comportar como uma função
        resultado = 1

        for i in args:
            resultado *= i

        return resultado

    def __setattr__(self, key, value): # será sempre chamado quando um atributo for setado
        print(f'Atributo: {key}, Valor: {value}')

    def __del__(self): # será chamado quando o objeto não for mais utilizado (não recomendado)
        print('Lixo coletado')

    def __str__(self): # é executado quando tentamos dar um print na classe
        return 'Classe A'

    def __len__(self): # possibilita o uso do método len() na classe
        return 55

a = A()
print(a) # será chamado o método __str__


var = a(1, 2, 3, 4, 5)  # chamando a classe como uma função
# print(var)

a.nome = 'Lucas' # será chamado o método __setattr__
a.idade = 19 # será chamado o método __setattr__

print(len(a))

