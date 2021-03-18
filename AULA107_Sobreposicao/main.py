from classes import *

cliente = Cliente('Lucas', 19)
cliente.falar()

clienteVIP = ClienteVIP('André', 'Lima', 25)
print(clienteVIP.sobrenome)
clienteVIP.falar() # a função falar se comporta de forma diferente, pois foi sobrescrita