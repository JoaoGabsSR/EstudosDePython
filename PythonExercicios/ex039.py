from datetime import date

anoNascimento = int(input('Informe a ano de seu nascimento: '))
anoAtual = date.today().year

if (anoAtual - anoNascimento) < 18:
    print('Você ainda não está na idade de se alistar no exército, espere mai um pouco.')
    print('Anda falta {} ano(s) para que se você possa se alistar.'.format(18 - (anoAtual - anoNascimento)))
elif (anoAtual - anoNascimento) == 18:
    print('Você já tem idade de se alistar no exército, procure o posto militar mais próximo de sua residência.')
else:
    print('Você já passou da idade de se alistar, caso já esteja alistado ignore está mensagem, caso não, procure o posto militar mais próximo de sua residência.')
    print('Caso ainda não tenha se alistado, passou-se {} ano(s).'.format((anoAtual - anoNascimento) - 18))
