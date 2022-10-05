nMulher = idade = mIdade = sIdade = m = 0
sexo = nome = mIdadeNome = ''

for c in range(0,4):
    print(f'----- {c + 1}ª pessoa -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ').strip()

    if c == 0:
        mIdade = idade

    if sexo in 'Mm' and idade > mIdade:
        mIdade = idade
        mIdadeNome = nome

    if sexo in 'Ff' and idade < 20:
        nMulher += 1

    sIdade += idade

m = sIdade / 4

print(f'''A média de idade do grupo é de {m:.1f}. 
O homem mais velho tem {mIdade} anos e se chama {mIdadeNome}. 
Ao todo são {nMulher} mulheres com menos de 20 anos.''')
