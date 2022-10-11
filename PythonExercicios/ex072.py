numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'desseseis', 'dessesete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número [0-20]: '))

    if n < 0 or n > 20:
        while True:
            n = int(input('Número digitado inválido. Digite outro [0-20]: '))

            if n > -1 and n < 21:
                break

    print(f'Número digitado por extenso: {numeros[n]}')

    continuar = ' '

    while continuar not in 'SN':
        continuar = input('Deseja continuar[S/N]: ').strip().upper()[0]

    if continuar == 'N':
        break

print('Acabou!')
