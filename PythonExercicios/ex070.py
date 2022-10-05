totalGasto = maisDeMil = maisBarato = c = 0
nomeMaisBarato = ''

while True:
    nomeProduto = input('Nome do produto: ')
    preco = float(input('Preço: R$'))

    totalGasto += preco

    if c == 0:
        maisBarato = preco
        nomeMaisBarato = nomeProduto

    c += 1

    if preco > 1000:
        maisDeMil += 1

    if preco < maisBarato:
        maisBarato = preco
        nomeMaisBarato = nomeProduto

    continuar = ' '

    while continuar not in 'SN':
        continuar = input('Deseja continuar [S/N]: ').strip().upper()[0]

    if continuar == 'N':
        break

print(f'''Total Gasto: R${totalGasto:.2f}
Quantidade de produtos que custam mais de R$1000.00: {maisDeMil}
Produto mais barato: {nomeMaisBarato} (R${maisBarato:.2f})''')
