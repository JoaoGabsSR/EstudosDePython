expre = input('Digite a expressão: ')
pilha = list()

for sim in expre:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) > 0:
    print('Sua expressão não é válida.')
else:
    print('Sua expressão é válida.')
