nome = input('Digite seu nome: ')

espacos = nome.count(' ')
priNome = nome.split()

print('Nome com todas as letras em maiúsculo: {}'.format(nome.upper()))
print('Nome com todas as letras em minúsculo: {}'.format(nome.lower()))
print('Número de letras totais no nome(espaços não contabiizados): {}'.format(len(nome) - espacos))
print('O primeiro nome possui {} letras.'.format(len(priNome[0])))
