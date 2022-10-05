p = l = 0

for c in range(0, 5):
    peso = float(input(f'Digite o peso da {c + 1}ª pessoa: '))

    if c == 0:
        p = l = peso

    if peso > p:
        p = peso

    if peso < l:
        l = peso

print(f'O maior peso foi {p:.1f}Kg, e o menor peso foi {l:.1f}Kg')
