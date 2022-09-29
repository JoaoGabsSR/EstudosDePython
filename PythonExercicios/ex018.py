import math

a = float(input('Digite o ângulo: '))
rad = math.radians(a)

print('Do ângulo {}º temo: \n'.format(a),
      'Seno: {:.3f}\n'.format(math.sin(rad)),
      'Cosseno: {:.3f}\n'.format(math.cos(rad)),
      'Tangente: {:.3f}'.format(math.tan(rad)))
