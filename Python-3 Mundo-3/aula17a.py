lanche = ['Hambúrger', 'Suco', 'Pizza', 'Pudim']

lanche[3] = 'Picole'
lanche.append('Cookie')
lanche.insert(0, 'Cachorro Quente')

#print(lanche)

lanche.pop(3) # or lanche.remove('Suco') or del(lanche[3])
lanche.pop()

#print(lanche)

valores = list(range(4, 11))

valores.sort(reverse=True)

#print(valores)
#print(len(valores))

#for c, v in enumerate(valores):
#    print(f'Na posição {c} o valor é {v}')

nums = list()

#for c in range(0, 5):
#    nums.append(int(input('Digite um valor: ')))

#print(nums)

a = [1, 2, 3, 7]
b = a[:]

b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
