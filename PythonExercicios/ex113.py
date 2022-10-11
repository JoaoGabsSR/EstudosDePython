def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))

        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite um número inteiro válido\033[m')

        except KeyboardInterrupt:
            print(f'O usuário interrompeu a execução do programa.')
            return 0
            break

        else:
            return n


def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt).replace(',', '.'))

        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite um número real válido\033[m')

        except KeyboardInterrupt:
            print(f'O usuário interrompeu a execução do programa.')
            return 0
            break

        else:
            return n


nI = leiaInt('Digite um número inteiro: ')
nR = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {nI} e o número real digitado foi {nR}')
