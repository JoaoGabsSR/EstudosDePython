from exercicios import moeda

p = float(input('Digite o valor: R$'))
print(f'''A metade de {moeda.moeda(p)} é {moeda.metade(p, format=True)}.
O dobro de {moeda.moeda(p)} é {moeda.dobrar(p, format=True)}.
Aumentando 10%, temos {moeda.aumentar(p, 10, format=True)}.
Reduzindo 13%, temos {moeda.diminuir(p, 13, format=True)}''')
