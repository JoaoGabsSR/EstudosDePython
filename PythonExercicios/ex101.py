from datetime import datetime


def calcidadevoto(anonascimento=datetime.now().year):
    """
    -> Calcula a idade com base na ano de nascimento e informa se é possível votar ou não
    :param anonascimento: ano do nascimento da pessoa, caso não seja informaddo recebera o ano atual
    :return: str
    """

    anoatual = datetime.now().year

    if anoatual - anonascimento >= 18:
        return 'VOTO OBRIGATÓRIO'
    elif anoatual - anonascimento <=17 and anoatual - anonascimento >= 16:
        return 'VOTO OPCIONAL'
    else:
        return 'IDADE IMPOSSIBILITA O VOTO'


ano = int(input('Digite seu ano de nascimento: '))
idade = anoatual = datetime.now().year - ano
voto = calcidadevoto(ano)

print(f'Com {idade} anos: {voto}!')
