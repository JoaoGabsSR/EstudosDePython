from exercicios import moeda

p = float(input('Digite o valor: R$'))
print(f'''A metade de R${p} é R${moeda.metade(p)}.
O dobro de R${p} é R${moeda.dobrar(p)}.
Aumentando 10%, temos R${moeda.aumentar(p, 10)}.
Reduzindo 13%, temos R${moeda.diminuir(p, 13)}''')
