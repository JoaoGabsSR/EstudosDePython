def calcTerreno(a, b):
    r = a * b
    print(f'A área de um terreno {a}x{b} é de {r}')


print('Controle de Terrenos')
print('-'*20)

largura = float(input('LARGURA: '))
comprimento = float(input('COMPRIMENTO: '))
calcTerreno(largura, comprimento)
