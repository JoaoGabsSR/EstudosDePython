nome = input('Digite seu nome completo: ').lstrip().rstrip()
n = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {} e seu último nome é {}.'.format(n[0], n[len(n) - 1]))
