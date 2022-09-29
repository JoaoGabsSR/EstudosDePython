km = float(input('Digite quantos kilometros você rodou ao todo: '))
dias = int(input('Informa quantos dias você alugou o carro: '))

pagamentoTotal = (km * 0.15) + (dias * 60)

print('O valor total a ser pago é de: R$ {:.2f}.'.format(pagamentoTotal))
