nome = input('Entre com seu nome: ')
if nome == 'João':
    print('Seu nome é bem bonito')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil')
elif nome in 'Ana Moana Giovanna Carla':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')

print('Tenha um bom dia {}'.format(nome))
