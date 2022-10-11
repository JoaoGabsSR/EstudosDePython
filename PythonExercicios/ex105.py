def notas(*nums, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param nums: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações spbre a situação da turma
    """

    aluno = dict()

    aluno['total'] = len(nums)
    aluno['maior'] = max(nums)
    aluno['menor'] = min(nums)
    aluno['media'] = sum(nums)/len(nums)

    if sit:
        if aluno['media'] > 6.9:
            aluno['situacao'] = 'BOA'
        elif aluno['media'] <= 6.9 and aluno['media'] >= 5:
            aluno['situacao'] = 'MEDIANA'
        else:
            aluno['situacao'] = 'RUIM'

    return aluno


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
