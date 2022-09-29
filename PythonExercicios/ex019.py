import random as rand

a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome do aluno: ')
a3 = input('Digite o nome do aluno: ')
a4 = input('Digite o nome do aluno: ')

alunoEscolhido = rand.choice([a1, a2, a3, a4])
print('O aluno escolhido para apagar o quadro foi: {}'.format(alunoEscolhido))
