def aumentar(valor=0, porcentagem=0, format=False):
    if format:
        return moeda(valor + (valor * (porcentagem/100)))
    else:
        return valor + (valor * (porcentagem/100))


def diminuir(valor=0, porcentagem=0, format=False):
    if format:
        return moeda(valor - (valor * (porcentagem / 100)))
    else:
        return valor - (valor * (porcentagem/100))


def dobrar(valor=0, format=False):
    if format:
        return moeda(valor * 2)
    else:
        return valor * 2


def metade(valor=0, format=False):
    if format:
        return moeda(valor / 2)
    else:
        return valor / 2


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>.2f}'


def resumo(valor=0, porcentagemup=0, porcentagemdown=0):
    print('-'*29)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 29)

    print(f'{"Preço Analisado: "}  \t{moeda(valor):>5}')
    print(f'{"Dobro do Preço: "}  \t{dobrar(valor, True):>5}')
    print(f'{"Metade do Preço: "} \t {metade(valor, True):>5}')
    print(f'{f"{porcentagemup}% de Aumento: "}  \t{aumentar(valor, porcentagemup, True)}')
    print(f'{f"{porcentagemup}% de Redução: "}  \t{diminuir(valor, porcentagemdown, True)}')
    print('-' * 29)
