dados = dict()

dados = {'Nome': 'Pedro', 'Idade': 25}

#print(dados['Nome'])
#print(dados['Idade'])

dados['Sexo'] = 'M'

#print(dados)

del(dados['Idade'])

#print(dados)

filme = {
'Titulo': 'Star Wars',
'Ano': 1997,
'Diretor': 'George Lucas'
}

#print(filme)

#filme['Titulo'] = 'Star Wars: O Empério Contra Ataca'
#print(filme)

#print(filme.values())
#print(filme.keys())
#print(filme.items())

#for k, v in filme.items():
#    print(f'O {k} é {v}')

locadora = []
locadora.append(
    filme
)
locadora.append(
    {'Titulo': 'Avengers',
    'Ano': 2012,
    'Diretor': 'Joss Whedon'}
)
locadora.append(
    {'Titulo': 'Matrix',
    'Ano': 1999,
    'Diretor': 'Irmãos Wachowski'}
)

#print(locadora)

#for f in locadora:
#    print(f'Titulo: {f["Titulo"]} Ano: {f["Ano"]} Diretor: {f["Diretor"]}')

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ').lower().capitalize().strip()
    estado['sigla'] = input('Sigla do Estado: ').strip().upper()
    brasil.append(estado.copy())

print(brasil)
