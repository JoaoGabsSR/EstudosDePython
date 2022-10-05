km = int(input('Qual a velocidade atual do carro: '))

if km <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Opa, você está muito rápido deverá pagar uma multa de R$ {:.2f}'.format(7 * (km - 80)))
