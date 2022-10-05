from random import randint

itens = ['pedra', 'papel', 'tesoura']
computador = randint(0, 2)

print('''Suas opções: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Escolha: '))

print('O computador jogou {}.'.format(itens[computador]))
print('O jogador jogou {}.'.format(itens[jogador]))

if computador == 0: #compuatdor jogou pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('A VITÓRIA É DO: Jogador. O computador perdeu')
    elif jogador == 2:
        print('A VITÓRIA É DO: Computador. O jogador perdeu')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #compuatdor jogou papel
    if jogador == 0:
        print('A VITÓRIA É DO: Computador. O jogador perdeu')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('A VITÓRIA É DO: Jogador. O computador perdeu')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #compuatdor jogou tesoura
    if jogador == 0:
        print('A VITÓRIA É DO: Jogador. O computador perdeu')
    elif jogador == 1:
        print('A VITÓRIA É DO: Computador. O jogador perdeu')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
