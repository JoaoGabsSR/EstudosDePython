# achando fatorial usando o while
n = int(input('Digite um valor para que seja calculado o fatorial do mesmo: '))
c = n
fat = 1

print(f'Calculando {n}! ', end='')
while c >= 2:
    print(f'{c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')

    fat *= c
    c -= 1

print(f'{fat}')

print('=-=' * 15)

# achando o fatorial usando modulos
from math import factorial

n = int(input('Digite um valor para que seja calculado o fatorial do mesmo: '))
f = factorial(n)

print(f'{n}! = {f}')
