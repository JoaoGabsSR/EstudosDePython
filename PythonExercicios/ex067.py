while True:
    n = int(input('Digite um número(números negativos encerrão o programa): '))

    if n > 0:
        for c in range(1, 11):
            print(f'{n} x {c} = {n * c}')
    else:
        break
    print('-' * 30)

    '''
    repetir = input('Deseja repetir[S/N]: ').strip().upper()

    if repetir in 'Nn':
        break
    '''

print('Programa encerrado!')
