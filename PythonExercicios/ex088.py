from random import randint
from time import sleep

jogo = []

n = int(input('Quantos jogos deseja sortear: '))

print('GERANDO JOGOS: ')
print('-='*10, end='')
print(f'{"< Jogos! >":^5}', end='')
print('-='*10)

for c in range(0, n):
    for i in range(0, 6):
        valor = randint(1, 60)
        if valor in jogo:
            valor = randint(1, 60)
            jogo.append(valor)
        else:
            jogo.append(valor)

    print(f'Jogo {c + 1}: {jogo}')
    sleep(1)

    jogo.clear()

print('-='*10, end='')
print(f'{"< BOA SORTE! >":^5}', end='')
print('-='*8, end='')
