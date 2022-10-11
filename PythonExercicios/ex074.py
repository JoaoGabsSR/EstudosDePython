from random import randint

valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram: {valores[0]} {valores[1]} {valores[2]} {valores[3]} {valores[4]}')
print(f'O maior valor é: {max(valores)}')
print(f'O menor valor é: {min(valores)}')
