frase = input('Digite um frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print(f'Você digitou a frase {junto}.')

'''
inverso = junto[::-1]
'''

'''
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
'''

print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('Temos um palídromo!')
else:
    print('Não é um palídromo')
