import re


def removerCaracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)  # o que for diferente de 0 a 9 será removido da string


def removerDigitos(cnpj):
    novoCNPJ = cnpj[:-2]
    return novoCNPJ

def calculoPrimeiroDigito(cnpj):
    total = 0
    i = 5

    for v in cnpj:
        total += (i * int(v))
        i -= 1

        if i < 2:
            i = 9

    primeiroDigito = 11 - (total % 11)
    primeiroDigito = 0 if primeiroDigito > 9 else primeiroDigito

    cnpj += str(primeiroDigito)
    return cnpj

def calculoSegundoDigito(cnpj):
    total = 0
    i = 6

    for v in cnpj:
        total += (i * int(v))
        i -= 1

        if i < 2:
            i = 9

    segundoDigito = 11 - (total % 11)
    segundoDigito = 0 if segundoDigito > 9 else segundoDigito

    cnpj += str(segundoDigito)
    return cnpj

def validar(CNPJInput, CNPJCalculado):
    if CNPJInput[-2:] == CNPJCalculado[-2:]: # comparando os dois ultimos digitos do cnpj digitado e do calculado
        return True

    return False