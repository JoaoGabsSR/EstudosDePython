jogador = dict()
gols = list()

jogador['nome'] = input('Nome do Jogador: ').strip().lower().capitalize()
p = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
t = 0

for c in range(0, p):
    g = int(input(f'Quantos gols na {c + 1}ª partida: '))
    t += g
    gols.append(g)

jogador['gols'] = gols
jogador['total'] = t

print('-='*25)
print(jogador)

print('-='*25)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-='*25)
print(f'O jogador {jogador["nome"]} jogou {p} partida(s): ')

for c in range(0, p):
    print(f'    => Na partida {c + 1}, fez {jogador["gols"][c]} gols.')

print(f'Foi um total de {jogador["total"]} de gols nesses {p} jogo(s).')
