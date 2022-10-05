import datetime

anoInformado = int(input('Que ano deseja analisar ? Coloque 0 para analisar o ano atual: '))

if anoInformado != 0:
    if anoInformado % 4 == 0 and anoInformado % 100 != 0 or anoInformado % 400 == 0:
        print('O ano {} é bissexto'.format(anoInformado))
    else:
        print('O ano {} não é bissexto'.format(anoInformado))
else:
    ano = datetime.date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('O ano atual é bissexto.')
    else:
        print('O ano atual não é bissexto.')
