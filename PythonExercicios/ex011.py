largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite o comprimento da parede: '))

area = largura * altura

print('Será necessario {} litros de tinta para pintar a parede'.format(area / 2))
