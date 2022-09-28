something = input('Digite algo: ')

print('Você digitou {}'.format(something))
print('O tipo de dado é: {}'.format(type(something)))

print('Só tem espaços:', something.isspace())
print('É um número:', something.isnumeric())
print('É alfabético:', something.isalpha())
print('É alfanumérico:', something.isalnum())
print('Está em maiúsculo:', something.isupper())
print('Está em minúsculo:', something.islower())
print('Está capitalizada:', something.istitle())
