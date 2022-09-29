cidade = input('Digite o nome da sua cidade: ')

nomeCidadeFormatado = cidade.lstrip().rstrip().lower()

print('O nome da cidade começa com "Santo": {}'.format(nomeCidadeFormatado.startswith('SANTO'.lower())))
