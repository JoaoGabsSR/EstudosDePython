valores= list()

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))

print(f'Você digitou os valores: {valores}')

print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for c in range(0, 5):
    if valores[c] == max(valores):
        print(f'{c}... ', end='')

print(f'\nO menor valor digitado foi {max(valores)} nas posições ', end='')
for c in range(0, 5):
    if valores[c] == min(valores):
        print(f'{c}... ', end='')
