quantidadeHomens = maior18 = mulherMenosVinte = 0

while True:
    print('-'*30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)

    idade = int(input('Idade: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]

    print('-' * 30)

    if sexo == 'M':
        quantidadeHomens += 1

    if idade > 18:
        maior18 += 1

    if sexo == 'F' and idade < 20:
        mulherMenosVinte += 1

    continuar = ' '

    while continuar not in 'SN':
        continuar = input('Deseja continuar [S/N]: ').strip().upper()[0]

    if continuar == 'N':
        break

print(f'''Total de pessoas com mais de 18 anos: {maior18}.
Homens Cadastrados: {quantidadeHomens}.
Mulheres com menos de 20 anos: {mulherMenosVinte}''')
