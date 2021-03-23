from banco import Banco
from cliente import Cliente
from conta import CC, CP

banco = Banco()

cl1 = Cliente('Mariana', 21)
cl2 = Cliente('Luiz', 32)
cl3 = Cliente('Jorge', 26)

c1 = CP(1111, 6192, 0)
c2 = CC(3333, 5874, 0)
c3 = CP(2222, 1415, 0)

cl1.insert_conta(c1)
cl2.insert_conta(c2)
cl3.insert_conta(c3)

banco.insert_cliente(cl1)
banco.insert_conta(c1)

if banco.autenticar(cl1):
    cl1.conta.depositar(600)
    cl1.conta.sacar(200)
else:
    print('Cliente não autenticado')

print('#' * 25)
banco.insert_cliente(cl2)
banco.insert_conta(c2)

if banco.autenticar(cl2):
    cl2.conta.depositar(600)
    cl2.conta.sacar(800)
else:
    print('Cliente não autenticado')

