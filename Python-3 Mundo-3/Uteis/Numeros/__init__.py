def fatorial(n=1):
    """
    -> Calcula o fatorial de um número inteiro qualquer
    :param n: número(opcional) que terá seu fatorial calculado
    :return: valor do fatorial do número passado
    """

    f = 1

    for c in range(n, 0, -1):
        f *= c

    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3
