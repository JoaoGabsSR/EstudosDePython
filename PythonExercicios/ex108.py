from exercicios import moeda

p = float(input('Digite o valor: R$'))
print(f'''A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.
O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobrar(p))}.
Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}.
Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}''')
