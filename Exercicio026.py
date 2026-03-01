frase = str(input('Digite uma frase : ')).upper().strip()
print('A letra a aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'. format(frase.find('A')+1))
print('A ultimo letra A aparece na posicão {}'.format(frase.rfind('A')+1))
