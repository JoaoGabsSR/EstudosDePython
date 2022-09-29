import random as rand

a1 = input('Informe o nome do aluno: ')
a2 = input('Informe o nome do aluno: ')
a3 = input('Informe o nome do aluno: ')
a4 = input('Informe o nome do aluno: ')

ordem = [a1, a2, a3, a4]
rand.shuffle(ordem)
print('A ordem da apresentação será'
      ':\n {},\n {},\n {},\n {}'.format(ordem[0], ordem[1], ordem[2], ordem[3]))
