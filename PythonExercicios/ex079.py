numeros = list()

while True:
    valor = int(input('Digite um valor: '))
    if valor in numeros:
        print('Valor já adicionado!')
    else:
        numeros.append(valor)

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar adicionando valores[S/N]: ').strip().upper()

    if continuar == 'N':
        break

print(f'Você digitou os valores: {sorted(numeros)}')
