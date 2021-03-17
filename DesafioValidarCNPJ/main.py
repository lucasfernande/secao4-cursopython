import cnpj

CNPJInput = '04.252.011/0001-10'
CNPJInput = cnpj.removerCaracteres(CNPJInput)

novoCNPJ = cnpj.removerDigitos(CNPJInput) # pegando o cnpj sem os dígitos

CNPJCalculado = cnpj.calculoPrimeiroDigito(novoCNPJ) # calculando o primeiro digito
CNPJCalculado = cnpj.calculoSegundoDigito(CNPJCalculado) # calculando o segundo digito

valido = cnpj.validar(CNPJInput, CNPJCalculado)

if valido:
    print('CNPJ Válido')
else:
    print('CNPJ Inválido')


