sentence = input('Digite algo: ').lower().lstrip().rstrip()

print('A letra "A" aparece {} vezes.'.format(sentence.count('a')))
print('A primeira ocorrência da letra "A" nessa sentença é na posição {}.'.format(sentence.find('a')+1))
print('A última ocorrência da letra "A" nessa sentença é na posição {}.'.format(sentence.rfind('a')+1))
