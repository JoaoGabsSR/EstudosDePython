s = 0

for n in range(0, 6):
    num = int(input('Informe um número: '))

    if num % 2 == 0:
        s += num

print(f'A soma dos números pares digitados é de {s}.')
