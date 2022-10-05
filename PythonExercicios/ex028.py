from random import randint

print('Vou pensar em um número entre 0 e 5. Tente adivinhar qual é: ')

n = randint(0, 5)
res = int(input('Em qual número eu pensei ? '))

if res == n:
    print('Parabéns você acertou, o número em que pensei foi: {}'.format(n))
else:
    print('Desculpe, você errou, o número em que pensei foi {}'.format(n))


