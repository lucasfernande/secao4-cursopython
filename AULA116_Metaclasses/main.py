"""
metaclasses são "classes" que criam classes
"""

class Meta(type): # metaclasse
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace: # forçando que o método exista na classe B
            print(f'Crie o método b_fala na classe {name}')
        else:
            if not callable(namespace['b_fala']):
                print('b_fala precisa ser um método') # evita que b_fala seja um atributo, precisa ser uma função

        if 'teste' in namespace:
            print(f'{name} tentou sobreescrever um atributo') # evitando que um atributo seja sobreescrito por uma classe filha
            del namespace['teste']

        return type.__new__(mcs, name, bases, namespace)

class A(metaclass=Meta):
    teste = 'Value 1'
    def fala(self):
        self.b_fala()

class B(A):
    teste = 'Value 2'
    # def b_fala(self): # se esse método não existir, vai gerar um erro na classe A
    #     print('Oi')


b = B()
print(b.teste)

print()
print()

# ----------- Criando uma classe com metaclasses ------------

C = type('C', (), {'attr': 'Teste Atributo'})

c = C()
print(c.attr)
