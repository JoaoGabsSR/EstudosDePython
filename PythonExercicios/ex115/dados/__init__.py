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
