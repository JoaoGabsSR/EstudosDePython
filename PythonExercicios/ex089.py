ficha = list()

while True:
    nome = input('Nome: ').strip().lower().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    m = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], m])

    resp = input('Deseja continuar: ').strip().upper()[0]
    if resp == 'N':
        break

print('='*30)

print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

print('-'*26)

while True:
    opc = int(input('Mostrar notas de qual aluno: '))

    if opc <= len(ficha) - 1:
        print(f'Notas do aluno {ficha[opc][0]}: {ficha[opc][1]}')

    resp = input('Deseja algo: ').strip().upper()[0]
    if resp == 'N':
        break
    else:
        print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
        print('-' * 26)

        for i, a in enumerate(ficha):
            print(f'{i:<4}{a[0]:<10}{a[2]:>8}')

        print('-' * 26)
