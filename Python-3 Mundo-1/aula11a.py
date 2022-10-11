print('\033[1;34;40mOlá Mundo!\033[m')

nome = 'João'
print('Olá! Seja muito bem vindo {}{}{}'.format('\033[4;36m', nome, '\033[m'))

cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'vermelho' : '\033[31m',
         'amarelo' : '\033[33m',
         'pretoebranco' : '\033[7;30m'}
print('Olá! Seja muito bem vindo {}{}{}'.format(cores['azul'], nome, cores['limpa']))
