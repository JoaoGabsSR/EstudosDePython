distancia = int(input('Digite a distância da viagem: '))

if distancia <= 200:
    valor = distancia * 0.5
    print('O preço total de sua viagem é de: R$ {}'.format(valor))
else:
    valor = distancia * 0.45
    print('O preço total de sua viagem é de: R$ {}'.format(valor))
