try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print(f'Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print(f'O usuário não informou os dados.')
except Exception as ex:
    print(f'O erro foi ocasionado por {ex.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print(f'Volte Sepre! Muito Obrigado.')
