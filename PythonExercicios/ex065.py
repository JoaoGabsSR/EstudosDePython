s = 0
maior = 0
menor = 0
c = 0

while True:
    n = int(input('Digite um número: '))
    c += 1

    s += n

    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n

        if n < menor:
            menor = n

    continuar = input('Deseja contiuar[S/N]: ').strip()

    if continuar in 'nN':
        break

print(f'''Você digitou {c} números e a média foi {s / c:.2f}.
O maior valor foi {maior} e o menor foi {menor}.''')
