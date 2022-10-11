times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corithians', 'Flamengo', 'Atlético-PR', 'Atlético-MG', 'América-MG',
         'Fortaleza', 'Botafogo', 'Santos', 'Goiás', 'São Paulo', 'Bragantino', 'Coritiba', 'Ceará SC', 'Cuiabá', 'Avaí',
         'Atlético-GO', 'Juventude')

print(f'Lista de Times do Brasileirão: {times}')
print('>=<'*150)

print(f'Os cinco primeros são: {times[:5]}')
print('>=<'*94)

print(f'Os 4 últimos são: {times[16:]}')
print('>=<'*94)

print(f'Times em orfem alfabética: {sorted(times)}')
print('>=<'*94)

print(f'Chapecoense está na posição {times.index("Chapecoense")}' if 'Chapecoense' in times else 'Chapecoense não está na serié A do Brasileirão')
print('>=<'*94)
