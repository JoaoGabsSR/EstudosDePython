def menuPrincipal(dict):
    titulo('MENU PRINCIPAL')

    for k, v in dict.items():
        print(f'\033[1;34m{k}\033[m \033[1m-\033[m \033[1;33m{v}\033[m')

    linha('-', (len('MENU PRINCIPAL') + 15))


def titulo(txt):
    tam = len(txt) + 15

    print('~'*tam)
    print(f'{txt.center(tam)}')
    print('~'*tam)


def linha(charc, quant):
    print(f'{charc}'*quant)
