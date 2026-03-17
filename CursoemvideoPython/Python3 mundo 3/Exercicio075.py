num = (int(input('Digite um numero : ')),
           int(input('Digite um numero : ')), 
           int(input('Digite um numero : ')),
           int(input('Digite um numero : ')))
print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O valor 3 apareceu na {num.index(3)+1} posição ')