def ficha(nome='', gols=''):

    if nome == '' and gols == '':
        return f'O jogador <desconhecido> fez 0 gols no campeonato.'
    elif nome == '':
        return f'O jogador <desconhecido> fez {gols} gols no campeonato.'
    else:
        return f'O jogador {nome} fez {gols} gols no campeonato.'


nome = input('Nome do Jogador: ')
g = input('Número de Gols: ')
print(ficha(nome, g))
