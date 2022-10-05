valorCasa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite agora o seu salário: R$ '))
anosParaPagar = float(input('Digite em quantos anos pretende pagar: '))

prestacaoMensal = valorCasa / (anosParaPagar * 12)

if prestacaoMensal <= (salario * 0.3):
    print('Cada prestação será de R${:.2f}'.format(prestacaoMensal))
    print('Seu empréstimo para a compra da casa foi aprovado!')
else:
    print('Cada prestação será de R${:.2f}'.format(prestacaoMensal))
    print('Seu empréstimo para a compra da casa foi negado')