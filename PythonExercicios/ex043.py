peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu imc é {:.2f}, e está abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu imc é {:.2f}, e está  no peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu imc é {:.2f}, e está um pouco acima do peso ideal.'.format(imc))
elif imc >= 30 and imc < 35:
    print('Seu imc é {:.2f}, e está acima do peso.'.format(imc))
else:
    print('Seu imc é {:.2f}, e está muito acima do peso.'.format(imc))
