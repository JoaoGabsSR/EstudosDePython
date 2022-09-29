import math

catOposto = float(input('Digite o cateto oposto do triângulo: '))
catAdjacente = float(input('Digite o cateto adjacente do trinângulo: '))

hipotenusa = math.sqrt(math.pow(catOposto, 2) + math.pow(catAdjacente, 2))

print('A hipotenusa desse triângulo retangulo é {:.1f}'.format(hipotenusa))
