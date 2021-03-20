"""
Polimorfismo é o princípio que permite que classes derivadas de uma mesma superclasse
tenham métodos iguais (de mesma assinatura) mas com comportamentos diferentes

Mesma assinatura = mesma quantidade e tipo de parâmetros

"""
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self, msg): pass


class B(A):
    def falar(self, msg):
        print(f'B está falando {msg}')


class C(A):
    def falar(self, msg):
        print(f'C está falando {msg}')


b = B()
c = C()

b.falar('sobre polimorfismo')
c.falar('sobre polimorfismo')
# mesmo método, comportamentos diferentes
