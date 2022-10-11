from time import sleep

def linha(dsn, n):
    print(f'{dsn}'*n)

def maior(*nums):

    if len(nums) == 0:
        print('Nenhum valor foi informado.')
        print('O maior valor não existe.')
    else:
        for n in nums:
            print(f'{n}', end=' ')
            sleep(0.6)

        print(f'Foram informados {len(nums)} ao todo.')
        print(f'O maior valor informado foi {max(nums)}')


linha('-=', 25)
print('Analisando valores passados... ')
maior(2, 9, 4, 5, 7, 1)

linha('-=', 25)
print('Analisando valores passados... ')
maior(4, 7, 0)

linha('-=', 25)
print('Analisando valores passados... ')
maior(1, 2)

linha('-=', 25)
print('Analisando valores passados... ')
maior(6)

linha('-=', 25)
print('Analisando valores passados... ')
maior()
