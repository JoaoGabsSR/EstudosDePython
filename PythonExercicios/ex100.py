from random import randint
from time  import sleep

def linha(dsn, n):
    print(f'{dsn}'*n)

def sumPares(list):
    s = 0
    for v in list:
        if v % 2 == 0:
           s += v

    return s

def randVal(q, i, f):
    valores = list()
    for c in range(0, q):
        valores.append(randint(i, f))

    return valores


val = randVal(5, 1, 10)

print('Sorteando 5 valores da lista: ', end='')
for v in val:
    print(v, end=' ')
    sleep(1)

print('PRONTO!')

linha('-', 60)

print(f'Somando os valores pares de {val}, temos {sumPares(val)}')
