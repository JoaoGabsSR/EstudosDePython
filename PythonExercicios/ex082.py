valores = []
pares = []
impares = []

while True:
    n = int(input('Digite um valor: '))
    valores.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar[S/N]: ').strip().upper()[0]

    if continuar == 'N':
        break


print(f'''A lista completa é {valores}.
A lista de pares é {pares.sort()}.
A lista de ímpares é {impares.sort()}.''')
