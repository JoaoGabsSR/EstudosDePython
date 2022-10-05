sexo = input('Informe o sexo [M/F]: ').upper().strip()[0]
while sexo not in 'MmFf':
    sexo = input('Sexo informado inválido! Por favor informe corretamente [M/F]: ').upper()

print(f'Sexo {sexo} cadastrado com sucesso.')
