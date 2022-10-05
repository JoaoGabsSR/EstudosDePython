nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('O aluno foi reprovado com a média de {:.1f}.'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('O aluno está em recuperação devido a média de {:.1f}.'.format(media))
else:
    print('O aluno foi aprovado pela média de {:.1f}.'.format(media))
