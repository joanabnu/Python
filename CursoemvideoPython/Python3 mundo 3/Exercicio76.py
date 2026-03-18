listagem = ('Lapis', 1.75,
            'Borracha',2,
            'Estojo', 25,
            'Tranferidor',4.20,
            'Compasso', 9.99,
            'Mochila',120.99,
            'Canetas',22.38,
            'Livro', 34.90)
print('=='*30)
print('Listagem de preço')
print('=='* 30)
for item in range(0,len(listagem)):
    if item % 2 == 0:
      print(f'{listagem[item]:.<30}',end='')
    else: 
       print(f'R${listagem[item]:>7}')