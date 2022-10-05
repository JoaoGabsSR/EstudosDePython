import math

num = int(input('Digite um número inteiro qualquer: '))
baseConversao = int(input('Digite uma base de conversão: '
                          '\n1 - binário;'
                          '\n2 - octal;'
                          '\n3 - hexadecimal'
                          '\nEscolha: '))

if baseConversao == 1:
    print('{} convertido para binário é {}.'.format(num, bin(num)[2:]))
elif baseConversao == 2:
    print('{} convertido para octal é {}.'.format(num, oct(num)[2:]))
elif baseConversao == 3:
    print('{} convertido para hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('A opção digita é inválida, tente novamente.')
