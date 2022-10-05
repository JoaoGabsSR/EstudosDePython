primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
mais = 10
total = 0

while mais != 0:
    total += mais
    while c <= 10:
        print('{} -> '.format(termo), end='')
        termo += razao
        c += 1

    print('PAUSA')

    mais = int(input('Quantos termos você quer mostrar a mais: '))

print(f'Progrssão finalizada com {total} termos mostrados.')
