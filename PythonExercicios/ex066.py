s = c = 0

while True:
    n = int(input('Digite um número [digite 999 para parar o programa]: '))

    if n == 999:
        break
    else:
        s += n
        c += 1

print(f'Você digitou {c} números e a soma deles é {s}')
