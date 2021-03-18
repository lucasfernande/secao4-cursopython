from classes import Cliente

cliente1 = Cliente('Lucas', 19)
cliente1.inserir_endereco('São Paulo', 'SP')
cliente1.listar_enderecos()
print()

cliente2 = Cliente('Maria', 25)
cliente2.inserir_endereco('Salvador', 'BA')
cliente2.inserir_endereco('Feira de Santana', 'BA')
cliente2.listar_enderecos()
del cliente2 # quando o cliente 2 for apagado, os endereços também serão, pois a classe endereco PERTENCE a classe cliente
print()

cliente3 = Cliente('Carlos', 23)
cliente3.inserir_endereco('Belo Horizonte', 'MG')
cliente3.inserir_endereco('Montes Claros', 'MG')
cliente3.listar_enderecos()
print()

print('#' * 100) # fim do codigo


