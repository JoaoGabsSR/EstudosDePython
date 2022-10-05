termos = int(input('Quanto termos deseja mostrar: '))
np = 0
ns = 1
c = 3

print(f'{np} -> {ns}', end='')

while c <= termos:
    nt = np + ns
    print(f' -> {nt}', end='')
    np = ns
    ns = nt
    c += 1

print(' -> Acabou!')
