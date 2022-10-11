pessoas = list()
temp = list()
c = 0
min = 0
max = 0

while True:
    temp.append(input('Nome: ').lower().capitalize())
    temp.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        min = max = temp[1]
    else:
        if temp[1] > max:
            max = temp[1]

        if temp[1] < min:
            min = temp[1]

    pessoas.append(temp[:])

    temp.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar[S/N]: ').upper().strip()[0]

    if continuar == 'N':
        break

print(f'Os dados cadastrados foram: {pessoas}.')
print(f'Foram cadastrados ao todo: {len(pessoas)} cadastros.')

print(f'O maior peso foi de {max} Kg. As pessoas cadastradas com ess pesso foram: ', end='')
for p in pessoas:
    if p[1] == max:
        print(f'{p[0]}')

print(f'\nO menor peso foi de {min} Kg. As pessoas cadastradas com ess pesso foram: ', end='')
for p in pessoas:
    if p[1] == min:
        print(f'{p[0]}')
