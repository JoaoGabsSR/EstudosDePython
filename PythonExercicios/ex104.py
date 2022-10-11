def leiaInt(txt):
    ok = False
    valor = 0

    while True:
        n = input(txt)

        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[1;31mERRO! Digite um número inteiro válido\033[m')

        if ok:
            break

    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')
