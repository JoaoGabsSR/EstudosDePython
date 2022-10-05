from random import randint

jogador = computador = c = 0

print('''
=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=
        VAMOS JOGAR PAR OU ÍMPAR
=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=''')

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    jogadaJ = ''
    total = jogador + computador

    while jogadaJ not in 'PI':
        jogadaJ = input('Par ou Ímpar[P/I]: ').upper().strip()[0]

    print(f'Você jogou {jogador} e o computador {computador}. A soma é: {total}')

    if jogadaJ == 'P':
        if total % 2 == 0:
            print('Parabéns você VENCEU!')
            c += 1
        else:
            print('VOCÊ PERDEU!')
            break

    if jogadaJ == 'I':
        if total % 2 != 0:
            print('Parabéns você VENCEU!')
            c += 1
        else:
            print('VOCÊ PERDEU!')
            break

    print('Vamos jogar novamente...')

print(f'GAME OVER! Você venceu {c} vezes!')
