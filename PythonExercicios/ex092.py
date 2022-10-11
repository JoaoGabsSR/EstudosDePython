from datetime import datetime

funcionario = dict()

funcionario['nome'] = input('Nome: ').lower().capitalize().strip()
funcionario['nascimento'] = int(input('Ano de Nascimento: '))
funcionario['ctps'] = int(input('Carteira de Trabalho (Digite 0 caso não tenha): '))

if funcionario['ctps'] == 0:
    print('-='*25)
    print(f'''-- Nome do Funcionario: {funcionario["nome"]}
-- Idade: {datetime.now().year - funcionario["nascimento"]}
-- CTPS: Não Possui''')
else:
    funcionario['contratacao'] = int(input('Ano da Contratação: '))
    funcionario['salario'] = float(input('Salário: R$'))

    print('-=' * 25)
    print(f'''-- Nome do Funcionario: {funcionario["nome"]}
-- Idade: {datetime.now().year - funcionario["nascimento"]}
-- CTPS: {funcionario["ctps"]}
-- Ano da Contratação: {funcionario["contratacao"]}
-- Salário: R${funcionario["salario"]:.2f}
-- Aposentadoria: {(datetime.now().year - funcionario["nascimento"]) + ((funcionario["contratacao"] + 65) - datetime.now().year)}''')
