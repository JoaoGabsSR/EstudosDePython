from datetime import date

anoNascimento = int(input('Informe o ano de nascimento do competidor: '))
anoAtual = date.today().year

print('A idade do competidor é de {} anos.'.format(anoAtual - anoNascimento))
if (anoAtual - anoNascimento) <= 9:
    print('Categoria: Mirim')
elif (anoAtual - anoNascimento) >= 10 and (anoAtual - anoNascimento) <= 14:
    print('Categoria: Infantil')
elif (anoAtual - anoNascimento) >= 15 and (anoAtual - anoNascimento) <= 19:
    print('Categoria: Junior')
elif (anoAtual - anoNascimento) == 20:
    print(('Categoria: Sênior'))
else:
    print('Categoria: Master')
