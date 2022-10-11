jogador = dict()
gols = list()
time = list()

while True:
    jogador.clear()
    t = 0
    jogador['nome'] = input('Nome do Jogador: ').strip().lower().capitalize()
    p = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

    gols.clear()

    for c in range(0, p):
        g = int(input(f'Quantos gols na {c + 1}ª partida: '))
        t += g
        gols.append(g)

    jogador['gols'] = gols.copy()
    jogador['total'] = t

    time.append(jogador.copy())

    resp = input('Deseja continuar[S/N]: ').upper().strip()[0]
    while resp not in 'SN':
        print('Digite somente S ou N!!!')
        resp = input('Deseja continuar[S/N]: ').upper().strip()[0]

    if resp == 'N':
        break

print('-='*40)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-='*40)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*40)

while True:
    busca = int(input('Mostra dados de qual jogador: (999 para parar) '))

    if busca == 999:
        break
    if busca >= len(time):
        print('Erro! Não há jogador com esse código: ')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i + 1} fez {g} gol(s)')
    print('-=' * 40)
    
print('<<< Volte Sempre >>>')
