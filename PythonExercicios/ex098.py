from time import sleep

def linha(dsn, n):
    print(f'{dsn}'*n)

def contagem(start, end, jump):

    if jump == 0:
        print('Erro! Não se pode contar e 0 em 0, o valor da contagem será de 1 em 1.')
        jump = 1

    if start < end:
        n = start

        while n <= end:
            print(n, end=' ')
            n += jump
            sleep(0.7)
    else:
        n = start

        while n >= end:
            print(n, end=' ')
            n -= jump
            sleep(0.7)


linha('-=', 25)
print('Contagem de 1 até 10 de 1 em 1:')

contagem(1, 10, 1)

print('FIM!')

linha('-=', 25)
print('Contagem de 10 até 0 de 2 em 2:')

contagem(10, 0, 2)

print('FIM!')

linha('-=', 25)
print('Sua contagem')
inicio = int(input('Início: '))
fim = int(input('Final: '))
pulo = int(input('De quanto em quanto: '))

linha('-=', 25)
print(f'Contagem de {inicio} até {fim} de {pulo} em {pulo}:')

contagem(inicio, fim, pulo)

print('FIM!')
