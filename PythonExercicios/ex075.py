valores = (
    int(input('Digite o primeiro número: ')),
    int(input('Digite o segundo número: ')),
    int(input('Digite o terceiro número: ')),
    int(input('Digite o quarto número: '))
)

print(f'Você digitou os valores: {valores}')
print(f'O valor {9} apareceu {valores.count(9)} vezes.' if 9 in valores else f'O valor {9} não foi digitado.')
print(f'O valor {3} apareceu na {valores.index(3) + 1}ª posição.' if 3 in valores else f'O valor {3} não foi digitado.')
print('O valores pares digitados foram: ', end='')

for v in valores:
    if v % 2 == 0:
        print(v, end=' ')
