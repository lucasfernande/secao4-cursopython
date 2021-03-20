class MeuErroError(Exception):
    pass

def testar():
    raise MeuErroError('Meu erro personalizado')


try:
    testar()
except MeuErroError as error:
    print(f'Erro: {error}')
