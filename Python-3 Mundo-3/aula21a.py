#help(print)
#print(input.__doc__)
#help(input)


def contagem(start: int, end: int, jump: int):
    """
    -> Faz uma contagem e mostar na tela.
    -> Caso o parametro jump seja 0, seu valor será trocado por 1.
    :param start: inicio da contagem
    :param end: fim da contagem
    :param jump: passo da contagem
    :return: sem retorno
    """

    if jump == 0:
        print('Erro! Não se pode contar e 0 em 0, o valor da contagem será de 1 em 1.')
        jump = 1

    if start < end:
        n = start

        while n <= end:
            print(n, end=' ')
            n += jump
    else:
        n = start

        while n >= end:
            print(n, end=' ')
            n -= jump

def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores opcionais e mostra o resultado na tela
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: sem retorno
    """

    s = a + b + c
    print(f'A soma vale {s}')

def teste(b=0):
    if b == 0:
        x = 8
        print(f'Na função teste, n vale {n}')
        print(f'Na função teste, x vale {x}')
    else:
        global a
        a = 8
        b += 4
        c = 2
        print(f'A dentro vale {a}')
        print(f'B dentro vale {b}')
        print(f'C dentro vale {c}')

def newSum(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores opcionais e mostra o resultado na tela
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: retorna o valor da soma dos valores
    """

    s = a + b + c
    return s

def fatorial(n = 1):
    """
    -> Calcula o fatorial de um número inteiro qualquer
    :param n: número(opcional) que terá seu fatorial calculado
    :return: valor do fatorial do número passado
    """

    f = 1

    for c in range(n, 0, -1):
        f *= c

    return f


#help(contagem)
#contagem(0, 10, 2)

#help(somar)
#somar(3, 2, 5)
#somar(8, 4)
#somar()

#n = 2
#print(f'No programa principal, n vale {n}')
#teste()
#print(f'No programa principal, x vale {x}')

#a = 5
#teste(a)
#print(f'A fora vale {a}')

#r1 = newSum(3, 2, 5)
#r2 = newSum(1, 7)
#r3 = newSum(4)
#print(f'O resultado das somas são: {r1}, {r2}, {r3}')

num = int(input('Digite um número: '))
print(f'O fatorial de {num} é {fatorial(num)}')
