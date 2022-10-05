s = n = c = 0

while n != 999:
    n = int(input('Digite um número [digite 999 para parar o programa]: '))
    if n == 999:
        s += 0
    else:
        s += n
        c += 1

print(f'Você digitou {c} números e a soma deles é {s}')