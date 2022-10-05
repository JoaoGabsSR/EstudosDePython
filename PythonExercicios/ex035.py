n1 = float(input('Digite um valor para o primeiro lado do triângulo: '))
n2 = float(input('Digite um valor para o segundo lado do triângulo: '))
n3 = float(input('Digite um valor para o terceiro lado do triângulo: '))

if n1 > abs(n2 - n3) and n1 < (n2 + n3):
    print('Com esses valores pode-se formar um triângulo!')
elif n2 > abs(n1 - n3) and n2 < (n1 + n3):
    print('Com esses valores pode-se formar um triângulo!')
elif n3 > abs(n1 - n2) and n3 < (n1 + n2):
    print('Com esses valores pode-se formar um triângulo!')
else:
    print('Com esses valores não será possível formar um triângulo!')
