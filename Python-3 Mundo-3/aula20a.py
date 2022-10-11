def soma(a, b):
    return a + b

def contador(*num):
    print(num)

def dobraValores(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1

def soma(* valores):
    s = 0
    for n in valores:
        s += n

    print(s)


#PROGRAMA PRINCIPAL
#print(soma(4, 5))
#print(soma(b=6, a=9))

#contador(2, 1, 7)
#contador(4, 4, 7, 6, 2)

valores = [7, 2, 5, 0, 4]
dobraValores(valores)
#print(valores)

#soma(2, 5, 6, 7, 10)
