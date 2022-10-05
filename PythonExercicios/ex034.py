salario = float(input('Digite seu salário: R$ '))

if salario > 1250:
    print('Houve um ajuste em seu salário, o novo valor pe de R$ {}'.format(salario + (salario * 0.1)))
else:
    print('Houve um ajuste em seu salário, o novo valor pe de R$ {}'.format(salario + (salario * 0.15)))
