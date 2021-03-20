from classes.cp import ContaPoupanca
from classes.cc import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(50)
cp.depositar(20)
cp.sacar(10)
cp.sacar(25)
cp.sacar(70)

print('#' * 20)

cc = ContaCorrente(1111, 2223, 0, 100)
cc.depositar(200)
cc.sacar(150)
cc.sacar(100)
cc.sacar(120)
cc.depositar(1000)
