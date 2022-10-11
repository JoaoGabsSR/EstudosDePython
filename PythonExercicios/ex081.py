valores = []
c = 0

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
    else:
        print('Valor já adicionado anteriormente.')

    valores.sort(reverse=True)

    c += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar[S/N]: ').strip().upper()[0]

    if continuar == 'N':
        break

print(f'Você digitou {c} elementos.')
print(f'Os valores em ordem decrescente são: {valores}')
print(f'O valor {5} faz parte da lista' if 5 in valores else f'O valor {5} não faz parte da lista')
