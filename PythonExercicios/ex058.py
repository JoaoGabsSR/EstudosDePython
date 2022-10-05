from random import randint

computador = randint(0, 10)
tentativas = 1

print(f'''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar ?''')
jogador = int(input('Qual seu palpite: '))

while jogador != computador:
    if jogador > computador:
        jogador = int(input('Menos... Tente novamente: '))
        tentativas += 1

    if jogador < computador:
        jogador = int(input('Mais... Tente novamente: '))
        tentativas += 1

print(f'''Parabéns, você acertou o múmero em que pensei!
Com um total de {tentativas} tentativas.''')
