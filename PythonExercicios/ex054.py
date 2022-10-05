from datetime import date

mi = mn = 0
for c in range(0, 7):
    n = int(input('Digite o ano de seu nascimento: '))

    if date.today().year - n >= 18:
        mi += 1
    else:
        mn += 1
print(f'O número de pessoas maior de idade é {mi}')
print(f'O númeor de pessoas menor de idade é {mn}')
