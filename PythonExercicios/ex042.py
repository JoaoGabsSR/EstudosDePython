n1 = float(input('Digite um valor para o primeiro lado do triângulo: '))
n2 = float(input('Digite um valor para o segundo lado do triângulo: '))
n3 = float(input('Digite um valor para o terceiro lado do triângulo: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Com esses valores será possível formar um triângulo!')

    if n1 == n2 == n3:
        print('Esse trinângulo é equilátero.')
    elif n1 != n2 != n3 != n1:
        print('Esse trinângulo é escaleno.')
    else:
        print('Esse trinângulo é isóceles.')

else:
    print('Com esses valores não será possível formar um triângulo!')
