from abc import ABC, abstractmethod
# Abstract Base Class
"""
Classes abstratas não podem ser instanciadas, elas servem de base para outras classes

"""

class A(ABC):
    @abstractmethod
    def falar(self):
        pass

class B(A):

    def falar(self):
        print('Oi')

b = B()
b.falar()
