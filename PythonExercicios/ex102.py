def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: o número a ser calculado
    :param show: Mostrar a conta ou não
    :return: O valor do fatorial de um número n
    """

    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} ', end='')

            if c != 1:
                print('x ', end='')
            else:
                print(f'= ', end='')

        f *= c

    return f


help(fatorial)
print(fatorial(5, show=True))
