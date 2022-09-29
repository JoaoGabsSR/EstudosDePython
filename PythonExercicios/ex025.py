nome = input('Digite seu nome: ')

lowerName = nome.lower()
splitName = lowerName.split()

print('O nome contém "Silva" em algum lugar: {}'.format(splitName.__contains__('silva')))
