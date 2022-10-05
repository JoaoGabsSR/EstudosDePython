preco = float(input('Informe o preço de sua compra: R$'))
escolha = int(input('Qual vai ser a forma de pagamento: '
                    '\n[ 1 ] - À vista(dinheiro/cheque) com 10% de desconto'
                    '\n[ 2 ] - À vista(cartão) com 5% de descono'
                    '\n[ 3 ] - Parcelado(2 vezes)'
                    '\n[ 4 ] - Parcelado(3 vezes ou mais) com juros de 20%'
                    '\nForma de pagamento: '))

if escolha == 1:
    print('Escolha: Pagamento à vista(dinheiro ou cheque).')
    print('O pagamento final será de R${:.2f}'.format(preco - (preco * 0.1)))
elif escolha == 2:
    print('Escolha: Pagamento à vista(cartão).')
    print('O pagamento final será de R${:.2f}'.format(preco - (preco * 0.05)))
elif escolha == 3:
    print('Escolha: Pagamento parcelado(2 vezes).')
    print('O pagamento final será de R${:.2f}, cada parcela terá o preço de R${}'.format(preco, preco / 2))
elif escolha == 4:
    print('Escolha: Pagamento parcelado(3 vezes ou mais).')
    vezes = int(input('Quantas vezes você deseja parcelar: '))
    print('O pagamento final será de R${:.2f}, cada parcela terá o preço de R${:.2f}'.format(preco + (preco * 0.2), (preco + (preco * 0.2)) / vezes))
else:
    print('Opção digitada inválida, tente novamente.')
