
class A:
    v = 123 # variavel de classe

    def __init__(self):
        # pass
        self.v = 321 # variavel de instância


a1 = A()
a2 = A()

# A.v = 'Alterado'

print(a1.v) # as instâncias tem o v 321
print(a2.v)
print(A.v) # apenas a classe tem o v 123
