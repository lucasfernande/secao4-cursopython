"""
class Arquivo:
    def __init__(self, arquivo, modo):
        print('abriu o arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self): # retorna o que vai para o 'as file' do with
        print('retornou o arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('fechou o arquivo')
        self.arquivo.close()
        # ... Tratar exceção
        return True

with Arquivo('file.txt', 'a+') as file:
    file.write('Teste\n')
"""

from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()

with abrir('file.txt', 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3')