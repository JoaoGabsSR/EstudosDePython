primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
c = primeiro

while c <= decimo:
    print(f'{c} ', end='-> ')
    c += razao

print('Acabou!')
