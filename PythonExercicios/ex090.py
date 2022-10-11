aluno = dict()

aluno['nome'] = input('Nome: ').lower().capitalize().strip()
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))
if aluno['media'] > 6.9:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] <= 6.9 and aluno['media'] >= 4:
    aluno['situacao'] = 'Em Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print('-='*20)

print(f'''--- Nome do Aluno: {aluno["nome"]}
--- Média de {aluno["nome"]}: {aluno["media"]}
--- Situação do aluno: {aluno["situacao"]}''')
