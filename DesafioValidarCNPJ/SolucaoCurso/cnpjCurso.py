import re

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = apenasNumeros(cnpj)

    try:
        if sequencia(cnpj):  # se for uma sequência, não será validado
            print('Erro: é uma sequência')
            return False
        novoCNPJ = calcularDigitos(cnpj, 1)
        novoCNPJ = calcularDigitos(novoCNPJ, 2)
    except Exception as e:
        return False

    if novoCNPJ == cnpj:
        return True
    else:
        return False

def calcularDigitos(cnpj, digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novoCNPJ = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novoCNPJ = cnpj
    else:
        return None

    total = 0
    for i, v in enumerate(regressivos):
        total += int(cnpj[i]) * v

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0

    novoCNPJ += str(digito)
    return novoCNPJ


def sequencia(cnpj):  # função para verificar se o cnpj não é uma sequência, para evitar que o programa seja burlado
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False


def apenasNumeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)
