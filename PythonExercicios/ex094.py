dadosTemp = dict()
cadastros = list()

while True:
    nome = input('Nome: ').strip().lower().capitalize()
    sexo = input('Sexo[M/F]: ').strip()[0]
    while sexo not in 'MF':
        sexo = input('Erro: Digite somente M ou F. Sexo[M/F]: ').strip()[0]
    idade = int(input('Idade: '))

    dadosTemp['nome'] = nome
    dadosTemp['sexo'] = sexo
    dadosTemp['idade'] = idade

    cadastros.append(dadosTemp.copy())

    resp = input('Deseja continuar[S/N]: ').strip()[0]
    while resp not in 'SN':
        resp = input('Erro: Somente digite S ou N. Deseja continuar[S/N]: ').strip()[0]

    if resp == 'N':
        break

print('-='*30)

s = 0

for c in cadastros:
    s += c['idade']

m = s / len(cadastros)

print(f'''A) Ao todo temos {len(cadastros)} cadastrada(s)
B) A média de idade é de {m:.2f} anos''')

print('C) As mulheres cadastradas são: ')
for c in cadastros:
    if c['sexo'] == 'F':
        print(f'    - {c["nome"]};')

print('\nD) Lista das pessoas que estão acima da média: ')
for c in cadastros:
    if c['idade'] > m:
        print(f'    nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]}')

print('<<< Encerrado >>>')
