primeiro = float(input('Digite um valor: '))
segundo = float(input('Digite um valor: '))

resultado = 0
maior = 0

print('''Opções: 
[ 1 ] - Somar
[ 2 ] - Multiplicação
[ 3 ] - Maior
[ 4 ] - Novos Números
[ 5 ] - Sair do programa''')
opcao  = int(input('Escolha: '))

while opcao != 5:
    if opcao not in [1, 2, 3, 4, 5]:
        print('Opção Inválida! Tente Novamente!')

    if opcao == 1:
        resultado = primeiro + segundo
        print(f'Resultado da soma: {resultado}')
        print('-=' * 15)

    if opcao == 2:
        resultado = primeiro * segundo

        print(f'Resultado da multiplicação: {resultado}')
        print('-=' * 15)

    if opcao == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo

        print(f'Maior Valor: {maior}')
        print('-=' * 15)

    if opcao == 4:
        print('Entre com os novos valores: ')
        primeiro = int(input('Primeiro: '))
        segundo = int(input('Primeiro: '))
        print('-=' * 15)

    print('''Opções: 
    [ 1 ] - Somar
    [ 2 ] - Multiplicação
    [ 3 ] - Maior
    [ 4 ] - Novos Números
    [ 5 ] - Sair do programa''')
    opcao = int(input('Escolha: '))

print('FIM DO PROGRAMA!')
