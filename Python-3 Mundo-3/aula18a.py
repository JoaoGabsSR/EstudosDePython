dados = list()

dados.append('Pedro')
dados.append(27)

pessoas = list()

pessoas.append(dados[:])
pessoas.append(['Maria', 19])
pessoas.append(['João', 32])

galera = list()
dado = list()

for c in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))

    galera.append((dado[:]))

    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade.')
