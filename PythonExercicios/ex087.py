matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sP = sTC = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Gite um valor para {[l, c]}: '))

print('='*60)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:^4}', end='')
    print()

print('='*60)

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            sP += matriz[l][c]

        if l == 0 and c == 0:
            maior = matriz[l][c]
        else:
            if l == 1 and matriz[1][c] > maior:
                maior = matriz[1][c]

    sTC += matriz[l][2]

print(f'''A soma dos valores pares são: {sP}.
A soma dos valores da terceira coluna são: {sTC}.
O maior valor da segunda linha é {maior}''')
